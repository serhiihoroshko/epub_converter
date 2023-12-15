import os
import uuid
from ebooklib import epub
from faker import Faker


def generate_uuid():
    return str(uuid.uuid4())


def generate_random_title():
    fake = Faker()
    return fake.catch_phrase()


def txt_to_epub(txt_folder, epub_file):
    txt_files = [file for file in os.listdir(txt_folder) if file.endswith(".txt")]

    book = epub.EpubBook()
    book.set_identifier(generate_uuid())

    random_title = generate_random_title()
    book.set_title(random_title)

    book.set_language('en')

    for index, txt_file in enumerate(txt_files):
        txt_path = os.path.join(txt_folder, txt_file)
        with open(txt_path, 'r', encoding='utf-8') as file:
            content = file.read()

        chapter = epub.EpubItem(uid=f"chapter{index + 1}",
                                file_name=f"chapter{index + 1}.xhtml",
                                content=content,
                                media_type="application/xhtml+xml")
        book.add_item(chapter)

    book.spine = book.items

    epub.write_epub(epub_file, book, {})


txt_to_epub('txt_folder', 'output.epub')
