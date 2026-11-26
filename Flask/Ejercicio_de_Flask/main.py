from flask import Flask, request
import data as dt

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def get_task():
    tasks = dt.read_json()
    filtered_status = tasks
    status_filter = request.args.get("Status")
    if status_filter:
        filtered_status = list(
            filter(lambda show: show["Status"] == status_filter, filtered_status)
        )
    return {"data": filtered_status}, 200

@app.route("/tasks", methods=["POST"])
def post_task():
    tasks = dt.read_json()
    request_body = request.get_json()
    if not isinstance(request_body, dict):
        return {"error": "Invalid JSON body"}, 400
        
    required_fields = ["ID", "Title", "Description", "Status"]
    for field in required_fields:
        if field not in request_body or request_body[field] is None or str(request_body[field]).strip() == "":
            return {"error": f"{field} is required"}, 400

    request_body["ID"] = str(request_body["ID"])        
    for task in tasks:
        if str(task["ID"]) == request_body["ID"]:
            return {"error": "Task ID already exists"}, 400
        
    valid_status = ["Pending", "In Progress", "Completed"]
    if request_body["Status"] not in valid_status:
        return {"error": "Invalid Status"}, 400
    tasks.append(request_body)
    dt.save_json(tasks)

    return {"data": request_body}, 201

@app.route("/tasks/<task_id>", methods=["PUT"])
def put_task(task_id):
    tasks = dt.read_json()
    request_body = request.get_json()
    if not isinstance(request_body, dict):
        return {"error": "Invalid JSON body"}, 400

    for task in tasks:
        if str(task["ID"]) == str(task_id):
            required_fields = ["Title", "Description", "Status"]
            for field in required_fields:
                if field not in request_body or request_body[field] is None or str(request_body[field]).strip() == "":
                    return {"error": f"{field} is required"}, 400

            valid_status = ["Pending", "In Progress", "Completed"]
            if request_body["Status"] not in valid_status:
                return {"error": "Invalid Status"}, 400
            
            task["Title"] = request_body["Title"]
            task["Description"] = request_body["Description"]
            task["Status"] = request_body["Status"]
            
            dt.save_json(tasks)
            return {"message": "Task updated", "data": task}, 200
    return {"error": "Task not found"}, 404

@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = dt.read_json()
    for task in tasks:
        if str(task["ID"]) == str(task_id):
            tasks.remove(task)
            dt.save_json(tasks)
            return {"message": "Task deleted"}, 200
    
    return {"error": "Task not found"}, 404

if __name__ == "__main__":
    app.run(host="localhost", debug=True)

