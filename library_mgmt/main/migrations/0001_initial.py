# Generated by Django 5.1.1 on 2024-12-06 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(choices=[('book', 'Book'), ('movie', 'Movie')], default='book', max_length=5)),
                ('name', models.CharField(max_length=255)),
                ('date_of_procurement', models.DateField()),
                ('quantity', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_address', models.TextField()),
                ('adhaar_card_no', models.CharField(max_length=12)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('membership_type', models.CharField(choices=[('6_months', 'Six Months'), ('1_year', 'One Year'), ('2_years', 'Two Years')], default='6_months', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('new', 'New User'), ('existing', 'Existing User')], default='new', max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('admin_status', models.CharField(choices=[('yes', 'Admin'), ('no', 'User')], default='no', max_length=10)),
            ],
        ),
    ]
