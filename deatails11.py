# student_details.py
# Program to print student details

def print_student_details():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    usn = input("Enter student USN: ")
    address = input("Enter student address: ")

    print("\n--- Student Details ---")
    print("Name:", name)
    print("Age:", age)
    print("USN:", usn)
    print("Address:", address)

# Call the function
print_student_details()
