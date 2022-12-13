import random

import sweetify
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from .forms import *
from .models import Ticket


def index(request):
	tickets = Ticket.objects.order_by('-created_at')[:20]
	return render(request,'index.html', {'tickets': tickets})


def pending_ticket(request):
	tickets = Ticket.objects.exclude(Q(status='Completed') | Q(status='Void')).order_by('-created_at')[:20]
	return render(request,'ticket_pending.html', {'tickets': tickets})


def create_ticket(request):
	form = TicketForm()
	return render(request, "create_ticket.html", {'form': form})


def save_ticket(request):
	if request.method == 'POST':
		form = TicketForm(request.POST)
		getEmail = form.data['requester_email']
		getLockerId = form.data['locker_num']
		getEmailName = getEmail.split('@')[0]
		if form.is_valid():
			obj = form.save(commit=False)
			tag = random.randint(111111, 999999)
			obj.tag_num = tag
			form.save()

			objLoc = Locker.objects.get(id=getLockerId)
			objLoc.locker_status = 'Unavailable'
			objLoc.locker_available = False
			objLoc.save()

			getMsg = 'Hi '+ getEmailName + ', Locker Number : '+ str(objLoc.locker_num) +' Tag Num : '+ str(tag) +' to Drop the Documents.'

			subject = 'Locker and TAG Number'
			message = getMsg
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [getEmail, ]
			send_mail( subject, message, email_from, recipient_list )

			tickets = Ticket.objects.exclude(Q(status='Completed') | Q(status='Void')).order_by('-created_at')[:20]

	return render(request,'ticket_pending.html', {'tickets': tickets})


def update_ticket(request):
	ticketId = request.GET.get('ticketId')
	getStatus = request.GET.get('getStatus')
	getStatus = getStatus.replace(" ", "_")
	getStatus = getStatus.upper()
	getLockerNum = request.GET.get('getLockerNum')
	getTicket = Ticket.objects.get(pk=ticketId)

	if getTicket and getLockerNum == '':
		if getStatus == 'ADMIN_VERIFYING':
			getTicket.status = TicketStatus.ADMIN_VERIFYING
		elif getStatus == 'ADMIN_VERIFIED':
			getTicket.status = TicketStatus.ADMIN_VERIFIED
		elif getStatus == 'ADMIN_REWIEWING':
			getTicket.status = TicketStatus.ADMIN_REWIEWING
		elif getStatus =='ADMIN_REVIEWED':
			getTicket.status = TicketStatus.ADMIN_REVIEWED
		elif getStatus == 'COMPLETED':
			getTicket.status = TicketStatus.COMPLETED
		elif getStatus == 'VOIDED':
			getTicket.status = TicketStatus.VOIDED

		getTicket.save()

	elif getTicket and getLockerNum != '':
		if getStatus == 'ADMIN_TO_DROP':
			getTicket.status = TicketStatus.ADMIN_TO_DROP
			
			tag = random.randint(111111, 999999)
			getTicket.tag_num = tag

			getTicket.save()			
			Ticket.objects.filter(pk=ticketId).update(locker_num=Locker.objects.get(locker_num=getLockerNum).id)

			getMsg = 'Hi '+ getTicket.requester_email + ', You have Documents to Drop at Locker Number : '+ str(getLockerNum) +' Tag Num : '+ str(tag)

			subject = 'Document to Drop'
			message = getMsg
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [getTicket.requester_email, ]
			send_mail( subject, message, email_from, recipient_list )

			
	tickets = Ticket.objects.exclude(Q(status='Completed') | Q(status='Void')).order_by('-created_at')[:20]
	return render(request,'ticket_pending.html', {'tickets': tickets})
	
	
def ticket_by_id(request, ticket_id):
	ticket = Ticket.objects.get(pk=ticket_id)
	form_status = UpdateStatus(instance=ticket)
	locker = 'No'
	return render(request, 'ticket_by_id.html', {'ticket':ticket, 'form_status': form_status, 'locker': locker,})


def ticket_by_id2(request):
	status = request.POST.get('getStatus')
	ticket = Ticket.objects.get(pk=request.POST.get('ticketId'))
	getlocker = Locker.objects.filter(locker_status='Available').values('locker_num')
	if status == 'Admin To Drop' and ticket.locker_num is None:
		locker = 'Yes'
	else:
		locker = 'No'

	data = {
		'getlocker': list(getlocker),
		'locker': locker,
	}

	return JsonResponse(data)


def ticket_by_id_cnt_edit(request, ticket_id):
	ticket = Ticket.objects.get(pk=ticket_id)
	return render(request, 'ticket_by_id_cnt_edit.html', {'ticket':ticket})


