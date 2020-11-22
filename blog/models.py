from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Tag(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(
        max_length=200,
        editable=False,
        unique=True,
        null=True,
        default=''
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    POST_STATUS = [
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('publish', 'Publish'),
    ]

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(
        max_length=200,
        editable=False,
        unique=True,
        null=True,
        default=''
    )
    content = models.TextField()
    excerpt = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=POST_STATUS,
        default='publish'
    )
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']


class Category(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(
        max_length=200,
        editable=False,
        unique=True,
        null=True,
        default=''
    )
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['-published_at']


def _generate_unique_slug(instance):
    slug = slugify(instance.title)
    qs = Post.objects.filter(slug=slug).order_by('-id')

    if qs.exists():
        slug = '%s-%s' % (slug, qs.first().id)

    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        instance.slug = _generate_unique_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Post)
pre_save.connect(pre_save_post_receiver, sender=Category)
pre_save.connect(pre_save_post_receiver, sender=Tag)
