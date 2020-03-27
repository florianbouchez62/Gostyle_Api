from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Promotion


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'start_date', 'end_date', 'percentage', 'active')
    list_filter = ('start_date', 'end_date', 'active')
    readonly_fields = ["qrcode_image"]
    exclude = ('qrcode',)

    def get_fieldsets(self, request, obj=None) -> tuple:
        fieldsets = super(PromotionAdmin, self).get_fieldsets(request, obj)
        default_fieldsets = (
            (None, {
                'fields': ('name', 'description', 'start_date', 'end_date', 'percentage', 'image')
            }),
        )
        if not obj:
            default_fieldsets[0][1]['fields'] += ('active',)
        else:
            default_fieldsets[0][1]['fields'] += ('qrcode_image', 'active')
        fieldsets = default_fieldsets

        return fieldsets

    def delete_model(self, request, obj) -> None:
        obj.delete_medias()
        obj.delete()

    def delete_queryset(self, request, queryset) -> None:
        for obj in queryset:
            obj.delete_medias()
            obj.delete()

    def qrcode_image(self, obj):
        return mark_safe('<img src="/{}" width="200" height="200" />'.format(obj.qrcode))

    qrcode_image.allow_tags = True
    qrcode_image.__name__ = 'Qr code'
