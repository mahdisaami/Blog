from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from content.models import Post
from lib.common_modesl import BaseModel

User = get_user_model()


class Like(BaseModel):
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_('post'), related_name='likes', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        db_table = 'like'

    def __str__(self):
        return f'Post: {self.post.title}, User: {self.user.username}'


class Comment(BaseModel):
    text = models.TextField(_('text'))
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name=_('post'), related_name='comments', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comment'

    def __str__(self):
        return "User {} commented for Post {}".format(self.user.username, self.post.title)
