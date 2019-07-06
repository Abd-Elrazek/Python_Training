
class Parent():
    def __init__(self, last_name, eye_color):
        print ("parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print ("child constructor called")
        Parent.__init__(self, last_name, eye_color)


miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.eye_color)