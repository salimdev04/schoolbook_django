from django.db import models
from django.urls.base import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
import uuid

# Create your models here.


class PublishManager(models.Manager):
    """
    To create my own queryset manager
    """

    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status='published')


def campus_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'campus_{0}/{1}'.format(instance.created_at, filename)


class Category(models.Model):
    pays = models.CharField(max_length=50)
    slug = models.SlugField(unique='pays')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("campus_per_pays", args=[self.id, self.slug])

    def __str__(self):
        return self.pays


class Speciality(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique='pays')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Level(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Campus(models.Model):

    objects = models.Manager  # the default manager
    published = PublishManager()  # our own manager

    TYPE = (
        ('private', 'Private'),
        ('public', 'Public'),
    )
    LANGUE = (
        ('english', 'English'),
        ('french', 'French')
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    tags = TaggableManager()

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='campus_admin')
    pays = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique_for_date="publish")
    type = models.CharField(choices=TYPE, max_length=8, default='Public')
    study_level = models.ForeignKey(Level, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    langue = models.CharField(choices=LANGUE, max_length=50, default='French')
    site_web = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    region = models.CharField(max_length=150)
    description = models.TextField()
    debut_inscription = models.DateField()
    fin_inscription = models.DateField()
    image = models.ImageField(upload_to=campus_directory_path, null=False)

    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES,
                              default='draft', max_length=10)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pub = self.publish
        return reverse('campus_detail', args=[pub.year, pub.month, pub.day, self.slug])


class Images(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(
        upload_to=campus_directory_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
