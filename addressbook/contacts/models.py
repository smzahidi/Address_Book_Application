from django.db import models

# Create your models here.

class Contacts(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    streetAddress = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.firstName + " " + self.lastName