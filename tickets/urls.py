#from django.conf.urls.defaults import url
from django.urls import include, path
from .api import TicketsList, TicketsDetail

urlpatterns = [
path('programmers/$', views.TicketsList.as_view()),
path('r'^'programmers/(?P<pk>[0-9]+)/$', views.TicketsDetail.as_view()),
path('r'^'ckeditor/', include('ckeditor_uploader.urls')),
]