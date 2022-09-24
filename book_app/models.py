from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    is_reader = models.BooleanField('reviewer status', default=False)
    is_author = models.BooleanField('author status', default=False)

class Post_data(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=150)
    Review = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("single_post", kwargs={'pk': self.pk})

class Author_Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    mobile = models.CharField(default="Null", max_length=12)
    Work_Experience = models.CharField(default="Null",max_length=100)
    your_best_work = models.TextField(default="Null",max_length=250)


    def __str__(self):
        return f"{self.user.username} Profile"

class Reader_Profile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Reader_profile")
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    Name = models.CharField(default="Null", max_length=12)
    mobile = models.CharField(default="Null", max_length=12)
    Interest  = models.CharField(default="Null",max_length=100)
    Location = models.CharField(default="Null",max_length=250)


    def __str__(self):
        return f"{self.user.username} Profile"


class Comment(models.Model):
    post = models.ForeignKey('book_app.Post_data', related_name="comments",on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
