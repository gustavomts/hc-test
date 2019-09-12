from .views import ReportListView
from django.conf.urls import url

urlpatterns = [
    url(r'^$', ReportListView.as_view(), name='report-rud'),
]
