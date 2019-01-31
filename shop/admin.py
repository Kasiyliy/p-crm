from django.contrib import admin
from .models import Product, Category, Client, Order, OrderProduct


class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('category_name',)
    list_display = ['category_name','created_at']


class ClientAdmin(admin.ModelAdmin):
    list_per_page = 10

    search_fields = ('client_name',)
    list_display = ['client_name','created_at']


class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10

    search_fields = ('title','price','quantity',)
    list_display = ['title', 'quantity', 'price', 'category_name', 'created_at','status']


class OrderItemInline(admin.TabularInline):
    model = OrderProduct

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":

            kwargs["queryset"] = Product.objects.filter(status=True).all()


        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class OrderAdmin(admin.ModelAdmin):
    list_per_page = 10
    exclude = ('vendor',)
    search_fields = ('status',)
    list_display = ['client', 'vendor', 'created_at', 'get_total_cost', 'status']
    inlines = [OrderItemInline]

    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.groups.filter(name='Супервайзер').exists():
            return qs

        return qs.filter(vendor=request.user)

    def save_model(self, request, obj, form, change):
        if obj.id is None:
            obj.vendor = request.user
        super().save_model(request, obj, form, change)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

