class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    def breathe(self):
        print('breathing')
    def move(self):
        print('moving')
    def eat(self):
        print('eating')
class Mammals(Animals):
    def milking(self):
        print('feeding young')
class Giraffes(Mammals):
    def __init__(self, spots):
        self.giraffe_spots = spots
    def left_foot_forward(self):
        print('left foot forward')
    def left_foot_backward(self):
        print('left foot backward')
    def right_foot_forward(self):
        print('right foot forward')
    def right_foot_backward(self):
        print('right foot backward')
    def eat_leaves(self):
        print('eating leaves')
    def found_food(self):
        self.move()
        print('i found food')
        self.eat_leaves()
    def dance(self):
        self.left_foot_forward()
        self.left_foot_backward()
        self.right_foot_forward()
        self.right_foot_backward()
        self.left_foot_backward()
        self.right_foot_backward()
        self.right_foot_forward()
        self.left_foot_forward()
reginald = Giraffes(150)
harold = Giraffes(100)
print(reginald.giraffe_spots)
harold.dance()
reginald.dance()
