from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    category = models.CharField(max_length=250)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author=models.CharField(max_length=300)
    slug=models.CharField(max_length=150)
    timestamp = models.DateField(blank=True, default=now)

    def __str__(self):
        return self.title +' by ' + self.author

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment=models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    parents = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] +' ... by    '+self.user.username

