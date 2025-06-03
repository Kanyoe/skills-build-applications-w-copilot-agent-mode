from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(id=ObjectId(), email="john.doe@example.com", name="John Doe", password="password123")
        user2 = User.objects.create(id=ObjectId(), email="jane.smith@example.com", name="Jane Smith", password="password456")

        # Create test teams
        Team.objects.create(id=ObjectId(), name="Team Alpha", members=["John Doe", "Jane Smith"])

        # Create test activities
        Activity.objects.create(id=ObjectId(), user=user1, type="Running", duration=30)
        Activity.objects.create(id=ObjectId(), user=user2, type="Cycling", duration=45)

        # Create test leaderboard entries
        Leaderboard.objects.create(id=ObjectId(), user=user1, points=100)
        Leaderboard.objects.create(id=ObjectId(), user=user2, points=150)

        # Create test workouts
        Workout.objects.create(id=ObjectId(), name="Morning Run", description="A quick morning run to start the day.")
        Workout.objects.create(id=ObjectId(), name="Evening Yoga", description="Relaxing yoga session in the evening.")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
