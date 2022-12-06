from django.test import TestCase, Client
from django.urls import reverse
from ticketApp.models import *
import json



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index = reverse('index')
        self.pending_ticket = reverse('pending_ticket')
        self.create_ticket = reverse('create_ticket')
        self.ticket_by_id = reverse('ticket_by_id', args=['2'])
        # self.ticket_id = Ticket.objects.get(pk=2)
        self.ticket_by_id2 = reverse('ticket_by_id2')
        self.ticket_by_id_cnt_edit = reverse('ticket_by_id_cnt_edit', args=['2'])


    def test_index_GET(self):
        response = self.client.get(self.index)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_pending_ticket_GET(self):
        response = self.client.get(self.pending_ticket)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ticket_pending.html')

    
    def test_create_ticket_POST(self):
        response = self.client.get(self.create_ticket)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_ticket.html')


    # def test_ticket_by_id_GET(self):
    #     response = self.client.get(self.ticket_id)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'ticket_by_id.html')


    # def test_ticket_by_id_GET(self):
    #     response = self.client.get(self.ticket_by_id2)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'ticket_by_id.html')


    # def test_ticket_by_id_cnt_edit_GET(self):
    #     response = self.client.get(self.ticket_by_id_cnt_edit)

    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'ticket_by_id_cnt_edit.html')