import sqlite3
from html2text import html2text

conn = sqlite3.connect('Развитие_личности_base/assets/database.db')
cursor = conn.cursor()
cursor.execute("SELECT title, text FROM items ORDER BY _id;")

with open('book.md', 'w', encoding='utf-8') as f:
    for title, content in cursor:
        # Конвертируем HTML в Markdown и очищаем лишние теги
        clean_text = html2text(content).replace('\n', '  \n')  # Сохраняем переносы строк
        f.write(f"# {title}\n\n{clean_text}\n\n")

conn.close()
