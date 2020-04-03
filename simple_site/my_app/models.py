'''
doc string for the model
'''
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    '''
    Customer Model Class
    '''
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264)
    address = models.CharField(max_length=264)
    cc_number = models.CharField(max_length=264)
    def __str__(self):
        '''
        print firstname and lastname
        '''
        return '{} {}'.format(self.first_name, self.last_name)

class UserProfileInfo(models.Model):
    '''
    add additional info to user
    '''
    user = models.OneToOneField(User)
    #Additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return self.user.username