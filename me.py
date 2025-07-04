import sqlite3
connect = sqlite3.connect("step.python.db")
cursor = connect.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    class TEXT
)
''')
connect.commit()


def delete_all_students():
    cursor.execute("DELETE FROM students")
    connect.commit()
    print(" All student records deleted.")


def add_student(name, age, gender, class_name):
    cursor.execute("INSERT INTO students (name, age, gender, class) VALUES (?, ?, ?, ?)",
                   (name, age, gender, class_name))
    connect.commit()


def show_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)


delete_all_students()


add_student("Aarav", 16, "Male", "10A")
add_student("Riya", 15, "Female", "9B")


print(" Student List:")
show_students()


connect.close()
