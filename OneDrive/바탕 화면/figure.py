
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
    __length=0

    def __init__(self, length):
        """
        초기 length 값을 받음.
        """
        self.length=length

    def get_length(self):
        """
        선의 길이 반환
        """
        return self.__length
    
    def set_length(self,length):
        """
        선의 길이 수정
        """
        self.__length=length


    def area_square(self, length):
        """
        길이를 입력받아 정사각형의 넓이를 구하는 함수
        """
        return self.__length*self.__length
    
    def area_circle(self,length):
        """
        길이를 입력받아 원의 넓이를 구하는 함수
        """
        return self.__length*self.__length*math.pi
    
    def area_regular_triangle(self,length):
        """
        길이를 입력받아 정삼각형의 넓이를 구하는 함수
        """
        return self.__length*self.__length*math.sqrt(3)*0.25
    