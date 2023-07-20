from django.contrib import admin

from handouts.models import (
    Faculty,
    Department,
    Session,
    UnderGradLevel,
    Course,
    Handout,
)


admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(UnderGradLevel)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Handout)
