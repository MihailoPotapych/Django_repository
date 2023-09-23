from django.db import models

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=20)
    description = models.TextField('Описание', max_length=500)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если уместен торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'advertisements'
    def __str__(self):
        return f'Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})'

# <Advertisement: Advertisement(id=1, title=Заголовок №1, price=100.00)>.