def reset_tag_number(request):
	getTicketId = request.GET.get('ticketId')
	
	if getTicketId:
		getTicket = Ticket.objects.get(id=getTicketId)

		tag = random.randint(111111, 999999)
		getTicket.tag_num = tag
		getTicket.save()

		getMsg = 'Hi '+ getTicket.requester_email + ', Your Tag Num has been Reset : '+ str(tag) +' for Locker Number : '+ str(getTicket.locker_num) +' to Drop the Documents.'

		subject = 'Reset TAG Number'
		message = getMsg
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [getTicket.requester_email, ]
		send_mail( subject, message, email_from, recipient_list )

	sweetify.success(request, '', text='Tag Number for Ticket INT' + str(getTicketId).zfill(7) + ' Has been Reset', persistent='')
	form_status = UpdateStatus(instance=getTicket)
	return render(request, 'ticket_by_id.html', {'ticket':getTicket, 'form_status': form_status})


def student_drop(request):
	return render(request, 'student_dropcollect.html')


def student_drop_doc(request):
	if request.method == "POST":
		getLocketNum = request.POST.get('lockernumber')
		getTagNum = request.POST.get('tagnumber')
		getRadio = request.POST.get('checkradio')

		if getLocketNum and getTagNum:
			loc_id = Locker.objects.get(locker_num=getLocketNum)
			if loc_id:
				obj2 = Ticket.objects.filter(locker_num=loc_id, tag_num=getTagNum)
				if obj2:
					obj = Ticket.objects.get(locker_num=loc_id, tag_num=getTagNum)
					if getRadio == 'drop':

						tag = random.randint(111111, 999999)
						obj.tag_num = tag
						obj.save()

						getMsg = 'Hi '+ obj.requester_email + ', You have Documents to collect at Locker Number : '+ str(obj.locker_num) +' Tag Num : '+ str(tag)

						subject = 'Document Droped'
						message = getMsg
						email_from = settings.EMAIL_HOST_USER
						recipient_list = [obj.requester_email, ]
						send_mail( subject, message, email_from, recipient_list )

						obj.status = TicketStatus.ADMIN_TO_COLLECT
						obj.save()
						sweetify.success(request, '', text='Document Droped Successfully', persistent='')
					elif getRadio == 'collect':
						obj.status = TicketStatus.STUDENT_COLLECTED
						obj.save()

						loc_id.locker_status = 'Available'
						loc_id.locker_available = True
						loc_id.save()

						Ticket.objects.filter(id=obj.id).update(locker_num='')
						sweetify.success(request, '', text='Document Collected Successfully', persistent='')
					
				else:
					sweetify.warning(request, '', text='Locker and Tag Number not Match', persistent='')
			else:
				sweetify.warning(request, '', text='Locker Number not found', persistent='')
		else:
			sweetify.warning(request, '', text='Locker and Tag Number filed cannot be Empty', persistent='')

	tickets = Ticket.objects.exclude(Q(status='Completed') | Q(status='Void')).order_by('-created_at')[:20]
	return render(request,'ticket_pending.html', {'tickets': tickets})


def admin_drop(request):
	return render(request, 'admin_dropcollect.html')


def admin_drop_doc(request):
	if request.method == "POST":
		getLocketNum = request.POST.get('lockernumber')
		getTagNum = request.POST.get('tagnumber')
		getRadio = request.POST.get('checkradio')

		if getLocketNum and getTagNum:
			loc_id = Locker.objects.get(locker_num=getLocketNum)
			if loc_id:
				obj2 = Ticket.objects.filter(locker_num=loc_id, tag_num=getTagNum)
				if obj2:
					obj = Ticket.objects.get(locker_num=loc_id, tag_num=getTagNum)
					if getRadio == 'drop':

						tag = random.randint(111111, 999999)
						obj.tag_num = tag
						obj.save()

						getMsg = 'Hi '+ obj.requester_email + ', You have Documents to collect at Locker Number : '+ str(obj.locker_num) +' Tag Num : '+ str(tag)

						subject = 'Document Droped'
						message = getMsg
						email_from = settings.EMAIL_HOST_USER
						recipient_list = [obj.requester_email, ]
						send_mail( subject, message, email_from, recipient_list )

						obj.status = TicketStatus.STUDENT_TO_COLLECT
						obj.save()
						sweetify.success(request, '', text='Document Droped Successfully', persistent='')
					elif getRadio == 'collect':
						obj.status = TicketStatus.ADMIN_COLLECTED
						obj.save()

						loc_id.locker_status = 'Available'
						loc_id.locker_available = True
						loc_id.save()

						Ticket.objects.filter(id=obj.id).update(locker_num='')
						sweetify.success(request, '', text='Document Collected Successfully', persistent='')
					
				else:
					sweetify.warning(request, '', text='Locker and Tag Number not Match', persistent='')
			else:
				sweetify.warning(request, '', text='Locker Number not found', persistent='')
		else:
			sweetify.warning(request, '', text='Locker and Tag Number filed cannot be Empty', persistent='')

	tickets = Ticket.objects.exclude(Q(status='Completed') | Q(status='Void')).order_by('-created_at')[:20]
	return render(request,'ticket_pending.html', {'tickets': tickets})