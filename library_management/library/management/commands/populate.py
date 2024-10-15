# library/management/commands/populate.py

from django.core.management.base import BaseCommand
from faker import Faker
from library.models import Author, Book, Borrower, Borrowing
import random

class Command(BaseCommand):
    help = 'Populate the database with random data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create authors
        authors = []
        for _ in range(10):  # Create 10 authors
            author = Author.objects.create(
                name=fake.name(),
                bio=fake.text(max_nb_chars=200)
            )
            authors.append(author)

        # Create books
        books = []
        for _ in range(20):  # Create 20 books
            book = Book.objects.create(
                title=fake.sentence(nb_words=4),
                author=random.choice(authors),
                published_date=fake.date(),
                isbn=fake.isbn13(),
                pages=random.randint(100, 500),
                language=random.choice(['English', 'Spanish', 'French', 'German']),
            )
            books.append(book)

        # Create borrowers
        borrowers = []
        for _ in range(5):  # Create 5 borrowers
            borrower = Borrower.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
            )
            borrowers.append(borrower)

        # Create borrowings
        for _ in range(15):  # Create 15 borrowing records
            Borrowing.objects.create(
                borrower=random.choice(borrowers),
                book=random.choice(books),
                borrow_date=fake.date(),
                return_date=fake.date(),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with random data'))
