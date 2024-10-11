from django.contrib.auth.models import AbstractUser
from django.db import models
import os
import uuid


def get_avatar_filename(instance, filename):
    # imagen3121212      .png            imagen3121212.png
    base_filename, file_extension = os.path.splitext(filename)
    # user_1_avatar.png
    new_filename = f"user_{instance.id}_avatar{file_extension}"
    # user/avatar/user_1_avatar.png
    return os.path.join('user/avatar/', new_filename)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(max_length=30, blank=True)
    avatar = models.ImageField(
        upload_to=get_avatar_filename, default='user/default/avatar_default.jpg')
    
    @property
    def is_collaborator(self):
        return self.groups.filter(name='Collaborators').exists()

    @property
    def is_registered(self):
        return self.groups.filter(name='Registered').exists()

    @property
    def is_admin(self):
        return self.groups.filter(name='Admins').exists()
