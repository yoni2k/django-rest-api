from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profile """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to edit their own profile """
        if request.method in permissions.SAFE_METHODS: #allow users see other users info (read / safe HTTP Method), but not change
            return True

        #return if what they are updaing is their own id (authenticated user by Django framework)
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """ Allow users to update their own status """

    def has_object_permission(self, request, view, obj):
        """ Check user is styring to edit their own status """
        if request.method in permissions.SAFE_METHODS: #allow users see other users info (read / safe HTTP Method), but not change
            return True

        #return if what they are updaing feed with their own id as the foreign key
        return obj.user_profile.id == request.user.id
