from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from .models import Product, SiteDetail, User


class UserAdmin(BaseUserAdmin):
    list_display = ("first_name", "last_name", "created_at")
    list_filter = list_display
    ordering = ("first_name", "last_name", "email")

    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (_("Personal Information"), {"fields": ("first_name", "last_name", "avatar")}),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("created_at", "updated_at", "last_login")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                ),
            },
        ),
    )

    readonly_fields = ("created_at", "updated_at")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at", "updated_at")
    list_filter = list_display

class SiteDetailAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        obj, created = self.model.objects.get_or_create()
        return HttpResponseRedirect(
            reverse(
                "admin:%s_%s_change"
                % (self.model._meta.app_label, self.model._meta.model_name),
                args=(obj.id,),
            )
        )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SiteDetail, SiteDetailAdmin)
