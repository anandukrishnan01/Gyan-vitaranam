from django.db import models
from django.core.validators import FileExtensionValidator
from PIL import Image
from io import BytesIO
# Create your models here.

class Student_Details(models.Model):
    Student_name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    Roll_no=models.IntegerField()
    def __str__(self):
        return self.Student_name
    
class Marklist(models.Model):
    studentdetails=models.ForeignKey(Student_Details,on_delete=models.CASCADE)
    Semester=models.CharField(max_length=100)
    Mark=models.CharField(max_length=100)


class ImageConverter(models.Model):
    image_file=models.ImageField(
        upload_to="image/",validators=[FileExtensionValidator(allowed_extensions=["jpg","png"])]
    )


    def save(self, *args, **kwargs):
        # Open the image using PIL
        pil_image = Image.open(self.image_file)

        # Convert the image to JPEG format
        pil_image = pil_image.convert('RGB')

        # Save the converted image to a BytesIO buffer
        buffer = BytesIO()
        pil_image.save(buffer, format='webp')

        # Save the buffer contents to the ImageField
        self.image_file.save(f'{self.image_file.name.split(".")[0]}.webp', buffer, save=False)

        super().save(*args, **kwargs)
    