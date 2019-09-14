from .views import UserListView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', UserListView.as_view(), name='users'),
]
