from flask import Blueprint, request, render_template, redirect
from . import db
from .models import Todo

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
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

@main.route('/update/<int:sno>', methods=['GET', 'POST'])
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

@main.route('/delete/<int:sno>')
def delete(sno):
    try:
        todo = Todo.query.filter_by(sno=sno).first()
        db.session.delete(todo)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        db.session.rollback()
        return f"An error occurred while deleting the todo: {e}"
