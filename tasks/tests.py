from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task
class TaskFlowTests(TestCase):
 def setUp(self):
  self.a=User.objects.create_user('alice',password='safe-test-pass-123')
  self.b=User.objects.create_user('bob',password='safe-test-pass-123')
  self.task=Task.objects.create(owner=self.a,title='Только для Алисы')
 def test_anonymous_redirected(self):
  self.assertEqual(self.client.get('/').status_code,302)
 def test_ownership_enforced(self):
  self.client.force_login(self.b)
  self.assertEqual(self.client.get(reverse('task_edit',args=[self.task.pk])).status_code,404)
  self.assertEqual(self.client.post(reverse('task_delete',args=[self.task.pk])).status_code,404)
 def test_create_task_owner(self):
  self.client.force_login(self.b)
  self.client.post(reverse('task_create'),{'title':'Новая','priority':'high','status':'todo'})
  self.assertTrue(Task.objects.filter(owner=self.b,title='Новая').exists())
