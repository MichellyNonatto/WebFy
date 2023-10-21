# Generated by Django 4.2.5 on 2023-10-21 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicas', '0012_alter_musica_categoria_alter_usuario_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='categoria',
            field=models.CharField(choices=[('ROCK', 'Rock'), ('POP', 'Pop'), ('OUTROS', 'Outros'), ('MPB', 'MPB'), ('PAGODE', 'Pagode')], max_length=10),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(default='avatar.jpg', upload_to='foto_perfil'),
        ),
    ]
