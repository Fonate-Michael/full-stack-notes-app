from django.db import models

class NoteModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(upload_to = '/images')
    date_created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title


    






