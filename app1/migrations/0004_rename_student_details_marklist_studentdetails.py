# Generated by Django 4.2 on 2023-04-15 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_collage_marklist_student_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marklist',
            old_name='Student_Details',
            new_name='studentdetails',
        ),
    ]
