import uuid

from django.db import models
from django.utils import timezone

TSUN_CATEGORY_CHOICES=(
        ('RE','永久保存'),
        ('DAC','終わったら消す'),
        ('DIT','今日中に消す'),
    )

TSUN_TYPE_CHOICES=(
    ('W','Web'),
    ('PD','PDF'),
    ('Pa','Paper')
)


class User(models.Model):
    """本モデル"""

    class Meta:
        db_table = 'user'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='ユーザー名', max_length=20)
    password = models.CharField(max_length=20,verbose_name='パスワード', null=True, blank=True)

class TsunList(models.Model):
    """本モデル"""

    class Meta:
        db_table = 'tsun'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    UserId = models.IntegerField(editable=False)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20,choices=TSUN_CATEGORY_CHOICES)
    tsuntype = models.CharField(max_length=20,choices=TSUN_TYPE_CHOICES)
    link = models.CharField(max_length=500)
    memo = models.CharField(max_length=200)
    exp = models.IntegerField(max_length=10000)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.title

