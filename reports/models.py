# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Report(models.Model):
    class Meta:
        db_table = 'report'

    message = models.TextField()
    author = models.ForeignKey(User, related_name='report_author', on_delete=models.CASCADE)
    supervisors = models.ManyToManyField(User, related_name='supervisors')

    def __str__(self):
        return self.message


class ReportResponse(models.Model):
    class Meta:
        db_table = 'report_response'

    message = models.TextField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='response')
    author = models.ForeignKey(User, related_name='response_author', on_delete=models.CASCADE)

    def __str__(self):
        return self.message
