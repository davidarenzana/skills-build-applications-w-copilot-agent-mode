from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Crear actividades
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300)
        Activity.objects.create(user=spiderman, type='Cycling', duration=45, calories=400)
        Activity.objects.create(user=batman, type='Swimming', duration=60, calories=500)
        Activity.objects.create(user=superman, type='Yoga', duration=20, calories=100)

        # Crear workouts
        Workout.objects.create(name='Full Body', description='Full body workout', suggested_for=marvel)
        Workout.objects.create(name='Strength', description='Strength workout', suggested_for=dc)

        # Crear leaderboard
        Leaderboard.objects.create(user=ironman, score=1000)
        Leaderboard.objects.create(user=spiderman, score=900)
        Leaderboard.objects.create(user=batman, score=950)
        Leaderboard.objects.create(user=superman, score=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
