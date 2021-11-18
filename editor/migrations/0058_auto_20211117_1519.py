# Generated by Django 3.2.5 on 2021-11-17 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import editor.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('editor', '0057_itemqueue_itemqueuechecklistitem_itemqueuechecklisttick_itemqueueentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectaccess',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_projectaccess', to='editor.project'),
        ),
        migrations.CreateModel(
            name='IndividualAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('access', models.CharField(choices=[('view', 'Can view'), ('edit', 'Can edit')], default='view', max_length=6)),
                ('object_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='individual_accesses', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, editor.models.TimelineMixin),
        ),
    ]
