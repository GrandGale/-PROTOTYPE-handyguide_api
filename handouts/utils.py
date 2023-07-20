def get_handout_upload_path(instance, filename):
    # Use the instance's attributes to construct the upload path dynamically
    return f"handouts/{instance.session.name.replace('/', '_')}/{instance.faculty.abbrev}/{instance.department.abbrev}/{instance.course.level.abbrev}/{instance.course.code}/{filename}"
