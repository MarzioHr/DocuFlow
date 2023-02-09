from django.db import models
import uuid
from django.contrib.auth.models import User, AbstractUser, Group, Permission

# Create your models here.
class User(AbstractUser):
    '''
    Add roles to the native Django User Model.
    '''
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, null=True, blank=True, related_name='home_user_groups')
    user_permissions = models.ManyToManyField(Permission, null=True, blank=True, related_name='home_user_permissions')

class BusinessUnit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=200, null=False, blank=False)

class Documentation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    heading = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    tags = models.ManyToManyField(Tag, null=True, blank=True, related_name='documentations')
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='documentations')
    business_unit = models.ManyToManyField(BusinessUnit, null=True, blank=True, related_name='documentations')