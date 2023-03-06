


from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from biocalc.models import AquaProfile
from biocalc.serializers import UserSerializer, UserProfileSerializer

# model crud
@permission_classes([IsAuthenticated])
class ProfileView(APIView):
    """
    This class handle the RUD operations for UserProfile
    """
    def get(self, request):
        """
        Handle GET requests to return UserProfile object
        """
        try:
            print("User in list:", self.request.user, " super?", self.request.user.is_superuser)
            user = User.objects.get(pk=request.user.id)
            profile = AquaProfile.objects.get(user=request.user)
            user_data = UserSerializer(user).data
            profile_data = UserProfileSerializer(profile).data 
            user_data.update(profile_data)
            return Response( user_data )
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request):
        """
        Handle PUT requests to update a Profile
        """
        modified = {}
        try:
            mod_user_data = {
                "first_name" : request.data.get('first_name'), 
                "last_name" : request.data.get('last_name')
                }    # data from client
            user = User.objects.get(pk=request.user.id)     # user as object
            user_data = UserSerializer(user).data           # user as dict
            user_serializer = UserSerializer(user, data=mod_user_data, partial=True)      # modified serializer
            
            for field in mod_user_data.keys():
                if user_data[field] != mod_user_data[field]:
                    if user_serializer.is_valid():
                        user_serializer.save()
                        modified.update({"user":True})
                        break
                    else:
                        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            mod_user_profile = {
                "bio" : request.data.get('bio'), 
                "location" : request.data.get('location'), 
                "birth_date" : request.data.get('birth_date')
                }
            profile = AquaProfile.objects.get(user=request.user)
            profile_data = UserProfileSerializer(profile).data 
            profile_serializer = UserProfileSerializer(profile, data=mod_user_profile, partial=True)
            for field in mod_user_profile.keys():
                if profile_data[field] != mod_user_profile[field]:
                    if profile_serializer.is_valid():
                        profile_serializer.save()
                        modified.update({"profile":True})
                        break
                    else:
                        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            if "user" in modified.keys() and "profile" in modified.keys():
                print("USER_PROFILE_VIEW \n user and profile modified\n", user_serializer.data, "\n", profile_serializer.data)
                user_data = user_serializer.data
                profile_data = profile_serializer.data
                user_data.update(profile_data)
                return Response(user_data)

            elif "user" in modified.keys():
                print("USER_PROFILE_VIEW \n only user modified\n", user_serializer.data)
                user_data = user_serializer.data
                user_data.update(profile_data)
                return Response(user_data)

            elif  "profile" in modified.keys():
                print("USER_PROFILE_VIEW \n only profile modified\n", profile_serializer.data)
                profile_data = profile_serializer.data
                profile_data.update(user_data)
                return Response(profile_data)

            return Response(status=status.HTTP_304_NOT_MODIFIED )
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        """
        Handle DELETE requests to delete a Profile
        """
        try:
            user = User.objects.get(pk=request.user.id)
            print("USER_PROFILE_VIEW \n user to del:", user)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
