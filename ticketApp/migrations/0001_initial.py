# Generated by Django 3.2.16 on 2022-12-06 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locker_num', models.IntegerField(blank=True, null=True)),
                ('locker_status', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], default='Available', max_length=15)),
                ('locker_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
        ),
        migrations.CreateModel(
            name='RandomNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagnum', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('requester_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('status', models.CharField(choices=[('Student to Drop the Document', 'Student To Drop'), ('Student to Collect the Document', 'Student To Collect'), ('Student Collected the Document', 'Student Collected'), ('Admin to Drop the Document', 'Admin To Drop'), ('Admin to Collect the Document', 'Admin To Collect'), ('Admin Collected the Document', 'Admin Collected'), ('Admin is Verifying the Document', 'Admin Verifying'), ('Admin Verified the Document', 'Admin Verified'), ('Admin is Reviewing the Document', 'Admin Rewiewing'), ('Admin Reviewed the Document', 'Admin Reviewed'), ('Completed', 'Completed'), ('Void', 'Voided')], default='Student to Drop the Document', max_length=60)),
                ('description', models.TextField()),
                ('tag_num', models.IntegerField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('locker_num', models.ForeignKey(blank=True, default=None, limit_choices_to={'locker_status': 'Available'}, null=True, on_delete=django.db.models.deletion.CASCADE, to='ticketApp.locker')),
            ],
        ),
    ]
