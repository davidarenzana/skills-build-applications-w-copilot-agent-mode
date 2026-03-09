"""octofit_tracker URL Configuration





















        self.assertIn('testuser', str(self.leaderboard))    def test_leaderboard(self):        self.assertEqual(str(self.workout), 'Test Workout')    def test_workout(self):        self.assertIn('testuser', str(self.activity))    def test_activity(self):        self.assertEqual(str(self.user), 'testuser')    def test_user(self):        self.assertEqual(str(self.team), 'Test Team')    def test_team(self):        self.leaderboard = Leaderboard.objects.create(user=self.user, score=123)        self.workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for=self.team)        self.activity = Activity.objects.create(user=self.user, type='Run', duration=10, calories=100)        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)        self.team = Team.objects.create(name='Test Team')    def setUp(self):class ModelSmokeTest(TestCase):The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.http import JsonResponse
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')

def api_info(request):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        base_url = "http://localhost:8000/api/"
    return JsonResponse({
        "api_base_url": base_url,
        "endpoints": [
            f"{base_url}users/",
            f"{base_url}teams/",
            f"{base_url}activities/",
            f"{base_url}workouts/",
            f"{base_url}leaderboard/",
        ]
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_info, name='api-info'),
    path('api/', include(router.urls)),
]
