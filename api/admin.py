from django.contrib import admin
from .models import CustomUser
from .models import StudentModel,SubjectModel, TeacherModel
# Register your models here.

# Now register the new UserAdmin...
admin.site.register(CustomUser)

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email','phone_no','roll','city']
    

@admin.register(TeacherModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','email','phone_no','experience','city']
    
@admin.register(SubjectModel)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['sub','score','grade']