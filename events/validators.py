
#This function is created to validate types of files that user is going to upload
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.mp4', '.mkv']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
    