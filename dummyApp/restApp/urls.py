
from django.conf.urls import url, include
from . import views
from rest_framework import routers
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'server', views.ServerView,base_name='server')

urlpatterns = [
    url(r'^serverTemplate/$', TemplateView.as_view(template_name="restApp/compute.html")),
]

urlpatterns += router.urls
