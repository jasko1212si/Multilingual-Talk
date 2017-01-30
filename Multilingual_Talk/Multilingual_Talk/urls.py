from django.conf.urls import url
from django.contrib import admin
from chat import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chat-room', views.chatRoom, name='chatRoom'),
    url(r'^request-messages', views.requestMessages, name='requestMessages'),
    url(r'^error', views.error, name='error'),
    url(r'^match', views.match, name='match'),
    url(r'^', views.home, name='home'),
]
