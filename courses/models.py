from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from memberships.models import Membership

User = get_user_model()


def upload_location(instance, filename):
    return "%s/%s"%(instance.lesson.title, filename)


def course_upload_location(instance, filename):
    return "%s/%s"%(instance.title, filename)


class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(allow_unicode=True, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=2500)
    description = models.TextField(blank=True, null=True)

    active = models.BooleanField(default=True)
    full_payment = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    thumbnail = models.ImageField(upload_to=course_upload_location, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    allowed_memberships = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('title')

    def get_absolute_url(self):
        return reverse('courses:single_course', kwargs={'slug': self.slug})


class Lesson(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(allow_unicode=True, unique=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    @property
    def videos(self):
        return self.video_set.all().order_by('position')

    class Meta:
        unique_together = ('title', 'slug')

    def get_absolute_url(self):
        return reverse('courses:lesson-detail',
                       kwargs={
                           'course_slug': self.course.slug,
                           'lesson_slug': self.slug
                       })


class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    slug = models.SlugField(allow_unicode=True, unique=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to=upload_location, null=True)
    position = models.IntegerField()
    free = models.BooleanField(default=False)

    class Meta:
        unique_together = ('title', 'slug')

    def __str__(self):
        return self.title + ": " + str(self.video_file)
