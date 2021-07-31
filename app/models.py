from datetime import datetime
from django.db import models
from django.urls import reverse
import geocoder

# token
mapbox_access_token = 'pk.eyJ1IjoiZXlhbnllaHlhIiwiYSI6ImNrcm5uem9kOTB5cW0yc252M3AxN2drNzMifQ.IIwBFoL3ox2l3rOwsvZe_w'


# Create your models here.
class Post(models.Model):
    # text = models.TextField(default='')
    # title = models.CharField(max_length=200, default='')
    username = models.TextField(max_length=200, default='')

    medicine = models.TextField(max_length=200, default='')
    expiry_date = models.DateField(default='2021-07-29')
    post_info = models.DateTimeField(default=datetime.now, blank=True)

    # MAPBOX STUFF
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng  # [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Post, self).save(*args, **kwargs)

    # author = models.ForeignKey(
    #     'auth.User',
    #     on_delete=models.CASCADE
    # )
    # first_name = models.CharField(max_length=200, default='')
    # body = models.TextField(default='')

    def __str__(self):
        return self.username

    # def get_absolute_url(self):
    #     return reverse('post_detail', args=[str(self.id)])
