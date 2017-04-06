from django.contrib.auth import get_user_model

from rest_framework import serializers

from dms.models import Document

"""
class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="user-detail", 
        lookup_field="id")

    class Meta:
        model = get_user_model()
        fields = ("username", "email")
"""

class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="document-detail",
        read_only=True)
    assigner = serializers.PrimaryKeyRelatedField(read_only=True)
    assignee = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all())

    class Meta:
        model = Document
        fields = ("url", "assigner", "assignee", "status", 
            "description", "document")