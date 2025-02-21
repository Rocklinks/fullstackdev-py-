import json
records = {
            "name": "Rajesh ",
            "age": 16,
            "subjects": "English, Maths. Science ",
            "grades": "A, A,B"
}

def wdata(records):
    with open('temp.json','w') as file:
    json.dump(records,file,indent=4)

def rdata(records):
    try:
        with open('temp.json','r') as file:
            return json.load(file)
            print(info)
    except FileNotFoundError as e:
        print(f"Error {e}")

    except json.JSONDecodeError as e:
        print(e)
