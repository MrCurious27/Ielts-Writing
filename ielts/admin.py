from django.contrib import admin

# Register your models here.

from .models import (
			AnswerTaskOneAcademic,
			AnswerTaskOneGeneral,
			AnswerTaskTwo,
			CoachingClass,
			CommonTaskOneAcademic,
			CommonTaskOneGeneral,
			CommonTaskTwo,
			Faculty,
			Student,
		)

admin.site.register(CoachingClass)
admin.site.register(Faculty)
admin.site.register(Student)

class CommonTaskTwoAdmin(admin.ModelAdmin):
	list_display = ['uid', 'question', 'is_active']

admin.site.register(CommonTaskTwo, CommonTaskTwoAdmin)

class CommonTaskOneGeneralAdmin(admin.ModelAdmin):
	list_display = ['uid', 'question', 'is_active']

admin.site.register(CommonTaskOneGeneral, CommonTaskOneGeneralAdmin)

class CommonTaskOneAcademicAdmin(admin.ModelAdmin):
	list_display = ['uid', 'question', 'is_active']

admin.site.register(CommonTaskOneAcademic, CommonTaskOneAcademicAdmin)
