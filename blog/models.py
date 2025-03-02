from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)  # ব্লগের শিরোনাম
    content = models.TextField()  # ব্লগের বিস্তারিত লেখা
    created_at = models.DateTimeField(auto_now_add=True)  # কখন পোস্ট হয়েছে

    def __str__(self):
        return self.title