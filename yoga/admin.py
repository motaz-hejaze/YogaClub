from django.contrib import admin

# Register your models here.
from .models import Information,About,Classes,Instructors_Row,Email,Post,Test
#admin.site.register(Information)
admin.site.register(Test)
admin.site.register(Classes)
admin.site.register(Instructors_Row)
admin.site.register(Email)
admin.site.register(Post)

@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):

    # some code...

    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Information.objects.exists():
            retVal = False
        return retVal

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    # some code...

    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and About.objects.exists():
            retVal = False
        return retVal