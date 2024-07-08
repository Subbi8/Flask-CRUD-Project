from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__, template_folder='../FRONTEND/public')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        try:
            title = request.form['title']
            desc = request.form['desc']
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"An error occurred while adding the todo: {e}"

    try:
        allTodo = Todo.query.all()
    except Exception as e:
        return f"An error occurred while fetching todos: {e}"

    return render_template('index.html', allTodo=allTodo)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        try:
            title = request.form['title']
            desc = request.form['desc']
            todo = Todo.query.filter_by(sno=sno).first()
            todo.title = title
            todo.desc = desc
            db.session.add(todo)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            db.session.rollback()
            return f"An error occurred while updating the todo: {e}"

    try:
        todo = Todo.query.filter_by(sno=sno).first()
    except Exception as e:
        return f"An error occurred while fetching the todo: {e}"

    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    try:
        todo = Todo.query.filter_by(sno=sno).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        db.session.rollback()
        return f"An error occurred while deleting the todo: {e}"

if __name__ == "__main__":
    app.run(debug=True)

print(os.path.abspath(app.template_folder))
