from django.contrib import admin
from .models import Advertisement

# Register your models here.


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'auction', 'created_date', 'updated_date', 'user', 'image_html']
    list_filter = ['auction', 'create_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общие', {
            'fields': ('title', 'description', 'user', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Доавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, AdvertisementAdmin)
