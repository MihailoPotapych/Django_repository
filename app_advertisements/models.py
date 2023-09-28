from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=20)
    description = models.TextField('Описание', max_length=500)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            created_time = str(int(created_time[:2]) + 3) + created_time[2:]
            return format_html('<span style="color: green; '
                               'font-weight: bold">Сегодня в '
                               '{}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата изменения')
    def updated_date(self):
        if self.created_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:%S")
            updated_time = str(int(updated_time[:2]) + 3) + updated_time[2:]
            return format_html('<span style="color: gray; '
                               'font-weight: bold">Сегодня в '
                               '{}</span>', updated_time)
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    class Meta:
        db_table = 'advertisements'
    def __str__(self):
        return f'Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})'

# <Advertisement: Advertisement(id=1, title=Заголовок №1, price=100.00)>.