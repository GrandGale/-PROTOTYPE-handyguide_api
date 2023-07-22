import django_filters
from handouts.models import Handout


class BaseHandoutFilter(django_filters.FilterSet):
    course = django_filters.CharFilter(
        field_name="course__code", lookup_expr="icontains"
    )
    department = django_filters.CharFilter(
        field_name="department__abbrev", lookup_expr="iexact"
    )
    department = django_filters.CharFilter(
        field_name="faculty__abbrev", lookup_expr="iexact"
    )

    class Meta:
        model = Handout
        fields = ("course__code", "department", "faculty")
