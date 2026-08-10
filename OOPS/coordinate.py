class Point:
    def __init__(self,x,y):
        self.x_cord = x
        self.y_cord = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cord,self.y_cord)

    def euclidean_distance(self,other):
        return ((self.x_cord-other.x_cord)**2 + (self.y_cord - other.y_cord)**2)**0.5

    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))

class Line:
    def __init__(self,a,b,c):
        self.A = a
        self.B = b
        self.C = c

    def __str__(self):
        return '{}x + {}y + {}z = 0'.format(self.A,self.B,self.C)

    def point_check(self,point):
        if (self.A * point.x_cord + self.B * point.y_cord + self.C == 0):
            print('POINT LIES ON THE LINE')
        else:
            print('POINT DOESNT LIE ON THE LINE') 


p2 = Point(1,1)
l = Line(2,3,4)

l.point_check(p2)

    
