from django.conf.urls import patterns, include, url

from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myFirst.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^myfirst/', views.current_datetime),
    url(r'^sayhi/', views.say_hello),
    url(r'^student/', views.getStudent),
    url(r'^studentList/', views.getStudentList),
    url(r'^student_list/', views.get_student_list),
    url(r'^student_list_2/', views.get_student_list_2),
    url(r'^stud/', views.server),
)
