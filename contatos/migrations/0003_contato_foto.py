# Generated by Django 4.1.7 on 2023-03-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contatos", "0002_contato_mostrar"),
    ]

    operations = [
        migrations.AddField(
            model_name="contato",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos/%Y/%m/"),
        ),
    ]
