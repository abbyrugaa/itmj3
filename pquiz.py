#My Custom Quiz App

from fastapi import FastAPI
import pymysql

app = FastAPI()

def get_db_connection():
    return pymysql.connect(host='localhost', 
                           user='root', 
                           password='', 
                           db='pquiz_db', 
                           port='3306',
                           cursorclass=pymysql.cursors.DictCursor)

#  Quizzes CRUD

# Create a quiz
@app.post("/quizzes/")
def create_quiz(title: str, description: str = None):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO quizzes (title, description) VALUES (%s, %s)", (title, description))
            connection.commit()
        return {"message": "Quiz created successfully"}
    finally:
        connection.close()

# Get all quizzes
@app.get("/quizzes/")
def get_quizzes():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM quizzes")
            quizzes = cursor.fetchall()
        return quizzes
    finally:
        connection.close()

# Update a quiz
@app.put("/quizzes/{quiz_id}")
def update_quiz(quiz_id: int, title: str, description: str = None):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE quizzes SET title = %s, description = %s WHERE id = %s", (title, description, quiz_id))
            connection.commit()
        return {"message": "Quiz updated successfully"}
    finally:
        connection.close()

# Delete a quiz
@app.delete("/quizzes/{quiz_id}")
def delete_quiz(quiz_id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM quizzes WHERE id = %s", (quiz_id,))
            connection.commit()
        return {"message": "Quiz deleted successfully"}
    finally:
        connection.close()

# Questions CRUD 

# Add a question to a quiz
@app.post("/quizzes/{quiz_id}/questions/")
def add_question(quiz_id: int, question_text: str, choices: str, correct_answer: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO questions (quiz_id, question_text, choices, correct_answer) VALUES (%s, %s, %s, %s)", 
                           (quiz_id, question_text, choices, correct_answer))
            connection.commit()
        return {"message": "Question added to quiz"}
    finally:
        connection.close()

# Get all questions for a quiz
@app.get("/quizzes/{quiz_id}/questions/")
def get_questions(quiz_id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM questions WHERE quiz_id = %s", (quiz_id,))
            questions = cursor.fetchall()
        return questions
    finally:
        connection.close()

# Update a question
@app.put("/questions/{question_id}")
def update_question(question_id: int, question_text: str, choices: str, correct_answer: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE questions SET question_text = %s, choices = %s, correct_answer = %s WHERE id = %s", 
                           (question_text, choices, correct_answer, question_id))
            connection.commit()
        return {"message": "Question updated successfully"}
    finally:
        connection.close()

# Delete a question
@app.delete("/questions/{question_id}")
def delete_question(question_id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM questions WHERE id = %s", (question_id,))
            connection.commit()
        return {"message": "Question deleted successfully"}
    finally:
        connection.close()

# Attempts CRUD 

# Record a quiz attempt
@app.post("/attempts/")
def create_attempt(quiz_id: int, user_id: int, answers: str):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO attempts (quiz_id, user_id, answers) VALUES (%s, %s, %s)", 
                           (quiz_id, user_id, answers))
            connection.commit()
        return {"message": "Attempt recorded"}
    finally:
        connection.close()

# Get details of a specific attempt
@app.get("/attempts/{attempt_id}")
def get_attempt(attempt_id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM attempts WHERE id = %s", (attempt_id,))
            attempt = cursor.fetchone()
        return attempt if attempt else {"message": "Attempt not found"}
    finally:
        connection.close()

#Categories CRUD

# Create category
@app.post("/categories/")
def create_category(category_name: str, description: str = None):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO categories (category_name, description) VALUES (%s, %s)", 
                           (category_name, description))
            connection.commit()
        return {"message": "Category created successfully"}
    finally:
        connection.close()

# Get all categories
@app.get("/categories/")
def get_categories():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM categories")
            categories = cursor.fetchall()
        return categories
    finally:
        connection.close()

# Update category
@app.put("/categories/{category_id}")
def update_category(category_id: int, category_name: str, description: str = None):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE categories SET category_name = %s, description = %s WHERE id = %s", 
                           (category_name, description, category_id))
            connection.commit()
        return {"message": "Category updated successfully"}
    finally:
        connection.close()

# Delete category
@app.delete("/categories/{category_id}")
def delete_category(category_id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM categories WHERE id = %s", (category_id,))
            connection.commit()
        return {"message": "Category deleted successfully"}
    finally:
        connection.close()

#Levels CRUD

# Create level
@app.post("/levels/")
def create_level(level_name: str, description: str = None):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO levels (level_name, description) VALUES (%s, %s)", 
                           (level_name, description))
            connection.commit()
        return {"message": "Level created successfully"}
    finally:
        connection.close()

# Get all levels
@app.get("/levels/")
def get_levels():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM levels")
            levels = cursor.fetchall()
        return levels
    finally:
        connection.close()

# Update level
@app.put("/levels/{level_id}")
def update_level(level_id: int, level_name: str, description: str = None):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE levels SET level_name = %s, description = %s WHERE id = %s", 
                           (level_name, description, level_id))
            connection.commit()
        return {"message": "Level updated successfully"}
    finally:
        connection.close()

# Delete level
@app.delete("/levels/{level_id}")
def delete_level(level_id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM levels WHERE id = %s", (level_id,))
            connection.commit()
        return {"message": "Level deleted successfully"}
    finally:
        connection.close()

#Topics CRUD

# Create topic
@app.post("/topics/")
def create_topic(topic_name: str, description: str = None):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO topics (topic_name, description) VALUES (%s, %s)", 
                           (topic_name, description))
            connection.commit()
        return {"message": "Topic created successfully"}
    finally:
        connection.close()

# Get all topics
@app.get("/topics/")
def get_topics():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM topics")
            topics = cursor.fetchall()
        return topics
    finally:
        connection.close()

# Update topic
@app.put("/topics/{topic_id}")
def update_topic(topic_id: int, topic_name: str, description: str = None):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE topics SET topic_name = %s, description = %s WHERE id = %s", 
                           (topic_name, description, topic_id))
            connection.commit()
        return {"message": "Topic updated successfully"}
    finally:
        connection.close()

# Delete topic
@app.delete("/topics/{topic_id}")
def delete_topic(topic_id: int):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM topics WHERE id = %s", (topic_id,))
            connection.commit()
        return {"message": "Topic deleted successfully"}
    finally:
        connection.close()
