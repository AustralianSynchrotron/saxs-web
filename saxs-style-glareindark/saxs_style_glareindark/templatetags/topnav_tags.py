from django.conf import settings
from django.template import Library, Node

register = Library()

class topnav_html(Node):
    def __init__(self):
        self.topnav_html = ""
    
    def render(self, context):
        
        installed_apps = getattr(settings, 'INSTALLED_APPS')
        for app in installed_apps:
            if app.find('_app_') >= 0:
                try:
                    exec "from %s.views import get_topnav" % app
                    menus = get_topnav()
                    for menu in menus:
                        if 'sub_menu' in menu:
                            classes = ["dir"]
                            for sub in menu['sub_menu']:
                                classes.append(sub['id'])
                            self.topnav_html += '<li class="%s">%s' % (" ".join(classes), menu['title'])
                            self.topnav_html += '<span></span><ul>'
                            for sub in menu['sub_menu']:
                                self.topnav_html += '<li id="%s"><a href="%s">%s</a></li>' % (sub['id'], sub['url'], sub['title'])
                            self.topnav_html += '</ul></li>'
                        else:
                            self.topnav_html += '<li class="%s"><a href="%s">%s</a></li>' % (menu['id'], menu['url'], menu['title'])
                except ImportError:
                    pass

        return self.topnav_html

def get_topnav_html(parser, token):
                
    return topnav_html()

register.tag('get_topnav_html', get_topnav_html)






class topnav_style(Node):
    def __init__(self):
        self.topnav_style = ""
    
    def render(self, context):
        
        installed_apps = getattr(settings, 'INSTALLED_APPS')
        for app in installed_apps:
            if app.find('_app_') >= 0:
                try:
                    exec "from %s.views import get_topnav_style as get_style" % app
                    self.topnav_style += get_style()
                    
                except ImportError:
                    pass

        return self.topnav_style

def get_topnav_style(parser, token):
                
    return topnav_style()

register.tag('get_topnav_style', get_topnav_style)