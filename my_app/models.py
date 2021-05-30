from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)

    #change the model name in admin panel
    class Meta:
        verbose_name_plural = 'Searches'

    def __str__(self):
        return self.search

class Contact(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    subject = models.CharField(max_length=500, null=True, blank=True)
    desc = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username