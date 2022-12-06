from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/pending', views.pending_ticket, name='pending_ticket'),
    path('ticket/create', views.create_ticket, name='create_ticket'),
    path('ticket/save', views.save_ticket, name='save_ticket'),
    #path('ticket/update/<int:ticket_id>', views.update_ticket, name='update_ticket'),
    path('ticket/update', views.update_ticket, name='update_ticket'),
    #path('ticket/update/update_ticket', views.update_ticket, name='update_ticket'),
    path('ticket/details/<int:ticket_id>', views.ticket_by_id, name='ticket_by_id'),
    #path('ticket/details', views.ticket_by_id2, name='ticket_by_id2'),
    path('ticket/details/ticket_by_id2', views.ticket_by_id2, name='ticket_by_id2'),
    path('ticket/details_all/<int:ticket_id>', views.ticket_by_id_cnt_edit, name='ticket_by_id_cnt_edit'),
    path('ticket/reset', views.reset_tag_number, name='reset_tag_number'),
    path('ticket/admin_drop', views.admin_drop, name='admin_drop'),
    path('ticket/admin_drop_doc', views.admin_drop_doc, name='admin_drop_doc'),
    path('ticket/student_drop', views.student_drop, name='student_drop'),
    path('ticket/student_drop_doc', views.student_drop_doc, name='student_drop_doc'),
]
