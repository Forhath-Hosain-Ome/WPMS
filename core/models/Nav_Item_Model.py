from django.db import models
from .Nav_Group_Model import NavGroup

class NavItemModel(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    open_in_new_tab = models.BooleanField(default=False)
    group = models.ForeignKey(
        NavGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='items',
        help_text="Leave empty for top-level item"
    )

    def __str__(self):
        return self.name