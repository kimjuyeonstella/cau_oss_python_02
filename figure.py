import math

class Line:
    """
    Line 클래스는 선의 길이를 나타내며, 길이에 대한 설정 및 접근 메서드를 포함합니다.
    length는 기본적으로 1로 설정되며, int 또는 float 타입으로만 설정될 수 있습니다.
    0 이하의 값은 설정될 수 없으며, 잘못된 값이 주어지면 기본 값 1로 설정됩니다.
    """
    
    def __init__(self, length=1):
        if isinstance(length, (int, float)) and length > 0:
            self.__length = length
        else:
            self.__length = 1

    def set_length(self, length):
        """
        length 값을 설정합니다. int 또는 float 타입의 양수만 설정될 수 있습니다.
        """
        if isinstance(length, (int, float)) and length > 0:
            self.__length = length

    def get_length(self):
        """
        현재 length 값을 반환합니다.
        """
        return self.__length

def area_square(line):
    """
    길이를 입력받아 정사각형의 넓이를 계산합니다.
    Line 객체가 아닌 경우 0을 반환합니다.
    """
    if isinstance(line, Line):
        length = line.get_length()
        return length ** 2
    return 0

def area_circle(line):
    """
    주어진 Line 객체의 길이를 사용하여 원의 넓이를 계산합니다.
    Line 객체가 아닌 경우 0을 반환합니다.
    """
    if isinstance(line, Line):
        length = line.get_length()
        return length ** 2 * math.pi
    return 0

def area_regular_triangle(line):
    """
    주어진 Line 객체의 길이를 사용하여 정삼각형의 넓이를 계산합니다.
    Line 객체가 아닌 경우 0을 반환합니다.
    """
    if isinstance(line, Line):
        length = line.get_length()
        return (math.sqrt(3) / 4) * length ** 2
    return 0