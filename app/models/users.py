from time import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.utils import timezone



NEW, CODE_VERIFIED, DONE = ('new','code_verified','done')


class User(AbstractUser):
    status_choices = (
        (NEW, NEW),
        (CODE_VERIFIED, CODE_VERIFIED),
        (DONE, DONE)
    )
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choices, default=NEW)
    image = models.ImageField(upload_to="user_images/", validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])], null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.username

class UserConfirmation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="confirmations")
    code = models.PositiveIntegerField()
    expire_time = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        expire_time = timezone.now()+timezone.timedelta(minutes=10)
        return super().save(*args, **kwargs)

    def is_expired(self):
        if self.expire_time > timezone.now():
            return False
        return True
    def __str__(self):
        return f"{self.user.username} | {self.code}"



