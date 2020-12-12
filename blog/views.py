from django.views import generic
from django.views.generic import RedirectView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from dashboard.models import Post


# BLOG
class HomeView(generic.ListView):
    queryset = Post.objects.filter(status="publish").order_by('-published_at')
    template_name = 'blog/index.html'

