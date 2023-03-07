from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    public_id = models.CharField(max_length=40, default=str(uuid4().hex))

class Profile(models.Model):

    public_id = models.CharField(max_length=40, default=str(uuid4().hex))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-created_at']
        verbose_name = 'user profile'
        verbose_name_plural = 'user profiles'
        db_table = 'UserProfiles'

    def __str__(self) -> str:
        
        return self.user.username
    
class UserLog(models.Model):

    public_id = models.CharField(max_length=40, default=str(uuid4().hex))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    log = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-created_at']
        verbose_name = 'user log'
        verbose_name_plural = 'user logs'
        db_table = 'UserLogs'

    def __str__(self) -> str:
        
        return self.log
    
class WorkSpace(models.Model):

    BASIC = 'basic'
    STANDARD = 'standard'
    PRO = 'pro'

    WORKSPACE_TIERS = (
        (BASIC, 'Basic'),
        (STANDARD, 'Standard'),
        (PRO, 'Pro'),
    )

    public_id = models.CharField(max_length=40, default=str(uuid4().hex))
    workspace_name = models.CharField(max_length=50)
    workspace_tier = models.CharField(max_length=50, choices=WORKSPACE_TIERS, default=BASIC)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(Profile)
    logs = models.ManyToManyField(UserLog)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['-created_at']
        verbose_name = 'workspace'
        verbose_name_plural = 'workspaces'
        db_table = 'Workspaces'

    def __str__(self) -> str:
        
        return self.workspace_name
