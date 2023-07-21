from django.contrib import admin
from parrot_control import models as website_models


admin.site.register(website_models.ParrotCommand)

admin.site.register(website_models.CommandConfig)

admin.site.register(website_models.CommandCategory)

class BlueParrotCommandAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(BlueParrotCommandAdmin, self).get_queryset(request)
        return qs.filter(parrot_1=True)

class RedParrotCommandAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(RedParrotCommandAdmin, self).get_queryset(request)
        return qs.filter(parrot_0=True)

admin.site.register(website_models.BlueParrotCommand, BlueParrotCommandAdmin)
admin.site.register(website_models.RedParrotCommand, RedParrotCommandAdmin)
