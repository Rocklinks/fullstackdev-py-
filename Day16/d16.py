import json

FILE = "students.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_student(name, age, subjects):
    data = load_data()
    data[name] = {"age": age, "subjects": subjects}
    save_data(data)

def update_student(name, age=None, subjects=None):
    data = load_data()
    if name in data:
        if age: data[name]["age"] = age
        if subjects: data[name]["subjects"] = subjects
        save_data(data)

def delete_student(name):
    data = load_data()
    if name in data:
        del data[name]
        save_data(data)

def get_student(name):
    return load_data().get(name, "Student not found")

add_student("Alice", 20, {"Math": "A", "Science": "B"})
print(get_student("Alice"))
delete_student("Alice")

##Task2
import json

# JSON string
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Convert JSON to dictionary
python_dict = json.loads(json_string)

# Modify a key-value pair
python_dict["age"] = 31

# Convert dictionary to JSON string
updated_json_string = json.dumps(python_dict, indent=4) #indent for pretty printing

# Print the updated JSON string
print(updated_json_string)
