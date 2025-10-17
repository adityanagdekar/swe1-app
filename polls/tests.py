from django.test import TestCase
from .models import Task


class TaskModelTest(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title="Test Task", description="Test Description")
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.is_completed)

    def test_task_str(self):
        task = Task.objects.create(title="Test Task")
        self.assertEqual(str(task), "Test Task")


class TaskViewTest(TestCase):
    def test_task_list_view(self):
        response = self.client.get("/polls/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Todo List")

    def test_add_task(self):
        response = self.client.post(
            "/polls/add/", {"title": "New Task", "description": "New Description"}
        )
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(response.status_code, 302)  # Redirect
