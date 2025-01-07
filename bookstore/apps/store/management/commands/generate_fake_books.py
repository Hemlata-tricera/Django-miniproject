from django.core.management.base import BaseCommand
from faker import Faker
from apps.store.models import Book, Category
import random

class Command(BaseCommand):
    help = 'Generates fake bookstore data for the database'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create fake categories
        category_list = []
        for _ in range(10):  # Create 10 fake categories
            category_name = fake.name()
            desc = fake.text(max_nb_chars=200)
            category = Category.objects.create(name=category_name, description=desc)
            category_list.append(category)

        # Prepare list for bulk creation of books
        books_to_create = []
        for _ in range(15000):  # Create 15000 fake books
            title = fake.sentence(nb_words=4)
            author = fake.name()
            genre = random.choice(category_list)  # Randomly select category
            price = round(random.uniform(10.0, 50.0), 2)
            stock = random.randint(1, 50)

            books_to_create.append(
                Book(
                    title=title,
                    author=author,
                    genre=genre,  # Foreign key to category
                    price=price,
                    stock=stock
                )
            )

        # Bulk create books
        Book.objects.bulk_create(books_to_create)

        self.stdout.write(self.style.SUCCESS('Successfully generated fake bookstore data!'))
