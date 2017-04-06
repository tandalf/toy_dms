from rest_framework import permissions

class IsAssignerOrAssignee(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, doc):
        return (doc.assigner == request.user) or \
            (doc.assignee == request.user)