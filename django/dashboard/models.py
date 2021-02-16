from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from sorl.thumbnail import ImageField


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(
        max_length=200,
        editable=False,
        unique=True,
        null=True,
        default=''
    )
    description = models.CharField(max_length=200, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['-published_at']


class Tag(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(
        max_length=200,
        editable=False,
        unique=True,
        null=True,
        default=''
    )
    description = models.CharField(max_length=200, null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Tag, self).save()

    def __str__(self):
        return self.title


class Post(models.Model):
    POST_STATUS = [
        ('draft', 'پیش نویس'),
        ('pending', 'در انتظار'),
        ('publish', 'انتشار'),
    ]

    title = models.CharField(max_length=200, unique=True)
    en_title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        editable=False,
        null=True,
        default=''
    )
    content = models.TextField()
    excerpt = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    description = models.CharField(max_length=200, null=True, blank=True)
    image = ImageField(
        upload_to='images/%Y/%m/%d',
        max_length=255,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=POST_STATUS,
        default='publish'
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.en_title, allow_unicode=True)
        super(Post, self).save()

    class Meta:
        ordering = ['-published_at']


class Media(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = ImageField(
        upload_to='images/%Y/%m/%d',
        max_length=255,
        null=False,
        blank=False
    )
    uploaded_at = models.DateTimeField(auto_now=True)
