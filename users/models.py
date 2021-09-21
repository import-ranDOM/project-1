from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#################### USER ACCOUNTS ######################
class userAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=300, blank=True)
    profile_pic = models.ImageField(upload_to="static/profile_pics", blank=True)
    friends = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

##########################################################


########################### BOOKS #############################
class book(models.Model):
    name = models.CharField(max_length=125)
    auther = models.CharField(max_length=125)
    mode = models.CharField(max_length=11, default="public")
    tag = models.CharField(max_length=75)
    book_cover = models.ImageField(upload_to="static/book_cover", blank=True)
    description = models.CharField(max_length=500, blank=True)
    user_account = models.ForeignKey(userAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

###############################################################
