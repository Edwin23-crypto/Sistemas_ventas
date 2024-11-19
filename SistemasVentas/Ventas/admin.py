from django.contrib import admin
from .models import Cliente, Orden, Producto

# Register your models here.
#admin.site.register(Producto)
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_creacion',)

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'subtotal', 'iva', 'total', 'fecha_creacion')
    filter_horizontal = ('productos',)
    readonly_fields = ('subtotal', 'iva', 'total')

    # Calcular totales automáticamente
    def save_model(self, request, obj, form, change):
        obj.calcular_totales()
        super().save_model(request, obj, form, change)
