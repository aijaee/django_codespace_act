from django.db import models
from django.conf import settings


class Theme(models.Model):
    theme_choices = (
        ('light', 'light'),
        ('dark', 'dark'),
        ('system', 'system'),
    )
    mode = models.CharField(
        max_length=50,
        choices=theme_choices,
        default='light',
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        default_permissions = []

    def __str__(self):
        return self.mode
