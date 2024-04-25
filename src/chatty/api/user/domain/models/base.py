from django.db import models


class BaseModel(models.Model):

    id = models.UUIDField(max_length=34, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ["created_at"]
