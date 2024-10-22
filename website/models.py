from django.db import models

# Create your models here.
from .utils import generate_code


class Website(models.Model):
    site_url = models.URLField(max_length=200)
    code = models.CharField(max_length=10, blank=True)
    create_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.site_url
    

    def save(self, *args, **kwargs) -> None:
        if self.code is None or self.code == '':
            self.code = generate_code(self)
        return super().save(*args, **kwargs)