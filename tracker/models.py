from django.db import models
from django.utils import timezone

class DailyPlan(models.Model):
    # Tanlovlar (Choices)
    STATUS_CHOICES = [
        ('pending', '⏳ Kutilmoqda'),
        ('in_progress', '🔥 Jarayonda'),
        ('completed', '✅ Tugatildi'),
    ]
    
    DIFFICULTY_CHOICES = [
        ('easy', '🟢 Oson'),
        ('medium', '🟡 O\'rta'),
        ('hard', '🔴 Qiyin'),
    ]

    day_number = models.IntegerField(unique=True, verbose_name="Kun raqami")
    title = models.CharField(max_length=200, verbose_name="Mavzu")
    description = models.TextField(verbose_name="Batafsil tavsif")
    
    # Yangi maydonlar
    video_url = models.URLField(blank=True, null=True, verbose_name="Video Darslik Linki")
    resource_url = models.URLField(blank=True, null=True, verbose_name="Qo'shimcha Material")
    
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium', verbose_name="Qiyinlik")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Holat")
    
    # Statistika uchun
    time_spent = models.FloatField(default=0, verbose_name="Sarflangan soat")
    notes = models.TextField(blank=True, null=True, verbose_name="Kunlik xulosa")
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Kun {self.day_number}: {self.title}"

    class Meta:
        ordering = ['day_number']