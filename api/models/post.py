from django.db import models
from api.models.user import User

class Post(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(default="", max_length=200)
    description = models.CharField(default="", max_length=200)
    keyword = models.CharField(default="", max_length=200)
    content = models.CharField(default="", max_length=13)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    _created = models.DateTimeField(auto_now_add=True)
    _updated = models.DateTimeField(auto_now=True)

    @property
    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        return super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'post'
        app_label = 'api'
