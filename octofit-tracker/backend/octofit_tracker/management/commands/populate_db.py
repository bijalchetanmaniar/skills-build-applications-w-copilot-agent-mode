from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', username='IronMan', team=marvel)
        captain = User.objects.create(email='captain@marvel.com', username='CaptainAmerica', team=marvel)
        batman = User.objects.create(email='batman@dc.com', username='Batman', team=dc)
        superman = User.objects.create(email='superman@dc.com', username='Superman', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date='2026-02-17')
        Activity.objects.create(user=batman, type='Cycling', duration=45, date='2026-02-16')
        Activity.objects.create(user=captain, type='Swimming', duration=60, date='2026-02-15')
        Activity.objects.create(user=superman, type='Flying', duration=120, date='2026-02-14')

        # Create workouts
        pushups = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        situps = Workout.objects.create(name='Situps', description='Do 30 situps')
        pushups.suggested_for.add(ironman, captain)
        situps.suggested_for.add(batman, superman)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
