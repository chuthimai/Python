# PY04010 - LỚP THÍ SINH - 1

class Student:
    def __init__(self, name, birth_date: str, p1, p2, p3):
        self.name = name
        self.birth_date = birth_date
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def sum_point(self):
        return self.p1 + self.p2 + self.p3
    def process_date(self):
        date = self.birth_date.split('/')
        if len(date[0]) < 2:
            date[0] = '0'+date[0]
        if len(date[1]) < 2:
            date[1] = '0'+date[1]
        return f"{date[0]}/{date[1]}/{date[2]}"
    def __repr__(self):
        return f"{self.name} {self.process_date()} {self.sum_point():.1f}"

name = input()
date = input()
p1 = float(input())
p2 = float(input())
p3 = float(input())
student = Student(name, date, p1, p2, p3)
print(student)
