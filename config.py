import sqlite3
BOT_TOKEN = '8127289280:AAExatCe0dW7qMMG1LTUWeiitZojwOd_yPI'
SEEN_USERS = set()


DB_NAME = 'recipes.db'

# Создаем соединение с базой данных при запуске бота
db_connection = sqlite3.connect(DB_NAME)
cursor = db_connection.cursor()

# Создаем таблицу если она еще не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        image_path TEXT,
        ingredients TEXT,
        instructions TEXT
    )
''')

db_connection.commit()
