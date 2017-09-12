from django.conf.urls import url
from django.conf.urls.static import static

from mail import views
from mail.views import CommentList

urlpatterns = [
    url(r'^home/$', views.send, name="home"),
    url(r'^display/$', CommentList.as_view()),
    url(r'^reply/$', views.reply, name="reply"),
]