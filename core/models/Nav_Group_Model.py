from django.db import models

class NavGroupModel(models.Model):
    name = models.CharField(max_length=100, help_text="Dropdown title (if this is a group)")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name