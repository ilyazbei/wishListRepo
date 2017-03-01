from __future__ import unicode_literals
from ..loginApp.models import User
from django.db import models
import re

class WishlistManager(models.Manager):

    def newItem(self, postData, userID):
        errors = []
        modelResponse = {}

        if len(postData['wish']) == 0 :
            errors.append('Item can not be empty!')
        if len(postData['wish']) < 3:
            errors.append('Item must be at least 3 charactor long!')

        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors

        # else (passed validations check)
        else:
            user = User.objects.get(id=userID)
            wish = Wishlist.objects.create(wish = postData['wish'], creator = user)
            user.wishlists.add(wish)

            modelResponse['status'] = True

        return modelResponse




# Create your models here.
class Wishlist(models.Model):
    wish = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name="wishlists")
    creator = models.ForeignKey(User, related_name = 'created_wishlists')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = WishlistManager()
