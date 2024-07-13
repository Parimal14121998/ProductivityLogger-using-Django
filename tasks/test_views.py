from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import timedelta
from tasks.models import Task

class TaskViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='Test Description',
            time_limit=timedelta(hours=8)
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

    def test_task_detail_view(self):
        response = self.client.get(reverse('task_detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Task')

    def test_task_create_view(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'New Description',
            'time_limit': '08:00:00'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    def test_task_edit_view(self):
        response = self.client.post(reverse('task_edit', args=[self.task.id]), {
            'title': 'Updated Task',
            'description': 'Updated Description',
            'time_limit': '08:00:00'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful update
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_task_delete_view(self):
        response = self.client.post(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after successful delete
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
