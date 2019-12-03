from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    texto = RichTextUploadingField()
    autor = models.CharField(max_length=25)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo