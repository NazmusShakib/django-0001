from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Company(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=100, null=True, blank=True)
    company_address = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ('company_name',)
