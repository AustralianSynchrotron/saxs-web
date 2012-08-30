# Testing models example

from django.db import models
from django.contrib.auth.models import User

#class Users(models.Model):
#    first_name = models.CharField(max_length=40, blank=True)
#    last_name  = models.CharField(max_length=40, blank=True)
#    def __unicode__(self):
#        return "%s, %s" % (self.last_name, self.first_name)
#    class Meta:
#        db_table = 'users'
#        ordering=['last_name', 'first_name']

class Experiment(models.Model):
    epn      = models.IntegerField()
    exp_name = models.CharField(max_length=255, blank=True)
    user_fk  = models.ForeignKey(User, verbose_name="Owner")
    def __unicode__(self):
        return "%s - %s" % (self.epn, self.exp_name)
    class Meta:
        db_table = 'experiment'
        ordering=['epn', 'exp_name']
        
class Buffer(models.Model):
    location = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'buffer'
        
class SubtractedImage(models.Model):
    location   = models.CharField(max_length=255, blank=True)
    avg_low_q  = models.CharField(max_length=30, blank=True)
    avg_high_q = models.CharField(max_length=30, blank=True)
    valid      = models.BooleanField(default=False)
    class Meta:
        db_table = 'subtracted_image'
        
class AverageImage(models.Model):
    location = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'average_image'
        
class AverageSubtractedImage(models.Model):
    location     = models.CharField(max_length=255, blank=True)
    porod_volume = models.CharField(max_length=30, blank=True)
    exp_fk       = models.ForeignKey(Experiment, verbose_name="Experiment")
    def __unicode__(self):
        return "%s" % (self.location)
    class Meta:
        db_table = 'average_subtracted_image'
        
class DamVolume(models.Model):
    dammif_pdb_file   = models.CharField(max_length=255, blank=True)
    dam_volume        = models.CharField(max_length=30, blank=True)
    avg_sub_image_fk = models.ForeignKey(AverageSubtractedImage, verbose_name="Average Subtracted Image")
    class Meta:
        db_table = 'dam_volume'