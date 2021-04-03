from django.db import models
from django.contrib.auth import get_user_model 
from django.shortcuts import reverse

User = get_user_model()

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
                                "date published",
                                auto_now_add=True
                            )

    author = models.ForeignKey(
                                User,
                                models.CASCADE,
                                related_name="posts"
                            )

    group = models.ForeignKey(
                                'Group',
                                models.SET_NULL,
                                related_name="related_posts",
                                blank=True,
                                null = True
                            ) 

    def __str__(self):
        return self.text
    
class Group(models.Model):
    title = models.CharField(
                                "group name",
                                max_length=100,
                                db_index=True,
                             )
    
    slug = models.SlugField(max_length=100)

    discription = models.TextField(blank=True,db_index=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail_group_url')
