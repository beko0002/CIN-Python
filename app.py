from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks (use a database for persistence)
tasks = [{"task": "do the dishes", "added": "2019-05-20", "time": None}]

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append({"task": task, "added": "2025-01-14", "time": None})  # Default "time" to None
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["GET"])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

@app.route("/update/<int:task_id>", methods=["POST"])
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        updated_task = request.form.get("task")
        if updated_task:
            tasks[task_id]["task"] = updated_task
    return redirect(url_for("index"))

# New route to set time for a task
@app.route("/set_time/<int:task_id>", methods=["POST"])
def set_task_time(task_id):
    if 0 <= task_id < len(tasks):
        time = request.form.get("time")
        if time:
            tasks[task_id]["time"] = time  # Update the time for the task
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5022)
