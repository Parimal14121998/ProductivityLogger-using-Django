from django.test import TestCase
from django.contrib.auth.models import User
from datetime import timedelta, datetime
from tasks.models import Task, WorkSession

class TaskModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(
            user=self.user,
            title='Test Task',
            description='Test Description',
            time_limit=timedelta(hours=8)
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.time_limit, timedelta(hours=8))
        self.assertFalse(self.task.completed)
        self.assertFalse(self.task.time_exceeded)

    def test_work_session_duration(self):
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=2)
        session = WorkSession.objects.create(
            task=self.task,
            start_time=start_time,
            end_time=end_time
        )
        self.assertEqual(session.duration(), timedelta(hours=2))

    def test_total_working_hours(self):
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=2)
        WorkSession.objects.create(task=self.task, start_time=start_time, end_time=end_time)
        WorkSession.objects.create(task=self.task, start_time=end_time, end_time=end_time + timedelta(hours=3))
        total_hours = self.task.total_working_hours()
        self.assertEqual(total_hours, timedelta(hours=5))

    def test_task_completion_and_time_exceeded(self):
        self.task.completed = True
        start_time = datetime.now()
        end_time = start_time + timedelta(hours=10)
        WorkSession.objects.create(task=self.task, start_time=start_time, end_time=end_time)
        self.task.save()
        self.assertTrue(self.task.time_exceeded)
