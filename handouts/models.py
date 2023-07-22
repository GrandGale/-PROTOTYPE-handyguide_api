from django.db import models
from django.contrib.auth.models import User

from handouts.utils import get_handout_upload_path


class Faculty(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Faculty", unique=True, db_index=True
    )
    abbrev = models.CharField(
        max_length=10, verbose_name="Abbreviation", unique=True, db_index=True
    )

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"

    def __str__(self) -> str:
        return "Faculty of {} ({})".format(self.name, self.abbrev)


class Department(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Department", unique=True, db_index=True
    )
    abbrev = models.CharField(max_length=10, verbose_name="Abbreviation", unique=True)
    faculty = models.ForeignKey(
        Faculty, on_delete=models.PROTECT, verbose_name="Faculty"
    )

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self) -> str:
        return "Department of {} ({})".format(self.name, self.abbrev)


class UnderGradLevel(models.Model):
    abbrev = models.CharField(max_length=10, unique=True, db_index=True)
    level = models.CharField(max_length=4, unique=True)

    class Meta:
        verbose_name = "UnderGraduate Level"
        verbose_name_plural = "UnderGraduate Levels"

    def __str__(self) -> str:
        return self.abbrev


class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True, db_index=True)
    level = models.ForeignKey(UnderGradLevel, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self) -> str:
        return "{} - {} ({})".format(self.code, self.name, self.level)


class Session(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.name


class Handout(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_handout_upload_path)
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Handout"
        verbose_name_plural = "Handouts"

    def __str__(self) -> str:
        return "{} - {}".format(self.course, self.session)
