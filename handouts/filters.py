import django_filters
from handouts.models import Handout


class BaseHandoutFilter(django_filters.FilterSet):
    # Define filters for course, department, and faculty using the 'iexact' lookup expression
    course_code = django_filters.CharFilter(field_name="course__code", lookup_expr="iexact")
    department = django_filters.CharFilter(
        field_name="department__abbrev", lookup_expr="iexact"
    )
    faculty = django_filters.CharFilter(
        field_name="faculty__abbrev", lookup_expr="iexact"
    )

    class Meta:
        model = Handout
        fields = {
            "course__code": ["exact"],
            "department__abbrev": ["exact"],
            "faculty__abbrev": ["exact"],
        }
