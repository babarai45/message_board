from django.contrib import admin
from .models import post_model


# first way to register model but not best approch 
# class postAdmin(admin.ModelAdmin):
#     list_display = ['author_name', 'psot_title', 'discriptions']

# admin.site.register(post_model, postAdmin)


#---------------------best approch or parctice 
# in this aproch we use admin decratore 
# Note :
# we did not use site method of admin
@admin.register(post_model)
class postAdmin(admin.ModelAdmin):
    list_display = ['id','author_name', 'psot_title', 'discriptions']
