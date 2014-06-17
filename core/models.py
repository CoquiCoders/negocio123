from django.db import models
from django.utils.encoding import iri_to_uri

# Create your models here.
class Agency(models.Model):
  class Meta:
    verbose_name_plural = 'Agencies'

  def __unicode__(self):
      return self.full_name

  full_name = models.CharField(max_length=50)
  short_name = models.CharField(max_length=12)
  slug = models.SlugField(max_length=50)

  def save(self, *args, **kwargs):
    self.slug = iri_to_uri('-'.join([x.lower() for x in self.full_name.split(' ')]))
    super(Agency, self).save(*args, **kwargs)