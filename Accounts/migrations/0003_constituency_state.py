# Generated by Django 2.2.4 on 2019-08-30 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_auto_20190823_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='constituency',
            name='state',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Accounts.State'),
            preserve_default=False,
        ),
    ]
