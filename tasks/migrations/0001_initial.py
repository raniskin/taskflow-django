from django.conf import settings
from django.db import migrations,models
import django.db.models.deletion
class Migration(migrations.Migration):
 initial=True
 dependencies=[migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
 operations=[migrations.CreateModel(name='Task',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('title',models.CharField(max_length=180,verbose_name='Название')),('description',models.TextField(blank=True,verbose_name='Описание')),('status',models.CharField(choices=[('todo','К выполнению'),('progress','В процессе'),('done','Готово')],default='todo',max_length=12,verbose_name='Статус')),('priority',models.CharField(choices=[('low','Низкий'),('medium','Средний'),('high','Высокий')],default='medium',max_length=10,verbose_name='Приоритет')),('due_date',models.DateField(blank=True,null=True,verbose_name='Дедлайн')),('created_at',models.DateTimeField(auto_now_add=True)),('owner',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='tasks',to=settings.AUTH_USER_MODEL))],options={'ordering':['-created_at']})]
