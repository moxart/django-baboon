from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
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
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('publish', 'Publish'),
    ]

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
        self.slug = slugify(self.title)
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
