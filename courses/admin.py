from django.contrib import admin
from .models import Video, Course, Lesson

# ds/ds


class CourseAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ['title', 'price', 'active', 'full_payment', 'updated']
    search_fields = ['title', 'description', 'price']
    list_editable = ['price', 'full_payment', 'active']
    readonly_fields = ['timestamp', 'updated']
    list_filter = ['price', 'active', 'full_payment']
    prepopulated_fields = {"slug": ("title", )}


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    search_fields = ['title', 'course']
    prepopulated_fields = {"slug": ("title", )}


class VideoAdmin(admin.ModelAdmin):
    list_display = ['course', 'title', 'lesson', 'position', 'free']
    search_fields = ['course', 'title', 'lesson', 'position', 'free']
    list_filter = ['course', 'title', 'lesson', 'position', 'free']
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Video, VideoAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
