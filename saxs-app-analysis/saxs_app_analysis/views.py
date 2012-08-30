from django.shortcuts import render_to_response
from django.utils import simplejson as json
from django.http import HttpResponse

from saxs_model_analysis.models import Experiment
from saxs_model_analysis.models import AverageSubtractedImage
from saxs_model_analysis.models import DamVolume

# import and configure matplotlib library
import os
import StringIO
import Image
from django.conf import settings
try:
    os.environ['HOME'] = settings.MATPLOTLIB_HOME
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as pyplot
    is_matplotlib_imported = True
except ImportError:
    is_matplotlib_imported = False
    
################################################################################
# Functions for dealing with HTML templates
################################################################################

def main(request, epn="", type="avg_sub_images"):     
    topnav_highlight = get_topnav_highlight(view_id = "analysis_%s" % (type))
    epns = Experiment.objects.values_list('epn', flat=True).distinct().order_by('epn')
    tabs = []
    this_epn = ""
    if epns:
        if epn == "":
            this_epn = epns[0]
        else:
            this_epn = int(epn)
        experiments = Experiment.objects.filter(epn=this_epn).values_list('exp_name', flat=True).distinct().order_by('exp_name')
        tabs = [ [exp, exp] for exp in experiments ]
    
    
    content = { "topnav_highlight":   topnav_highlight,
                "epns":               epns,
                "this_epn":           this_epn,
                "tabs":               tabs,
               }

    return render_to_response('avg_sub_images.html', content)    


################################################################################
# Functions for fetching data required 
################################################################################

def get_data(type, epn, experiment):  
    if type == "avg_sub_images":
        data = get_data_avg_sub_images(epn, experiment)
        
    return data
    
def get_data_avg_sub_images(epn, experiment):
    avg_sub_images = AverageSubtractedImage.objects.filter(exp_fk__epn=epn, exp_fk__exp_name=experiment)
    dam_volumes = DamVolume.objects.filter(avg_sub_image_fk__in=avg_sub_images)
    mapping_volumes = {}
    for volume in dam_volumes:
        image_id = volume.avg_sub_image_fk.id
        dam_volume = volume.dam_volume
        pdf_file = volume.dammif_pdb_file
        if image_id not in mapping_volumes:
            mapping_volumes[image_id] = []
        if [dam_volume, pdf_file] not in mapping_volumes[image_id]:
            mapping_volumes[image_id].append([dam_volume, pdf_file])

    data = []
    for img in avg_sub_images:
        if img.id not in mapping_volumes: # no dam volumes associated to this image
            row = []
            row.append(img.location)
            row.append(img.location)
            row.append(img.porod_volume)
            row.append("NaN") # dam volume
            row.append("NaN") # pdb file
            data.append(row)
        else:
            volumes = mapping_volumes[img.id]
            for volume in volumes:
                row = []
                row.append(img.location)
                row.append(img.location)
                row.append(img.porod_volume)
                row.append(volume[0]) # dam volume
                row.append(volume[1]) # pdb file
                data.append(row)
        
    return data    

def get_json(type, epn, experiment):
    data = get_data(type, epn, experiment)
    content = '{"aaData": %s}' % (json.dumps(data))
    
    return HttpResponse(content, mimetype='application/json')  

def get_feed(request, type="avg_sub_images", epn="", experiment="", feed="json"):
    if feed=="json":
        response = get_json(type, epn, experiment)
        
    return response

################################################################################
# Functions for fetching profile plot required 
################################################################################
def get_profile_values(profile):
    profile = profile.rstrip('/')
    pf = open(profile, 'r')
    lines = pf.readlines()
    lines = lines[2:] # ignore the first lines
    xaxis = []
    yaxis = []
    for line in lines:
        columns = line.split()
        x = columns[0] #q
        y = columns[1] #I
        xaxis.append(x)
        yaxis.append(y)
    return (xaxis, yaxis)


def get_profile_png(request, profile):
    if is_matplotlib_imported:
        xaxis, yaxis = get_profile_values(settings.PROFILE_HOME + profile)
        pyplot.plot(xaxis, yaxis)
        pyplot.xlabel("q")
        pyplot.ylabel("Intensity, log I(q)")
        pyplot.grid(True)
        
        # set size
        ratio = 1.5
        fig = pyplot.gcf()
        default_size = fig.get_size_inches()
        fig.set_size_inches(default_size[0] * ratio, default_size[1] * ratio)
        
        # Write PNG image
        buffer = StringIO.StringIO()
        canvas = pyplot.get_current_fig_manager().canvas
        canvas.draw()
        img = Image.fromstring('RGB', canvas.get_width_height(), canvas.tostring_rgb())
        img.save(buffer, 'PNG')
        pyplot.close()
        # Django's HttpResponse reads the buffer and extracts the image
        return HttpResponse(buffer.getvalue(), mimetype='image/png')
    
    else:
        buffer = StringIO.StringIO()
        return HttpResponse(buffer.getvalue(), mimetype='image/png')


################################################################################
# Functions for dealing with top navigation bar in base template 
################################################################################

# mandatory function for filling the menu in top navigation bar
def get_topnav():
    topnav = [{ 'title':    'Data Analysis',
                'id':       'analysis',
                'url':      '',
                'sub_menu': [{ 'title': 'Average Subtracted Images',
                               'id':    'analysis_avg_sub_images',
                               'url':   '/analysis/avg_sub_images'},
                            ]
              }]

    return topnav

# mandatory function for specifying the style of menu in top navigation bar 
def get_topnav_style():
    topnav_style = """
    body.analysis_avg_sub_images    #topnav li.analysis_avg_sub_images,
    body.analysis_avg_sub_images    #topnav #analysis_avg_sub_images a {
        color:#0C6DFF !important;
        font-weight: bold;
    }
    
    """

    return topnav_style

# mandatory function for highlighting present view in top navigation bar 
def get_topnav_highlight(view_id):
    topnav_highlight = {}
    menus = get_topnav()
    for menu in menus:
        for sub_menu in menu['sub_menu']:
            if sub_menu['id'] == view_id:
                topnav_highlight['app_title']  = menu['title']
                topnav_highlight['app_id']     = menu['id']
                topnav_highlight['view_title'] = sub_menu['title']
                topnav_highlight['view_id']    = sub_menu['id']
                
    return topnav_highlight
