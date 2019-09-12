from rest_framework import serializers
from django.contrib.auth.models import User
from reports.models import Report, ReportResponse


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ReportResponseSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = ReportResponse
        fields = ('message', 'author')


class ReportSerializer(serializers.ModelSerializer):
    responses = ReportResponseSerializer(many=True)
    author = AuthorSerializer()
    supervisors = AuthorSerializer(many=True)

    class Meta:
        model = Report
        fields = '__all__'
