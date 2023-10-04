'''5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов
и методов
    - как минимум один атрибут должен быть с уровнем доступа private.
    Соответственно, для получения значений этого атрибута  нужно использовать методы get и set
5.2. Создайте репозиторий на Github и отправьте файл с домашним заданием в этот
 удаленный репозиторий
'''


class Students:
    def __init__(self, name, surname, course, age):
        self.name = name
        self.surname = surname
        self.course = course
        self.__age = age

    def full_name(self):
        return f"{self.name} {self.surname}"

    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age

    def get_age(self):
        return self.__age


class Students_med(Students):

    def __init__(self, name, surname, course, age, qualification):
        super().__init__(name, surname, course, age)
        self.qualification = qualification


student_1 = Students("Mary", "Hat", 2, 25)
student_2 = Students_med('Jack', 'Stuard', 3, 21, 'radiology')

print(student_2.full_name())
print(student_1.get_age())
student_1.set_age(20)
print(student_1.get_age())