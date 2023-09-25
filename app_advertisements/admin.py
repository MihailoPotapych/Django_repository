from django.contrib import admin
from .models import Advertisement

# Register your models here.

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_at', 'auction']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_false', 'created_date']
    fieldsets = (
        ('Общее', {
            'fields': (
                'title',
                'description'
            )
        }),
        ('Финансы', {
            'fields': (
                'price',
                'auction'
            ),
            'classes': ['collapsed']
        })
    )

    @admin.action('Убрать возможность торга')
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)


admin.site.register(Advertisement, AdvertisementAdmin)
