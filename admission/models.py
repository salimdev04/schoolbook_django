from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from student.models import Adresse, Baccalaureat, Info_personnel, Student_file
from campus.models import Campus


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.campus.title


class Admission(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_infos = models.ForeignKey(Info_personnel, on_delete=models.CASCADE)
    student_adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    student_bac = models.ForeignKey(Baccalaureat, on_delete=models.CASCADE)
    student_file = models.ForeignKey(Student_file, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.campus.title}'


class Stream(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    admission = models.ForeignKey(Admission, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.admission

    def send_admission(sender, instance, *args, **kwargs):
        admission = instance
        student = admission.user
        campus = admission.campus
        stream = Stream(admission=admission, student=student,
                        created_at=admission.created_at, campus=campus)
        stream.save()


# Stream
post_save.connect(Stream.send_admission, sender=Admission)
