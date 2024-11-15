from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    apply_link = models.URLField(blank=True, null=True)  # Optional apply link field
   # image = models.ImageField(upload_to='job_images/', blank=True, null=True)  # Optional image upload
   # document = models.FileField(upload_to='job_documents/', blank=True, null=True)  # Optional document upload

    def __str__(self):
        return self.title
