from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps  # For the login_required
import os
print("Current working directory:", os.getcwd())

app = Flask(__name__, template_folder="../templates")

app.secret_key = 'your_secret_key'  # Required for session handling

USER_CREDENTIALS = {
    'username': 'admin',
    'password': 'password123'
}

tasks = [{"task": "do the dishes", "added": "2019-05-20", "time": None}]

# Decorator to enforce login
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:  # Check if user is logged in
            return redirect(url_for('login'))  # Redirect to login page
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def home():
    return render_template('index.html', username=session['username'], tasks=tasks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate credentials
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['username'] = username  # Store username in session
            return redirect(url_for('home'))  # Redirect to home
        else:
            return "Invalid credentials, please try again."

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove user from session
    return redirect(url_for('login'))  # Redirect to login page

@app.route("/add", methods=["POST"])
@login_required
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append({"task": task, "added": "2025-01-14", "time": None})  # Default "time" to None
    return redirect(url_for("home"))

@app.route("/delete/<int:task_id>", methods=["GET"])
@login_required
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("home"))

@app.route("/update/<int:task_id>", methods=["POST"])
@login_required
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        updated_task = request.form.get("task")
        if updated_task:
            tasks[task_id]["task"] = updated_task
    return redirect(url_for("home"))

@app.route("/set_time/<int:task_id>", methods=["POST"])
@login_required
def set_task_time(task_id):
    if 0 <= task_id < len(tasks):
        time = request.form.get("time")
        if time:
            tasks[task_id]["time"] = time  # Update the time for the task
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
