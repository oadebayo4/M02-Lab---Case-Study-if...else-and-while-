# Olajide Adebayo
# Module 2 Lab - Case Study: if...else and while
# An app that accepts student names and GPAs and tests if the student qualifies for either the Dean's List, the Honor Roll, or neither


HonorRoll = 3.25

DeansList = 3.5
student_records = {'Kelly Fowler' :[90,80,100] , 'Mike Brown' : [70,60,90] , 'Roger Cook' :[80,70,60] , 'Funke Kolade' : [90,70,60] , 'Ben Francis' : [80,90,100]}


def main():
    student_records = []

    while True:
        last_name = input("Enter the student's last name (or ZZZ to quit): ")
        if last_name == 'ZZZ':
            break

        first_name = input("Enter the student's first name: ")

        gpa = float(input("Enter the student's GPA: "))

        Srecord = {'last_name': last_name, 'first_name': first_name, 'gpa': gpa}

        student_records.append(Srecord)

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"Sorry, {first_name} {last_name} has not made the Dean's List or Honor Roll.")

    print("\nStudent Records:")
    for Srecord in student_records:
        print(f"{Srecord['first_name']} {Srecord['last_name']}: {Srecord['gpa']}")


if __name__ == '__main__':
    main()