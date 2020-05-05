import math

class Point:

    def __init__(self, x, y):
        try:
            self.__x = int(x)
            self.__y = int(y)
        except:
            raise Exception("The point is not an int")

    def __str__(self):
        return '({:d},{:d})'.format(self.__x, self.__y)
    
    @staticmethod
    def validate(other):
        if type(other) == Point:
            return other
        else:
            raise TypeError('Type must be Point, not '
                + str(type(other)))

    def __eq__(self, other):
        other = self.validate(other)
        return self.__x == other.__y and self.__y == other.__x

    def __sub__(self, other):
        other = self.validate(other)
        d = math.sqrt((self.__x - other.__x)**2 + (self.__y - other.__y)**2)
        return d

def main():

    p1 = Point(1, 4)
    p2 = Point(5, 1)
    print('p1 is', p1)
    print('p2 is', p2)
    if p1 == p2:
        print('The two points ARE equal')
    else:
        print('The two points are NOT equal')
    print('p1 - p2 is', p1 - p2)
    print('p2 - p1 is', p2 - p1)

    print('')
    
    p3 = Point(-2, 1)
    p4 = Point(2, -2)
    print('p3 is', p3)
    print('p4 is', p4)
    if p3 == p4:
        print('The two points ARE equal')
    else:
        print('The two points are NOT equal')
    print('p3 - p4 is', p3 - p4)
    print('p4 - p3 is', p4 - p3)

    print('')

    p5 = Point(5, 5)
    p6 = Point(5, 5)
    print('p5 is', p5)
    print('p5 is', p6)
    if p5 == p6:
        print('The two points ARE equal')
    else:
        print('The two points are NOT equal')
    print('p5 - p6 is', p5 - p6)
    print('p6 - p5 is', p6 - p5)

    #p3 = Point(1, 'abc')
    #x = p1-3
    #p1 == 3.3
        
main()
