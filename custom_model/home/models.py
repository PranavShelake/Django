from django.db import models

# Create your models here.







class student_manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_delete=False)


class Student(models.Model):
    name=models.CharField(default="not available",max_length=100)
    email=models.EmailField(default="not available")
    mark=models.IntegerField(default=0)

    is_delete=models.BooleanField(default=False)

    objects=student_manager()
    admin_manager= models.Manager()

    def __str__(self):
        return self.name