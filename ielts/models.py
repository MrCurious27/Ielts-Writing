from django.contrib.auth.models import User
from django.db import models
# from TakeATest.models import Role

# Create your models here.
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%% Main User Tables %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class CoachingClass(models.Model):
	user_key 	= models.OneToOneField(User, on_delete = models.CASCADE)
	credit 		= models.IntegerField()
	is_active 	= models.BooleanField(default = True)

class Faculty(models.Model):
	user_key 			= models.OneToOneField(User, on_delete = models.CASCADE)
	faculty_uid 		= models.IntegerField()
	mobile_number 		= models.BigIntegerField()
	coaching_class_key 	= models.ForeignKey(CoachingClass, on_delete = models.CASCADE)
	is_active 			= models.BooleanField(default = True)

class Student(models.Model):
	user_key 	= models.OneToOneField(User, on_delete = models.CASCADE)
	student_uid	= models.IntegerField()
	mobile_number = models.BigIntegerField()
	faculty_key = models.ForeignKey(Faculty, on_delete = models.CASCADE)
	is_active 	= models.BooleanField(default = True)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%% Basic Question Model %%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class CommonTaskOneAcademic(models.Model):
	uid 		= models.IntegerField(unique = True, null = True)
	question 	= models.TextField(unique = True)
	photo 		= models.ImageField(upload_to = 'ielts/question/academic/', null = True)
	is_active 	= models.BooleanField(default = True)

class CommonTaskOneGeneral(models.Model):
	uid 		= models.IntegerField(unique = True, null = True)
	question 	= models.TextField(unique = True)
	is_active 	= models.BooleanField(default = True)

	def __str__(self):
		return self.question

class CommonTaskTwo(models.Model):
	uid 		= models.IntegerField(unique = True, null = True)
	question 	= models.TextField(unique = True)
	is_active 	= models.BooleanField(default = True)

	def __str__(self):
		return self.question

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%% Answer Model %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class AnswerTaskOneGeneral(models.Model):
	question 						= models.TextField()
	answer 							= models.TextField()
	word_count 						= models.PositiveSmallIntegerField()
	student_key 					= models.ForeignKey(Student, on_delete = models.CASCADE)
	is_checked 						= models.BooleanField(default = False)
	timestamp 						= models.DateTimeField(auto_now_add = True)
	checked_time 					= models.DateTimeField(null = True)
	task_achievement 				= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	task_achievement_remark 		= models.TextField(blank = True, null = True)
	coherence_and_cohension 		= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	coherence_and_cohension_remark 	= models.TextField(blank = True, null = True)
	lexical_resource 				= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	lexical_resource_remark 		= models.TextField(blank = True, null = True)
	grammer_range_accuracy 			= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	grammer_range_accuracy_remark 	= models.TextField(blank = True, null = True)
	overall_band 					= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)

	class Meta:
		ordering = ['timestamp']

class AnswerTaskOneAcademic(models.Model):
	question 						= models.TextField()
	answer 							= models.TextField()
	word_count 						= models.PositiveSmallIntegerField()
	photo 							= models.ImageField(upload_to = 'ielts/answer/academic/', null = True)
	student_key 					= models.ForeignKey(Student, on_delete = models.CASCADE)
	is_checked 						= models.BooleanField(default = False)
	timestamp 						= models.DateTimeField(auto_now_add = True)
	checked_time 					= models.DateTimeField(null = True)
	task_achievement 				= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	task_achievement_remark 		= models.TextField(blank = True, null = True)
	coherence_and_cohension 		= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	coherence_and_cohension_remark 	= models.TextField(blank = True, null = True)
	lexical_resource 				= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	lexical_resource_remark 		= models.TextField(blank = True, null = True)
	grammer_range_accuracy 			= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	grammer_range_accuracy_remark 	= models.TextField(blank = True, null = True)
	overall_band 					= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)

	class Meta:
		ordering = ['timestamp']


class AnswerTaskTwo(models.Model):
	question 						= models.TextField()
	answer 							= models.TextField()
	word_count 						= models.PositiveSmallIntegerField()
	student_key 					= models.ForeignKey(Student, on_delete = models.CASCADE)
	is_checked 						= models.BooleanField(default = False)
	timestamp 						= models.DateTimeField(auto_now_add = True)
	checked_time 					= models.DateTimeField(null = True)
	task_achievement 				= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	task_achievement_remark 		= models.TextField(blank = True, null = True)
	coherence_and_cohension 		= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	coherence_and_cohension_remark 	= models.TextField(blank = True, null = True)
	lexical_resource 				= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	lexical_resource_remark 		= models.TextField(blank = True, null = True)
	grammer_range_accuracy 			= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)
	grammer_range_accuracy_remark 	= models.TextField(blank = True, null = True)
	overall_band 					= models.DecimalField(blank = True, null = True, max_digits=2, decimal_places=1)

	class Meta:
		ordering = ['timestamp']
