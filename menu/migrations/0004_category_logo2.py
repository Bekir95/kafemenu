# Generated by Django 4.2.21 on 2025-05-07 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_category_logo_menuitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='logo2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
