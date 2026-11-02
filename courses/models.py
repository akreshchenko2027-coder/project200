import os
from django.core.exceptions import ValidationError
from django.db import models
from users.models import User

def validate_file_extension_and_size(value):
    max_size_mb = 5
    if value.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Розмір файлу не повинен перевищувати {max_size_mb} МБ.")
    
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.zip', '.mp4', '.png', '.jpg']
    if ext.lower() not in valid_extensions:
        raise ValidationError(f"Недопустимий формат файлу. Дозволені: {', '.join(valid_extensions)}")

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=1)
    
    material_file = models.FileField(
        upload_to='lesson_materials/', 
        blank=True, 
        null=True, 
        validators=[validate_file_extension_and_size]
    )

    def __str__(self):
        return self.title