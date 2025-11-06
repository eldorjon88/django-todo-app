from django.test import TestCase
from django.urls import reverse

class TaskViewsTests(TestCase):
    def test_home_status_code(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_tasks_list_status_code(self):
        resp = self.client.get(reverse('tasks_list'))
        self.assertEqual(resp.status_code, 200)

    def test_create_page_status_code(self):
        resp = self.client.get(reverse('task_create'))
        self.assertEqual(resp.status_code, 200)
