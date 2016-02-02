from django.db import models
from django.utils.translation import ugettext as _


class Channel(models.Model):
    name = models.CharField(
        max_length= 100,
        verbose_name=_("channel name"),
    )
    description = models.TextField(
        max_length = 300,
        verbose_name=_("channel description"),
        help_text=_("Description of what a channel contains"),
    )
    author = models.CharField(
        max_length=100,
        verbose_name=_("channel author"),
        help_text=_("Channel author can be a person or an organization"),
    )
    editors = models.ManyToManyField(
        'auth.User',
        verbose_name=_("editors"),
        help_text=_("Users with edit rights"),
    )

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")