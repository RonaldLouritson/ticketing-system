from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class TicketStatus(models.TextChoices):
	STUDENT_TO_DROP = 'Student to Drop the Document'
	STUDENT_TO_COLLECT = 'Student to Collect the Document'
	STUDENT_COLLECTED = 'Student Collected the Document'
	ADMIN_TO_DROP = 'Admin to Drop the Document'
	ADMIN_TO_COLLECT = 'Admin to Collect the Document'
	ADMIN_COLLECTED = 'Admin Collected the Document'
	ADMIN_VERIFYING = 'Admin is Verifying the Document'
	ADMIN_VERIFIED = 'Admin Verified the Document'
	ADMIN_REWIEWING = 'Admin is Reviewing the Document'
	ADMIN_REVIEWED = 'Admin Reviewed the Document'
	COMPLETED = 'Completed'
	VOIDED = 'Void'


class LockerStatus(models.TextChoices):
	AVAILABLE = 'Available'
	UNAVAILABLE = 'Unavailable'


class Ticket(models.Model):
	title = models.CharField(max_length=100)
	requester_email = models.EmailField(blank=True,null=True)
	#assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
	status = models.CharField(max_length=60, choices=TicketStatus.choices, default=TicketStatus.STUDENT_TO_DROP)
	description = models.TextField()
	locker_num = models.ForeignKey('Locker', limit_choices_to={'locker_status': 'Available'}, null=True, blank=True, default=None, on_delete=models.CASCADE)
	tag_num = models.IntegerField(blank=True,null=True,default=None)
	created_at = models.DateTimeField('created at', auto_now_add=True)
	updated_at = models.DateTimeField('updated at', auto_now=True)	


class RandomNumber(models.Model):
	tagnum = models.IntegerField(blank=True,null=True)


class Locker(models.Model):
	locker_num = models.IntegerField(blank=True,null=True)
	locker_status = models.CharField(max_length=15, choices=LockerStatus.choices, default=LockerStatus.AVAILABLE)
	locker_available = models.BooleanField(default=True)
	created_at = models.DateTimeField('created at', auto_now_add=True)
	updated_at = models.DateTimeField('updated at', auto_now=True)

	def __str__(self):
		return str(self.locker_num)