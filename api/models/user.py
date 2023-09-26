from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(default="", max_length=200)
    email = models.CharField(default="", max_length=200)
    password = models.CharField(default="", max_length=200)
    phone_no = models.CharField(default="", max_length=13)
    salt = models.CharField(default="", max_length=16)

    _created = models.DateTimeField(auto_now_add=True)
    _updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'id' # Added this line

    @property
    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        return super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'user'
        app_label = 'api'
