from django.contrib import admin

from martin.models.InputOutput import InputOutput


class ControlInputOutput(admin.ModelAdmin):
    list_display = (
        'datetime',
        'milk',
        'ad',
        'd3',
        'ld',
        'water',
        'excrement',
    )
    ordering = ('-datetime',)
    list_per_page = 10
    list_max_show_all = 200
    save_as = False
    list_display_links = ('datetime',)
    list_editable = ('milk',)


# Register your models here.
admin.site.register(InputOutput, ControlInputOutput)
