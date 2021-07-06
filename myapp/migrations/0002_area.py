# Generated by Django 3.0 on 2021-07-03 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area', models.CharField(choices=[('Sg highway,Ahmedabad West', 'Sg highway,Ahmedabad West'), ('Shela,Ahmedabad West', 'Shela,Ahmedabad West'), ('South Bopal,Ahmedabad West', 'South Bopal,Ahmedabad West'), ('Chandkhelda,Ahmedabad North', 'Chandkhelda,Ahmedabad North'), ('Naroda,Ahmedabad East', 'Naroda,Ahmedabad East'), ('Bopal,Ahmedabad West', 'Bopal,Ahmedabad West'), ('Thaltej,Ahmedabad West', 'Thaltej,Ahmedabad West'), ('Satellite,Ahmedabad West', 'Satellite,Ahmedabad West'), ('Gota,Ahmedabad North', 'Gota,Ahmedabad North')], max_length=100)),
                ('Looking_To', models.CharField(max_length=100)),
                ('Property_Kind', models.TextField()),
                ('Address', models.TextField()),
                ('Property_Layout', models.TextField()),
                ('Property_Ownership', models.CharField(max_length=100)),
                ('Super_Area', models.TextField()),
                ('facing_road', models.TextField()),
                ('Property_Flooring', models.CharField(max_length=100)),
                ('Water_source', models.CharField(max_length=100)),
                ('Furnishing', models.CharField(max_length=100)),
                ('Facing', models.CharField(max_length=100)),
                ('Property_id', models.TextField()),
                ('Price', models.TextField()),
                ('Additional_Details', models.TextField()),
                ('Contact', models.TextField()),
                ('Image1', models.ImageField(upload_to='Property_Images/')),
                ('Image2', models.ImageField(upload_to='Property_Images/')),
                ('Image3', models.ImageField(upload_to='Property_Images/')),
                ('Image4', models.ImageField(upload_to='Property_Images/')),
                ('Image5', models.ImageField(upload_to='Property_Images/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User')),
            ],
        ),
    ]