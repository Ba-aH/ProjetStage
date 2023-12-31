# Generated by Django 4.2.3 on 2023-08-14 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('piece', '0004_alter_piece_piece_image'),
        ('panier', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panierpiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qts', models.PositiveIntegerField(default=1)),
                ('panier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panier.panier')),
                ('piece', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='piece.piece')),
            ],
        ),
        migrations.DeleteModel(
            name='Panierpieces',
        ),
    ]
