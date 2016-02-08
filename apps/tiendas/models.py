from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Zona(models.Model):
    nombre = models.CharField(max_length=128,unique=True)
    localizacion = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(default=0)

    def save(self, *args, **kwargs):
    	self.slug = slugify(self.nombre)
    	super(Zona, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre

class Tienda(models.Model):
    nombre = models.CharField(max_length=128,unique=True)
    calle = models.CharField(max_length=128,unique=True)
    zona = models.ForeignKey(Zona,null=True)
    imagen = models.ImageField(upload_to='tmp/', blank=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Tienda, self).save(*args, **kwargs)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.nombre

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username