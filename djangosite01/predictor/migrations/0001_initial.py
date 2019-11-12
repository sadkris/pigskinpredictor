# Generated by Django 2.2.7 on 2019-11-12 15:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('ShortName', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Town', models.CharField(max_length=20)),
                ('Nickname', models.CharField(max_length=20)),
                ('Logo', models.ImageField(default='football.png', upload_to='logos')),
            ],
        ),
        migrations.CreateModel(
            name='ScoresWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Week', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(17)])),
                ('WeekScore', models.IntegerField()),
                ('Season', models.IntegerField(validators=[django.core.validators.MinValueValidator(2012), django.core.validators.MaxValueValidator(2050)])),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-WeekScore', 'User'],
                'verbose_name_plural': 'Weekly Scores',
            },
        ),
        migrations.CreateModel(
            name='ScoresSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SeasonScore', models.IntegerField()),
                ('Season', models.IntegerField(validators=[django.core.validators.MinValueValidator(2012), django.core.validators.MaxValueValidator(2050)])),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-SeasonScore', 'User'],
                'verbose_name_plural': 'Season Scores',
            },
        ),
        migrations.CreateModel(
            name='ScoresAllTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AllTimeScore', models.IntegerField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-AllTimeScore', 'User'],
                'verbose_name_plural': 'All Time Scores',
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('Season', models.IntegerField(validators=[django.core.validators.MinValueValidator(2012), django.core.validators.MaxValueValidator(2050)])),
                ('Week', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(17)])),
                ('GameID', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(2010010101)])),
                ('HomeScore', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)])),
                ('AwayScore', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(150)])),
                ('Winner', models.CharField(max_length=4)),
                ('AwayTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AwayTeam_Results_Set', to='predictor.Team')),
                ('HomeTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HomeTeam_Results_Set', to='predictor.Team')),
            ],
            options={
                'verbose_name_plural': 'Results',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('Season', models.IntegerField(validators=[django.core.validators.MinValueValidator(2012), django.core.validators.MaxValueValidator(2050)])),
                ('Week', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(17)])),
                ('GameID', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(2010010101)])),
                ('DateTime', models.DateTimeField()),
                ('AwayTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='AwayTeam_Schedule_Set', to='predictor.Team')),
                ('HomeTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HomeTeam_Schedule_Set', to='predictor.Team')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Winner', models.CharField(choices=[('Home', 'Home'), ('Away', 'Away')], max_length=4)),
                ('Points', models.IntegerField(blank=True, null=True)),
                ('Banker', models.BooleanField(default=False)),
                ('PredWeek', models.IntegerField(blank=True, null=True)),
                ('Game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Match_Prediction_Set', to='predictor.Match')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('User', 'Game')},
            },
        ),
        migrations.CreateModel(
            name='Banker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserSeasonKey', models.CharField(blank=True, max_length=10, null=True)),
                ('BankWeek', models.IntegerField(blank=True, null=True)),
                ('BankSeason', models.IntegerField(blank=True, null=True)),
                ('BankGame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Match_Banker_Set', to='predictor.Match')),
                ('BankerTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BankerTeam_Banker_Set', to='predictor.Team')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('UserSeasonKey', 'BankerTeam')},
            },
        ),
    ]
