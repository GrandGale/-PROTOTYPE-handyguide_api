from typing import List, Tuple
from django.db.models.query import QuerySet

from handouts.filters import BaseHandoutFilter
from handouts.models import Course, Department, Faculty, Handout


def handouts_list(*, filters=None) -> QuerySet[Handout]:
    """
    Get a filtered list of handouts.

    This function returns a filtered queryset of Handout objects based on the provided filters.

    Args:
        filters (dict, optional): A dictionary of filters to apply on the Handout queryset.
                                  Defaults to None.

    Returns:
        QuerySet[Handout]: A filtered queryset of Handout objects.
    """
    filters = filters or {}
    qs = Handout.objects.all()
    return BaseHandoutFilter(filters, qs).qs


def get_faculty_department_course_list() -> (
    Tuple[List[Faculty], List[Department], List[Course]]
):
    """
    Get lists of all faculties, departments, and courses.

    This function retrieves all Faculty, Department, and Course objects and returns them as lists.

    Returns:
        Tuple[List[Faculty], List[Department], List[Course]]: A tuple containing lists of all faculties,
                                                             departments, and courses.
    """
    faculties = Faculty.objects.all()
    departments = Department.objects.all()
    courses = Course.objects.all()
    return faculties, departments, courses
