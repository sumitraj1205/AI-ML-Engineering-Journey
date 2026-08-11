class emplyoee:
    def work(self):
        print("work = employee")
class teacher(emplyoee):
    def work(self):
        print("work = teacher")
a = teacher()
a.work()