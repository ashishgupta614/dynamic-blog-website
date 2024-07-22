from django.db import models


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone=models.CharField(max_length=300)
    desc = models.CharField(max_length=3000)

    def __str__(self):
        return 'Query from ' + self.name + ' - ' + self.email