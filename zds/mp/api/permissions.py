# -*- coding: utf-8 -*-

from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from zds.mp.models import PrivateTopic


class IsParticipant(permissions.BasePermission):
    """
    Custom permission to know if a member is a participant in a private topic.
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user in obj.participants.all()


class IsParticipantFromPrivatePost(permissions.BasePermission):
    """
    Custom permission to know if a member is a participant in a private topic from a private post.
    """

    def has_permission(self, request, view):
        private_topic = get_object_or_404(PrivateTopic, pk=view.kwargs.get('pk_ptopic'))
        return private_topic.author == request.user or request.user in private_topic.participants.all()


class IsAloneInPrivatePost(permissions.BasePermission):
    """
    Custom permission to know if a member is the only participant in a private topic.
    """

    def has_permission(self, request, view):
        private_topic = get_object_or_404(PrivateTopic, pk=view.kwargs.get('pk_ptopic'))
        return private_topic.participants.count() > 0


class IsLastPrivatePostOfCurrentUser(permissions.BasePermission):
    """
    Custom permission to know if it is the last private post in the private topic.
    """

    def has_object_permission(self, request, view, obj):
        private_topic = get_object_or_404(PrivateTopic, pk=view.kwargs.get('pk_ptopic'))
        return private_topic.last_message == obj and obj.author == request.user


class IsAuthor(permissions.BasePermission):
    """
    Custom permission to know if the user is the author of the private topic.
    """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
