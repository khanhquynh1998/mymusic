# Generated by Django 3.2 on 2021-04-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_song_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name_type',
            field=models.CharField(blank=True, choices=[('Vpop', 'Vpop'), ('Kpop', 'Kpop'), ('USUK', 'USUK')], max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]