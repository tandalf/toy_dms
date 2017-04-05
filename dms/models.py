# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Document(models.Model):
    DOC_STATES = (
        ("NEW", "New"),
        ("ASSIGNED", "Assigned"),
        ("INPROG", "In Progress"),
        ("DONE", "Done"),
    )
    assigner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_docs')
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned_docs')
    status = models.CharField(max_length=50, choices=DOC_STATES)
    document = models.FileField(upload_to='docs/')
    description = models.TextField()