from django.db import models

# Create your models here.

class tbl_employee(models.Model):
    id=models.AutoField(primary_key=True,serialize=True)
    name=models.CharField(max_length=50,null=False)
    email=models.CharField(max_length=100,null=False)
    mobile=models.CharField(max_length=250,null=False)

    class Meta:
        db_table = 'tbl_employee'
        # managed = False
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
