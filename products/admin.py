from django.contrib import admin
from .models import product, productImage, Variation
# Register your models here.


class admin_custom(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ['title', 'price', 'active', 'updated']
    search_fields = ['title', 'description']
    list_filter = ['active', 'price']
    list_editable = ['price', 'active']
    readonly_fields = ['updated', 'created']
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = product


admin.site.register(product, admin_custom)
admin.site.register(productImage)
admin.site.register(Variation)
