# Generated by Django 2.2.5 on 2019-09-21 21:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=150)),
                ('full_name', models.CharField(max_length=255)),
                ('abbrev', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerStatistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('rebounds', models.IntegerField()),
                ('nerd', models.FloatField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nba.Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nba.Player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nba.Team')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nba.Team'),
        ),
        migrations.CreateModel(
            name='GameState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team_score', models.IntegerField()),
                ('away_team_score', models.IntegerField()),
                ('broadcast', models.TextField(max_length=50)),
                ('quarter', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)])),
                ('time_left_in_quarter', models.TimeField()),
                ('game_status', models.CharField(max_length=30)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nba.Game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_games', to='nba.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_games', to='nba.Team'),
        ),
    ]