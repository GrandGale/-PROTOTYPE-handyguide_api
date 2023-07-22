from django.db.models.query import QuerySet

from handouts.filters import BaseHandoutFilter
from handouts.models import Handout


def handouts_list(*, filters=None) -> QuerySet[Handout]:
    filters = filters or {}
    qs = Handout.objects.all()
    return BaseHandoutFilter(filters, qs).qs
