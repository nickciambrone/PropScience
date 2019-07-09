# from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify
# from accounts.models import User


from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()



class Group(models.Model):
    address = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    bed = models.IntegerField()
    bath = models.IntegerField()
    amenities = models.CharField(max_length=255)
    price = models.IntegerField()
    members = models.ManyToManyField(User,through="GroupMember")

    def __str__(self):
        return self.address

    def save(self, *args, **kwargs):
        self.slug = slugify(self.address)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:single", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["address"]

# def get_image_filename(instance, filename):
#     title = instance.post.title
#     slug = slugify(title)
#     return "post_images/%s-%s" % (slug, filename)
#
#
# class Images(models.Model):
#     group = models.ForeignKey(Group, default=None, on_delete='cascade')
#     image = models.ImageField(upload_to='housepics',
#                               verbose_name='Image')

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships", on_delete='cascade')
    user = models.ForeignKey(User,related_name='user_groups', on_delete='cascade')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")
