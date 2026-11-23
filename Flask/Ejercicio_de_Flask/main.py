from flask import Flask, request
import data as dt

tasks = dt.read_json()

app = Flask(__name__)

@app.route("/get_task", methods=["GET"])
def get_task():
    filtered_status = tasks
    status_filter = request.args.get("Status")
    if status_filter:
        filtered_status = list(
            filter(lambda show: show["Status"] == status_filter, filtered_status)
        )
    return {"data": filtered_status}, 200

@app.route("/post_task", methods=["POST"])
def post_task():
    request_body = request.get_json()
    
    required_fields = ["ID", "Title", "Description", "Status"]
    for field in required_fields:
        if field not in request_body or not request_body[field]:
            return {"error": f"{field} is required"}, 400
    for task in tasks:
        if task["ID"] == request_body["ID"]:
            return {"error": "Task ID already exists"}, 400
        
    valid_status = ["Pending", "In Progress", "Completed"]
    if request_body["Status"] not in valid_status:
        return {"error": "Invalid Status"}, 400
    tasks.append(request_body)
    dt.save_json(tasks)

    return {"data": tasks}, 200

@app.route("/put_task/<task_id>", methods=["PUT"])
def put_task(task_id):
    request_body = request.json
    for task in tasks:
        if task["ID"] == task_id:
            task.update(request_body)
            return {"data": "Task updated", "data": task}, 200
    return {"error": "Task not found"}, 404

@app.route("/delete_task/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["ID"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}, 200
    return {"error": "Task not found"}, 404

if __name__ == "__main__":
    app.run(host="localhost", debug=True)

