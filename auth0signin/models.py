from django.db import models

# Create your models here.
class TimeAuditModel(models.Model):
    """ To path when the record was created and last modified """
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created At",)
    updated = models.DateTimeField(auto_now=True, verbose_name="Last Modified At")

    class Meta:
        abstract = True

class Post(TimeAuditModel):
    post_title = models.CharField(max_length=255)
    post_description = models.TextField()
    post_description_markdown = models.TextField(blank=True)
    post_author = models.CharField(max_length=255)

    def __str__(self):
        return self.post_title