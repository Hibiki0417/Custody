from django.db import models

from django.conf import settings

class Customer(models.Model):
    STATUS_CHOICES = [
        ("LEAD", "見込み"),
        ("ACTIVE", "取引中"),
        ("WON", "成約"),
        ("LOST", "失注"),
    ]

    name = models.CharField(max_length=100)                 # 顧客名
    company = models.CharField(max_length=100, blank=True)  # 会社名
    email = models.EmailField(blank=True, null=True)        # メール
    phone = models.CharField(max_length=20, blank=True)     # 電話番号
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="LEAD")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 登録者(ユーザー)
    note = models.TextField(blank=True)                     # 備考
    created_at = models.DateTimeField(auto_now_add=True)    # 作成日時
    updated_at = models.DateTimeField(auto_now=True)        # 更新日時
    is_active = models.BooleanField(default=True)           # 有効フラグ

    def __str__(self):
        return f"{self.name} ({self.company})" if self.company else self.name