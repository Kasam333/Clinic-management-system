import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Blog_App.models import Post, Category

class Command(BaseCommand):
    help = "Generate fake blog posts with users and predefined categories"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Predefined categories
        predefined_categories = [
            "Artificial Intelligence",
            "Business",
            "Disaster",
            "Education",
            "Entertainment",
            "Health",
            "Life Style",
            "Politics",
            "Programming",
            "Science",
            "Sports",
            "Stock market",
            "Technology",
            "Travel",
        ]

        # Fetch existing categories or create them if not present
        categories = []
        for category_name in predefined_categories:
            category, created = Category.objects.get_or_create(name=category_name)
            categories.append(category)

        password = "abc123"  # Default password for all users
        # Generate users
        for _ in range(10):  # Create 10 users
            first_name = fake.first_name()
            email = fake.email()
            user, created = User.objects.get_or_create(username=email, first_name=first_name)
            if created:
                user.set_password(password)
                user.save()

            # Generate posts for each user
            for _ in range(random.randint(1, 5)):  # Each user has 1 to 5 posts
                title = fake.sentence(nb_words=6)
                title_description = fake.sentence(nb_words=10)
                body = fake.text(max_nb_chars=2000)
                category = random.choice(categories)
                post_image = random.choice([
                    "images/0_AZ4xTk4tDgeuH5UM.webp",
                    "images/0_UaZS29qc_qxURjPD.webp",
                    "images/post3.webp",
                    None  # Occasionally leave the post without an image
                ])
                post = Post.objects.create(
                    author=user,
                    title=title,
                    title_description=title_description,
                    body=body,
                    category=category.name,
                    post_image=post_image,  # Use one of the sample images or None
                )
                self.stdout.write(self.style.SUCCESS(f"Created post: {post.title} by {user.username}"))

        self.stdout.write(self.style.SUCCESS("Fake data generation complete!"))
