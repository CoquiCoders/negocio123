from django.db import models

# Create your models here.
class Agency(models.Model):
  class Meta:
    verbose_name_plural = 'Agencies'

  def __unicode__(self):
      return self.full_name

  full_name = models.CharField(max_length=50)
  short_name = models.CharField(max_length=12)