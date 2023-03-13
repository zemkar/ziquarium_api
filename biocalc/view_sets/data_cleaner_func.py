
import os
from django.contrib.auth.models import User
from django.utils import timezone


def data_cleaner(request_data, item_category, action_creator_id=None, instance=None):
    """
    
    Auto fill:
    * user_placeholder - when item created, can be changed only by admin
    * latest_editor - when item updated, can be changed only by admin
    * approving_user & approved_at -  if item is approved by admin

    Remove approved status when item updated.
    Remove all empty fields.
    """
    cleared_data = {}
    user = User.objects.filter(pk=action_creator_id)[0]
       
    for field in request_data: # filter for empty fields
        if request_data[field] != '':
            cleared_data[field] = request_data[field]
 
    
    cleared_data["type_category"] = item_category

    if instance: # if update
        cleared_data['latest_editor'] = str(action_creator_id)
        if "user_placeholder" in cleared_data: 
            cleared_data.pop("user_placeholder")
        if "image" in cleared_data:
            print("got image")
            try:
                print("image:", instance.image, instance.image.path)
                if os.path.isfile(instance.image.path):
                    print("del old image")
                    os.remove(instance.image.path)
            except:
                pass
        else: print("no image")
    else:       # if creation
        cleared_data['user_placeholder'] = str(action_creator_id)

    if 'gallery' in request_data: # if gallery contain less then 2 items store it in the list
        if type( request_data['gallery'] ) == type(" "):
            cleared_data['gallery'] = [request_data['gallery'],]

    if user.is_superuser:
        if 'latest_editor' in request_data and request_data['latest_editor'] != '':
            cleared_data['latest_editor'] = request_data['latest_editor']
            if 'edited_at' in request_data and request_data['edited_at'] != '': 
                cleared_data['edited_at'] = request_data['edited_at']
        if 'user_placeholder' in request_data and request_data['user_placeholder'] != '':
            cleared_data['user_placeholder'] = request_data['user_placeholder']
            if 'created_at' in request_data and request_data['created_at'] != '': 
                cleared_data['created_at'] = request_data['created_at']

        if user and 'approved' in request_data: # store time if item approved by editor
            if request_data['approved'] and not instance:
                # if item created
                cleared_data['approved_at'] = timezone.now()
                cleared_data['approving_user'] = str(action_creator_id)
            elif request_data['approved'] and instance and request_data['approved'] != instance.approved:
                # if item modified and approved changed to true
                cleared_data['approved_at'] = timezone.now()
                cleared_data['approving_user'] = str(action_creator_id)
    else: 
        cleared_data['approved'] = False
        cleared_data['approving_user'] = None

        
# @receiver(pre_save, sender=Fish)
# def check_fish_image_to_delete(sender, instance, **kwargs):
    
#     if not instance.pk:
#         print("new instance")
#         return False
#     else:
#         try:
#             old_image = Fish.objects.get(pk=instance.pk).image
            
#             print("have old image", old_image)
#             new_image = instance.image
#             if not old_image == new_image:
#                 print("new image != old image ", new_image, old_image)
#                 if os.path.isfile(old_image.path):
#                     print("del old image")
#                     os.remove(old_image.path)

#         except Fish.DoesNotExist:
#             return False

    return cleared_data
            