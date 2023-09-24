class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.sums = 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.Lgrades:
                lecturer.Lgrades[course] += [grade]
            else:
                lecturer.Lgrades[course] = [grade]
        else:
            return 'Ошибка'

    def Agrades(self):
        for i in self.grades:
            self.sums =+ sum(self.grades[i])/len(self.grades[i])
        return self.sums

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{self.Agrades()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент')
            return
        return self.sums < other.sums




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.Lgrades = {}
        self.sums = 0

    def Agrades(self):
        for i in self.Lgrades:
            self.sums =+ sum(self.Lgrades[i])/len(self.Lgrades[i])
        return self.sums


class Lecturer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.Agrades()}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор')
            return
        return self.sums < other.sums


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['C++']

bad_student = Student('Sanya', 'Kot', 'your_gender')
bad_student.courses_in_progress += ['Python']
bad_student.finished_courses += ['C++']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

bad_lecturer = Lecturer('Who', 'What')
bad_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Rev', 'Iewer')
cool_reviewer.courses_attached += ['Python']

bad_reviewer = Reviewer('Alex', 'Kotls')

best_student.rate_lecturer(cool_lecturer, 'Python', 5)
best_student.rate_lecturer(cool_lecturer, 'Python', 6)
best_student.rate_lecturer(cool_lecturer, 'Python', 1)

best_student.rate_lecturer(bad_lecturer, 'Python', 3)
best_student.rate_lecturer(bad_lecturer, 'Python', 2)
best_student.rate_lecturer(bad_lecturer, 'Python', 1)

cool_reviewer.rate_hw(best_student, 'Python', 4)
cool_reviewer.rate_hw(best_student, 'Python', 3)

cool_reviewer.rate_hw(bad_student, 'Python', 2)
cool_reviewer.rate_hw(bad_student, 'Python', 7)


# print(cool_reviewer)
# print(cool_lecturer)
# print(best_student)
# print(bad_student)
# print(best_student > bad_student)
# print(bad_lecturer)
# print(bad_lecturer > cool_lecturer)

def avg_course_grade(Slist, Course):
    ACG = 0
    leng = 0
    for student in Slist:
        ACG = ACG + sum(student.grades[Course])
        leng = leng + len(student.grades[Course])
    return ACG / leng

def avg_lect_grade(Llist, Course):
    ACG = 0
    leng = 0
    for lecturer in Llist:
        ACG = ACG + sum(lecturer.Lgrades[Course])
        leng = leng + len(lecturer.Lgrades[Course])
    return ACG / leng




print(avg_course_grade([best_student, bad_student], 'Python'))
print(avg_lect_grade([cool_lecturer, bad_lecturer], 'Python'))
