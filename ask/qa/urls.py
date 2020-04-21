from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.new_questions, name='new_questions'),
    url(r'popular/$', views.popular_questions, name='popular_questions'),
    url(r'question/(?P<id>\d+)/$', views.question, name='question'),
    # url(r'login/', views.test, name='test'),
    # url(r'signup/', views.test, name='test'),
    # url(r'ask/', views.test, name='test'),
]
