# Generated by Django 3.2.16 on 2022-11-14 16:11

from django.db import migrations, models
import myapp.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_Name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=100, null=True, validators=[myapp.validators.gmail_validation])),
                ('age', models.IntegerField(max_length=50, null=True)),
                ('Class', models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('5', 'Fifth'), ('6', 'Sixth'), ('7', 'Seventh'), ('8', 'Eigth'), ('9', 'Ninth'), ('10', 'Tenth'), ('11', 'Eleventh'), ('12', 'Tweleth')], default='1', max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
