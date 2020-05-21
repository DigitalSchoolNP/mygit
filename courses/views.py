from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View

from memberships.models import Membership, UserMembership
from .models import Video, Course, Lesson
from .forms import VideoForm


class CoursesListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


def all(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    template = 'courses/all.html'
    return render(request, template, context)


def single(request, slug):
    try:
        course = Course.objects.get(slug=slug)
        lesson = Lesson.objects.filter(course=course)
        video = Video.objects.filter(course=course)
        context = {'course': course, 'lesson': lesson, 'video': video}
        template = 'courses/single.html'
        return render(request, template, context)
    except:
        raise Http404


@login_required
def start_course(request, slug):
    try:
        course = Course.objects.get(slug=slug)
        user_membership = UserMembership.objects.filter(user=request.user).first()
        user_membership_type = user_membership.membership.membership_type
        course_allowed_mem_type = course.allowed_memberships.all()
        context = {'object': None}
        if course_allowed_mem_type.filter(membership_type=user_membership_type).exists():
            context = {'object': course}

        template = 'courses/start_course.html'
        return render(request, template, context)

    except:
        raise Http404
