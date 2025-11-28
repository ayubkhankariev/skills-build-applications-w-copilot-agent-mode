from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Очистка коллекций
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Команды
        marvel = Team.objects.create(name='marvel', description='Marvel super heroes')
        dc = Team.objects.create(name='dc', description='DC super heroes')

        # Пользователи
        users = [
            User.objects.create(email='tony@marvel.com', name='Tony Stark', team=marvel.name),
            User.objects.create(email='steve@marvel.com', name='Steve Rogers', team=marvel.name),
            User.objects.create(email='bruce@marvel.com', name='Bruce Banner', team=marvel.name),
            User.objects.create(email='clark@dc.com', name='Clark Kent', team=dc.name),
            User.objects.create(email='bruce@dc.com', name='Bruce Wayne', team=dc.name),
            User.objects.create(email='diana@dc.com', name='Diana Prince', team=dc.name),
        ]

        # Тренировки
        workouts = [
            Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy'),
            Workout.objects.create(name='Running', description='Run 5km', difficulty='medium'),
            Workout.objects.create(name='Deadlift', description='Heavy deadlift', difficulty='hard'),
        ]

        # Активности
        Activity.objects.create(user=users[0].email, activity_type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1].email, activity_type='pushups', duration=15, date=timezone.now().date())
        Activity.objects.create(user=users[3].email, activity_type='deadlift', duration=45, date=timezone.now().date())

        # Лидерборд
        Leaderboard.objects.create(user=users[0].email, score=100)
        Leaderboard.objects.create(user=users[3].email, score=120)
        Leaderboard.objects.create(user=users[4].email, score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
