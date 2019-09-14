from django.db.models import Q
from rest_framework import generics, pagination

from reports.models import Report
from .serializers import ReportSerializer, AuthorSerializer


class ReportListView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ReportSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        pagination_limit = self.request.query_params.get('pagination_limit', None)
        pagination_offset = self.request.query_params.get('pagination_offset', None)

        print(pagination_limit, pagination_offset, user_id)

        queryset = Report.objects.all()

        if user_id is not None:
            queryset = queryset.filter(
                Q(author=user_id) |
                Q(supervisors=user_id) |
                Q(responses__author=user_id)
            ).distinct()

        if pagination_offset is not None:
            queryset = queryset.all()[pagination_offset:]

        if pagination_limit is not None:
            queryset = queryset.all()[:pagination_limit]

        return queryset
