# List to store courses
courses = []

# Functions
def register_course():
    title = input("Course title: ")
    duration = int(input("Duration (hours): "))
    enrolled = int(input("Number of enrolled students: "))
    course = {"title": title, "duration": duration, "enrolled": enrolled}
    courses.append(course)
    print("Course successfully registered.\n")

def update_enrollment():
    title = input("Title of the course to update: ")
    for course in courses:
        if course["title"].lower() == title.lower():
            new_enrollment = int(input("New number of enrolled students: "))
            course["enrolled"] = new_enrollment
            print("Enrollment updated.\n")
            return
    print("Course not found.\n")

def filter_by_min_duration():
    min_duration = int(input("Minimum duration (hours): "))
    filtered = [c for c in courses if c["duration"] >= min_duration]
    print(f"\nCourses with at least {min_duration} hours:")
    if filtered:
        for course in filtered:
            print(f"- {course['title']} ({course['duration']}h, {course['enrolled']} enrolled)")
    else:
        print("No courses found with that minimum duration.")
    print()

def show_menu():
    print("=== Online Course Management ===")
    print("1. Register a course")
    print("2. Update enrollment")
    print("3. Filter by minimum duration")
    print("4. Exit")

# Main loop
while True:
    show_menu()
    option = input("Select an option (1-4): ")

    if option == "1":
        register_course()
    elif option == "2":
        update_enrollment()
    elif option == "3":
        filter_by_min_duration()
    elif option == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.\n")