from database import Database
from config import db_connection
db = Database('recipes.db')
db_connection.execute('''
    INSERT INTO recipes (name, type, image_path, ingredients, instructions)
    VALUES (?, ?, ?, ?, ?)
''', ("Омлет", "завтрак", "images/omelet.jpg", ", ".join(["яйца", "молоко", "соль", "черный перец"]), "Разбейте яйца в чашку, добавьте молоко, соль и черный перец. Разогрейте сковороду и вылейте смесь."))

# Добавляем несколько примеров рецептов
db.add_recipe(
    name="Омлет",
    type="завтрак",  # Обратите внимание на запятую после "завтрак"
    image_path="images/omelet.jpg",
    ingredients=["яйца", "молоко", "соль", "черный перец"],
    instructions="Разбейте яйца в чашку, добавьте молоко, соль и черный перец. Разогрейте сковороду и вылейте смесь."
)

# ... (добавьте другие рецепты аналогичным образом)


# Добавляем несколько примеров рецептов
db_connection.execute('''
    INSERT INTO recipes (name, type, image_path, ingredients, instructions)
    VALUES (?, ?, ?, ?, ?)
''', ("Омлет", "завтрак", "images/omelet.jpg", ", ".join(["яйца", "молоко", "соль", "черный перец"]), "Разбейте яйца в чашку, добавьте молоко, соль и черный перец. Разогрейте сковороду и вылейте смесь."))

# ... (добавьте другие рецепты аналогичным образом)
