class Person:
    def __init__(self, id, name):
        self.id = id  # 객체의 ID를 설정합니다.
        self.name = name  # 객체의 이름을 설정합니다.

    def printInfo(self):
        # 객체의 정보를 출력합니다.
        print("ID:", self.id)
        print("이름:", self.name)


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)  # 부모 클래스의 생성자를 호출하여 ID와 이름을 설정합니다.
        self.title = title  # 매니저의 직급을 설정합니다.

    def printInfo(self):
        super().printInfo()  # 부모 클래스의 printInfo 메서드를 호출하여 ID와 이름을 출력합니다.
        print("직급:", self.title)  # 매니저의 직급을 출력합니다.


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)  # 부모 클래스의 생성자를 호출하여 ID와 이름을 설정합니다.
        self.skill = skill  # 직원의 기술을 설정합니다.

    def printInfo(self):
        super().printInfo()  # 부모 클래스의 printInfo 메서드를 호출하여 ID와 이름을 출력합니다.
        print("기술:", self.skill)  # 직원의 기술을 출력합니다.


# 테스트 코드
# Person 테스트
person1 = Person(1, "Alice")
person1.printInfo()  # Person 객체의 정보를 출력합니다.
print()

# Manager 테스트
manager1 = Manager(2, "Bob", "Senior Manager")
manager1.printInfo()  # Manager 객체의 정보를 출력합니다.
print()

# Employee 테스트
employee1 = Employee(3, "Charlie", "Python")
employee1.printInfo()  # Employee 객체의 정보를 출력합니다.
print()

# 추가 테스트
manager2 = Manager(4, "David", "Project Manager")
employee2 = Employee(5, "Eve", "Data Analysis")

people = [person1, manager1, employee1, manager2, employee2]

for person in people:
    person.printInfo()  # 모든 객체의 정보를 출력합니다.
    print()
