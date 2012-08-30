#from saxs_model_analysis.models import Users
from saxs_model_analysis.models import Experiment
from saxs_model_analysis.models import Buffer
from saxs_model_analysis.models import SubtractedImage
from saxs_model_analysis.models import AverageImage
from saxs_model_analysis.models import AverageSubtractedImage
from saxs_model_analysis.models import DamVolume


from django.contrib import admin

#class UsersAdmin(admin.ModelAdmin):
#    list_display = ('id', 'first_name', 'last_name')
#    list_display_links = ['last_name']
#    search_fields = ['first_name', 'last_name']
#    
#admin.site.register(Users, UsersAdmin)

class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('id', 'epn', 'exp_name', 'user_fk')
    list_display_links = ['epn']
    list_filter = ['epn']
    search_fields = ['epn', 'exp_name']
    
admin.site.register(Experiment, ExperimentAdmin)

class BufferAdmin(admin.ModelAdmin):
    list_display = ('id', 'location')
    list_display_links = ['location']
    search_fields = ['location']
    
admin.site.register(Buffer, BufferAdmin)

class SubtractedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'avg_low_q', 'avg_high_q', 'valid')
    list_display_links = ['location']
    search_fields = ['location']
    
admin.site.register(SubtractedImage, SubtractedImageAdmin)

class AverageImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'location')
    list_display_links = ['location']
    search_fields = ['location']
    
admin.site.register(AverageImage, AverageImageAdmin)

class AverageSubtractedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'porod_volume', 'exp_fk')
    list_display_links = ['location']
    list_filter = ['exp_fk']
    search_fields = ['location', 'porod_volume', 'exp_fk']
    
admin.site.register(AverageSubtractedImage, AverageSubtractedImageAdmin)

class DamVolumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'dammif_pdb_file', 'dam_volume', 'avg_sub_image_fk')
    list_display_links = ['dammif_pdb_file']
    search_fields = ['dammif_pdb_file', 'dam_volume', 'avg_sub_image_fk']
    
admin.site.register(DamVolume, DamVolumeAdmin)
