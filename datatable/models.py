from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])


class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.CharField(max_length=250, null=False)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(
        Category, null=False, related_name='post_category_rel', on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = "posts"
    
    def __str__(self):
        return self.title