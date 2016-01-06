from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^vy/myfirst', views.current_datetime),
    url(r'^hi', views.hi),

    url(r'^custinfo', views.getCustomerInfo),
    url(r'^createLead', views.createLead),
    url(r'^provisionUser', views.provisionUser),

    url(r'^dummy', TemplateView.as_view(template_name="myDummyOne.html")),
    url(r'^second', TemplateView.as_view(template_name="secondPage.html")),
    url(r'^test_esb', TemplateView.as_view(template_name="test_esb.html")),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^cap_load', views.myCaptchaLoader),
    url(r'^studentList', views.getStudentList),
)
