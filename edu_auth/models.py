from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    type = models.SlugField(unique=True,max_length=50)
    is_hide = models.BooleanField(default= False)
    categgory_image = models.ImageField(_('Category Image'), upload_to='category-images', null=True, blank=True,default="placeholders/placeholder.jpg")
    created_at = models.DateTimeField(_('Created Joined'), auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

   