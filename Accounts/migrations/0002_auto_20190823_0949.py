# Generated by Django 2.2.4 on 2019-08-23 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fathername', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='Candidate_photos')),
                ('gender', models.IntegerField()),
                ('dob', models.DateField()),
                ('mobileno', models.IntegerField()),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('alliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Alliance')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='voter',
            name='voted',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Party_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField()),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Party')),
            ],
        ),
        migrations.CreateModel(
            name='Constituency_Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField()),
                ('constituency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Constituency')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Party')),
            ],
        ),
        migrations.CreateModel(
            name='Constituency_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Candidate')),
                ('constituency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Constituency')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='constituency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Constituency'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Party'),
        ),
        migrations.CreateModel(
            name='Alliance_Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Alliance')),
            ],
        ),
        migrations.AddField(
            model_name='voter',
            name='constituency',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Accounts.Constituency'),
            preserve_default=False,
        ),
    ]