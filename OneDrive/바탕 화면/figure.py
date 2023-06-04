"""
figure 모듈은 다음과 같은 역할을 수행함.
line class 로 line의 길이를 설정, 참조
area_square, area_circle, area_regular_triangle 함수로 정사각형, 원 정삼각형의 넓이를 계산
"""

import math

class line:
    """
    line 클래스는 line의 길이에 대해 저장한다.
    외부에서 접근 불가능한 __length변수 존재
    __length를 수정하고 접근하기 위해 set_length, get_length 메소드 제공
    """
    __width = 0
    __height=0

    def __init__(self, width, height):
        """
        초기 length 값을 받음.
        초기 width 값을 받음.
        초기 height 값을 받음.
        """
        self.__width=width
        self.__height=height

    def get_length(self):
        """
        선의 길이 반환
        """
        return self.__width, self.__height

    def set_length(self, width, height):
        """
        선의 길이 수정
        """
        self.__width = width
        self.__height = height

    def area_rectangle(width, height):
        if width<=0 or height<=0: raise ValueError
        return width*height
    
    def area_ellipse(width, height):
        if width<=0 or height<=0: raise ValueError
        return width * height * math.pi
    
    def area_right_triangle(width, height):
        if width<=0 or height<=0: raise ValueError
        return (width*height)/2
    