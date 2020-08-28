# the list "students" is already defined

students = [["Will", "B"], ["Kate", "B"], ["Max", "A"], ["Elsa", "C"], ["Alex", "B"], ["Chris", "A"]]

best_students = [student[0] for student in students if student[1] == "A"]

print(best_students)