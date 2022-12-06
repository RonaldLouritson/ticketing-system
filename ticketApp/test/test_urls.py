from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ticketApp.views import *

class TestUrls(SimpleTestCase):

    def test_index(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_pending_ticket(self):
        url = reverse('pending_ticket')
        self.assertEqual(resolve(url).func, pending_ticket)

    def test_create_ticket(self):
        url = reverse('create_ticket')
        self.assertEqual(resolve(url).func, create_ticket)

    def test_save_ticket(self):
        url = reverse('save_ticket')
        self.assertEqual(resolve(url).func, save_ticket)

    def test_update_ticket(self):
        url = reverse('update_ticket')
        self.assertEqual(resolve(url).func, update_ticket)

    def test_ticket_by_id(self):
        url = reverse('ticket_by_id', args=['4'])
        self.assertEqual(resolve(url).func, ticket_by_id)

    def test_ticket_by_id2(self):
        url = reverse('ticket_by_id2')
        self.assertEqual(resolve(url).func, ticket_by_id2)

    def test_ticket_by_id_cnt_edit(self):
        url = reverse('ticket_by_id_cnt_edit', args=['2'])
        self.assertEqual(resolve(url).func, ticket_by_id_cnt_edit)

    def test_reset_tag_number(self):
        url = reverse('reset_tag_number')
        self.assertEqual(resolve(url).func, reset_tag_number)

    def test_student_drop(self):
        url = reverse('student_drop')
        self.assertEqual(resolve(url).func, student_drop)

    def test_student_drop_doc(self):
        url = reverse('student_drop_doc')
        self.assertEqual(resolve(url).func, student_drop_doc)

    def test_admin_drop(self):
        url = reverse('admin_drop')
        self.assertEqual(resolve(url).func, admin_drop)

    def test_admin_drop_doc(self):
        url = reverse('admin_drop_doc')
        self.assertEqual(resolve(url).func, admin_drop_doc)