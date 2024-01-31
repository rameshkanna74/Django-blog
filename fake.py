from faker import Faker

fake = Faker()

def generate_fake_book():
    return {
        'title': fake.catch_phrase(),
        'author': fake.name(),
        'genre': fake.word(),
        'published_year': fake.year(),
        'isbn': fake.isbn13(),
    }

def generate_fake_book_list(num_books=10):
    return [generate_fake_book() for _ in range(num_books)]

if __name__ == "__main__":
    fake_books = generate_fake_book_list()

    for idx, book in enumerate(fake_books, start=1):
        print(f"Book {idx}: {book}")
