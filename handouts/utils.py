from rest_framework import serializers


def get_handout_upload_path(instance, filename):
    """
    Generate the upload path for Handout file.

    This function dynamically constructs the upload path for the Handout file based on the
    instance's attributes.

    Args:
        instance (Handout): The instance of the Handout model.
        filename (str): The original filename of the uploaded file.

    Returns:
        str: The generated upload path for the Handout file.
    """
    return f"handouts/{instance.session.name.replace('/', '_')}/{instance.faculty.abbrev}/{instance.department.abbrev}/{instance.course.level.abbrev}/{instance.course.code}/{filename}"


def create_serializer_class(name, fields):
    """
    Create a serializer class dynamically.

    This function creates a new serializer class with the specified name and fields.

    Args:
        name (str): The name of the serializer class.
        fields (dict): A dictionary of field names and their corresponding serializer fields.

    Returns:
        type: The dynamically created serializer class.
    """
    return type(name, (serializers.Serializer,), fields)


def inline_serializer(*, fields, data=None, **kwargs):
    """
    Create and instantiate an inline serializer.

    This function creates an inline serializer class with the specified fields and instantiates
    it with optional data and keyword arguments.

    Args:
        fields (dict): A dictionary of field names and their corresponding serializer fields.
        data (dict, optional): Data to be passed to the serializer for deserialization. Defaults to None.
        **kwargs: Additional keyword arguments to be passed to the serializer.

    Returns:
        Serializer: An instance of the inline serializer class.
    """
    serializer_class = create_serializer_class(name="inline_serializer", fields=fields)

    if data is not None:
        return serializer_class(data=data, **kwargs)

    return serializer_class(**kwargs)
