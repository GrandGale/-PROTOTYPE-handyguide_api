from django.db import models
from django.contrib.auth.models import User

from handouts.utils import get_handout_upload_path


class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    abbrev = models.CharField(max_length=10, unique=True, db_index=True)

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"
        ordering = ["name"]

    def __str__(self):
        return "Faculty of {} ({})".format(self.name, self.abbrev)


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    abbrev = models.CharField(max_length=10, unique=True)
    faculty = models.ForeignKey(
        Faculty, on_delete=models.PROTECT, related_name="departments"
    )

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["name"]

    def __str__(self):
        return "Department of {} ({})".format(self.name, self.abbrev)


class UnderGradLevel(models.Model):
    abbrev = models.CharField(max_length=10, unique=True, db_index=True)
    level = models.CharField(max_length=4, unique=True)

    class Meta:
        verbose_name = "Undergraduate Level"
        verbose_name_plural = "Undergraduate Levels"

    def __str__(self):
        return self.abbrev


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True, db_index=True)
    level = models.ForeignKey(UnderGradLevel, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["code"]

    def __str__(self):
        return "{} - {} ({})".format(self.code, self.name, self.level)


class Session(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Handout(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.PROTECT, related_name="handouts"
    )
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name="handouts"
    )
    faculty = models.ForeignKey(
        Faculty, on_delete=models.PROTECT, related_name="handouts"
    )
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_handout_upload_path)
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Handout"
        verbose_name_plural = "Handouts"

    def __str__(self):
        return "{} - {}".format(self.course, self.session)
