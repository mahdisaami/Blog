from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.core.validators import FileExtensionValidator

from lib.common_modesl import BaseModel

User = get_user_model()


class Category(BaseModel):
    title = models.CharField(_('title'), max_length=32)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        db_table = 'category'

    def __str__(self):
        return self.title


class Tag(BaseModel):
    title = models.CharField(_("title"), max_length=32)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        db_table = 'tag'

    def __str__(self):
        return self.title


class Post(BaseModel):
    DRAFT = 0
    PUBLISHED = 1
    ARCHIVED = 2

    STATUS_CHOICES = (
        (DRAFT, _('draft')),
        (PUBLISHED, _('published')),
        (ARCHIVED, _('archived')),
    )

    title = models.CharField(_('title'), max_length=16)
    body = models.TextField(_('body'), blank=True)
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='posts', on_delete=models.CASCADE)
    status = models.PositiveSmallIntegerField(_('status'), choices=STATUS_CHOICES, default=0)
    categories = models.ManyToManyField(Category, verbose_name=_('categories'), related_name='posts')
    tags = models.ManyToManyField(Tag, verbose_name=_('tags'), related_name='posts', through="PostTag", blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'

    def __str__(self):
        return 'Title: ({}) User: ({})'.format(self.title, self.user.__str__())


class PostTag(BaseModel):
    tag = models.ForeignKey(Tag, verbose_name=_('tag'), related_name='posts_tag', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_('post'), related_name='post_tags', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'PostTag'
        verbose_name_plural = 'PostsTags'
        db_table = 'post_tag'

    def __str__(self):
        return f'Title: ({self.tag.title}) Post: ({self.post.title})'


class Media(BaseModel):
    PHOTO = 0
    VIDEO = 1

    MEDIA_CHOICES = (
        (PHOTO, 'photo'),
        (VIDEO, 'video')
    )

    post = models.ForeignKey(Post, verbose_name=_('post'), related_name='medias', on_delete=models.CASCADE)
    media_type = models.PositiveSmallIntegerField(_('media type'), choices=MEDIA_CHOICES, default=PHOTO)
    media_file = models.FileField(_('media file'),
                                  upload_to='content/media',
                                  validators=[FileExtensionValidator(
                                      allowed_extensions=('jpg', 'jpeg', 'mp4', 'wmv', 'flv', 'png'))])

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = "Medias"
        db_table = 'media'

    def __str__(self):
        return self.post.__str__()