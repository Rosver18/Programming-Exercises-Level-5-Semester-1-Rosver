import json

def write_to_json(stdnt_details):
    with open('StudentJson.json', 'w') as file:
        json.dump(stdnt_details, file)

def read_from_json():
    with open('StudentJson.json', 'r') as file:
        stdnt_details = json.load(file)
    return stdnt_details

name = input("Enter student name: ")
stdnt_id = int(input("Enter student ID: "))
course = input("Enter student course: ")

student_details = {
    "Name": name,
    "ID": stdnt_id,
    "Course": course
}

write_to_json(student_details)

loaded_stdnt_details = read_from_json()

print("Details of the Student are")
for key, value in loaded_stdnt_details.items():
    print(f"\t{key}: {value}")

group = input("Enter course group: ")
course_year = int(input("Enter course year (Only Numbers): "))

loaded_stdnt_details["CourseDetails"] = {
    "Group": group,
    "Year": course_year
}

write_to_json(loaded_stdnt_details)

print("Details of the Student are:")
for key, value in loaded_stdnt_details.items():
    print(f"\t{key}: {value}")
