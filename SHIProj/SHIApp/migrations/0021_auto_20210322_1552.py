# Generated by Django 3.1.6 on 2021-03-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHIApp', '0020_auto_20210322_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotpropertylist',
            name='Prop_BHK1Price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='hotpropertylist',
            name='Prop_BHK2Price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='hotpropertylist',
            name='Prop_BHK3Price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='hotpropertylist',
            name='Prop_BHK4Price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='propertylist',
            name='BHK1Price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='propertylist',
            name='BHK2Price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='propertylist',
            name='BHK3Price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='propertylist',
            name='BHK4Price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='hotpropertylist',
            name='Property_Price',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='propertylist',
            name='Property_Price',
            field=models.CharField(default='', max_length=50),
        ),
    ]
