from django.db import models
from django.conf import settings
class Task(models.Model):
 STATUS_CHOICES=[('todo','К выполнению'),('progress','В процессе'),('done','Готово')]
 PRIORITY_CHOICES=[('low','Низкий'),('medium','Средний'),('high','Высокий')]
 owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='tasks')
 title=models.CharField('Название',max_length=180)
 description=models.TextField('Описание',blank=True)
 status=models.CharField('Статус',max_length=12,choices=STATUS_CHOICES,default='todo')
 priority=models.CharField('Приоритет',max_length=10,choices=PRIORITY_CHOICES,default='medium')
 due_date=models.DateField('Дедлайн',null=True,blank=True)
 created_at=models.DateTimeField(auto_now_add=True)
 class Meta:
  ordering=['-created_at']
 def __str__(self):return self.title
