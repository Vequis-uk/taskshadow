from django.test import TestCase
from django.contrib.auth.models import User
from .models import TaskShadowTodo


class TaskShadowTodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user to associate with the tasks
        cls.user = User.objects.create_user(
            username='testuser', password='testpass')
        # Create a sample task
        cls.task = TaskShadowTodo.objects.create(
            user=cls.user,
            title="Sample Task",
            completed=False
        )

    def test_task_creation(self):
        """Test that a task is created correctly."""
        task = TaskShadowTodo.objects.get(id=self.task.id)
        self.assertEqual(task.title, "Sample Task")
        self.assertEqual(task.completed, False)
        self.assertEqual(task.user, self.user)

    def test_task_str_method(self):
        """Test the string representation of the task."""
        task = TaskShadowTodo.objects.get(id=self.task.id)
        self.assertEqual(str(task), "Sample Task")

    def test_task_defaults(self):
        """Test the default values for the model fields."""
        new_task = TaskShadowTodo.objects.create(
            user=self.user,
            title="Another Task"
        )
        self.assertFalse(new_task.completed)
        # Default value for `completed` is False
