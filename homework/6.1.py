class Student(Person):
    def __init__(self, name='', age=30, sex='unknown', major='Computer'):
        super(Student, self).__init__(name, age, sex)
        self.SetMajor(major)

    def SetMajor(self, major):
        if not isinstance(major, str):
            print("Major must be a string.")
            return
        self.__major = major

    def Show(self):
        super(Student, self).Show()
        print(self.__major)
