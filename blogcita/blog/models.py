from django.db import models
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    # objects = None
    Title       = models.CharField(max_length=200)
    Body        = models.TextField()
    Category    = models.CharField(max_length=200)
    Published   = models.DateTimeField(auto_now_add=True)
    Update      = models.DateTimeField(auto_now=True)
    Slug        = models.SlugField(editable=False, blank=True, unique=True)

    def save(self):
        if self._state.adding:
            self._generate_slug()
        super(Post, self).save()

    def _generate_slug(self):
        if self.Slug:
            slug_candidate = slug_original = self.Slug
        else:
            # To Generate New Slug If None, You can change
            slug_candidate = slug_original = slugify(self.Title, allow_unicode=True)
            if not slug_candidate:
                slug_candidate = slug_original = lambda: random.randint(1, 10000000)

        self.Slug = slug_candidate

    # def save(self):
      #  self.slug = slugify(self.Title)
       # super(Post, self).save()

    def __str__(self):
        return "{}.{}".format(self.id, self.Title)