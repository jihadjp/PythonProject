class Student:
    total_students = 0

    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects  # dict: {"Math": 85, "English": 72}
        Student.total_students += 1

    def average(self):
        return sum(self.subjects.values()) / len(self.subjects)

    def grade(self):
        avg = self.average()
        if avg >= 80:
            return "A+"
        elif avg >= 70:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        return "F"

    def best_subject(self):
        return max(self.subjects, key=lambda k: self.subjects[k])

    def report(self):
        print("-" * 30)
        print(f"নাম: {self.name} | বয়স: {self.age}")
        for sub, mark in self.subjects.items():
            bar = "█" * (mark // 10)
            print(f" {sub:10}: {mark:3} {bar}")
        print(f"গড়: {self.average():.1f} | গ্রেড: {self.grade()}")
        print(f"সেরা বিষয়: {self.best_subject()}")


students = [
    Student("Rahim", 20, {"Math": 85, "English": 78, "Science": 92}),
    Student("Karim", 19, {"Math": 55, "English": 60, "Science": 48}),
    Student("Nusrat", 21, {"Math": 95, "English": 88, "Science": 91}),
]

print("STUDENT REPORT CARD")
for s in students:
    s.report()

top = max(students, key=lambda s: s.average())
print(f"\nসেরা ছাত্র: {top.name} ({top.average():.1f})")
print(f"মোট ছাত্র: {Student.total_students}")