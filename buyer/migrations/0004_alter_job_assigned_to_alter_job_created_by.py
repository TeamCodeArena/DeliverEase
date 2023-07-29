# Generated by Django 4.2.3 on 2023-07-29 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0001_initial'),
        ('buyer', '0003_alter_job_assigned_to_alter_job_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='userAuth.seller'),
        ),
        migrations.AlterField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyers', to='userAuth.buyer'),
        ),
    ]
