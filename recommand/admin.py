from django.contrib import admin
from recommand.models import raw_course
from recommand.models import course
from recommand.models import user_detail
from recommand.models import user_course
from recommand.models import course_score

class courseAdmin(admin.ModelAdmin):
    list_display = ('id','c_name', 'c_teacher')

class raw_courseAdmin(admin.ModelAdmin):
    list_display = ('id','rc_subjectid', 'rc_name', 'rc_teacher','rc_department' ,'rc_semester', 'rc_credit','c_id')

class course_score_admin(admin.ModelAdmin):
    list_display = ('u_id', 'c_id', 'cs_score', 'cs_comment', 'cs_createon')

class user_course_admin(admin.ModelAdmin):
    list_display = ('u_id', 'c_id', 'uc_grade')
# Register your models here.
admin.site.register(raw_course,raw_courseAdmin)
admin.site.register(course,courseAdmin)
admin.site.register(user_detail)
admin.site.register(user_course, user_course_admin)
admin.site.register(course_score, course_score_admin)

