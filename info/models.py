from django.db import models
from sorl.thumbnail import ImageField


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField('date published')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return str(self.name)


class Image(models.Model):
    date_created = models.DateTimeField('date published')
    gallery = models.ForeignKey(Gallery, null=True, related_name='images')
    path = ImageField(upload_to='info/')

    def __unicode__(self):
        return self.path

    def __str__(self):
        return str(self.path)


class Project(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField(default='')
    gallery = models.ForeignKey(Gallery, null=True)
    cover_image = models.ForeignKey(Image, null=True, blank=True)
    date_created = models.DateTimeField('date published')

    def __str__(self):
        return str(self.title)
