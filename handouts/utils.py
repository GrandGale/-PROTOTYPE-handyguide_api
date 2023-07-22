from rest_framework import serializers


def get_handout_upload_path(instance, filename):
    # Use the instance's attributes to construct the upload path dynamically
    return f"handouts/{instance.session.name.replace('/', '_')}/{instance.faculty.abbrev}/{instance.department.abbrev}/{instance.course.level.abbrev}/{instance.course.code}/{filename}"


def create_serializer_class(name, fields):
    return type(name, (serializers.Serializer,), fields)


def inline_serializer(*, fields, data=None, **kwargs):
    serializer_class = create_serializer_class(name="inline_serializer", fields=fields)

    if data is not None:
        return serializer_class(data=data, **kwargs)

    return serializer_class(**kwargs)
