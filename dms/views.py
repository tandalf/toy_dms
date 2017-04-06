# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db.models import Q

from rest_framework import viewsets

from dms.serializers import DocumentSerializer
from dms.models import Document
from dms.permissions import IsAssignerOrAssignee

class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    permission_classes = (IsAssignerOrAssignee,)
    
    def get_queryset(self):
        user_pk = self.request.user.pk
        return Document.objects.filter(
            Q(assigner__pk=user_pk) | Q(assignee__pk=user_pk))

    def perform_create(self, serializer):
        return serializer.save(assigner=self.request.user)
