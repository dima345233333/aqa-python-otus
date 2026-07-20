import csv
import json

# Чтение JSON пользователей
with open('users.json', 'r', encoding='utf-8') as file_users:
    users = json.load(file_users)

# Чтение CSV с книгами
with open('books.csv', 'r', encoding='utf-8') as file_csv:
    reader = csv.DictReader(file_csv)  # Читаем как словари
    books = list(reader)

# Распределени книг
total_books = len(books)
total_users = len(users)
books_per_user = total_books // total_users
extra_books = total_books % total_users

users_update = []
book_index = 0

for i, user in enumerate(users):
    user_copy = user.copy()

    if i < extra_books:
        user_books_count = books_per_user + 1
    else:
        user_books_count = books_per_user

    user_copy['books'] = books[book_index:book_index + user_books_count]
    book_index += user_books_count

    users_update.append(user_copy)

# Запись обновленнного JSON
with open('users_updated.json', 'w', encoding='utf-8') as file_result:
    json.dump(users_update, file_result, indent=2)