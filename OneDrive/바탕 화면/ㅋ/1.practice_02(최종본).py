class GPA_calculator: #class 생성
    def __init__(self, subject_name): 
        self.subject_name=subject_name

        self.subject_name_list=[] #이름 리스트
        self.score_list=[] #학점 리스트
        self.gpa_list=[] #평점 리스트

        self.units=[] #유닛 리스트

    def add_subject_name(self, subject_name): #과목명 리스트 항목 추가
        self.subject_name_list.append(subject_name)
    
    def add_score(self, score): #학점 리스트 항목 추가
        self.score_list.append(score)
        
    def add_gpa(self, gpa): #평점 리스트 항목 추가
        self.gpa_list.append(gpa)

        
def get_gpa_score(gpa): #평점 문자->숫자 변환 함수
    match gpa:
        case 'A+':
            return 4.5
        case 'A':
            return 4
        case 'B+':
            return 3.5
        case 'B':
            return 3
        case 'C+':
            return 2.5
        case 'C':
            return 2
        case 'D+':
            return 1.5
        case 'D':
            return 1
        case 'F':
            return 0

def get_grade(gpa): #평점 숫자->문자 변환 함수
    match gpa:
        case 4.5:
            return 'A+'
        case 4:
            return 'A'
        case 3.5:
            return 'B+'
        case 3:
            return 'B'
        case 2.5:
            return 'C+'
        case 2:
            return 'C'
        case 1.5:
            return 'D+'
        case 1:
            return 'D'
        case 0:
            return 'F'
        
units = [] #유닛 리스트

x=1
score1=0 #제출 학점
score2=0 #열람 학점
grade1=0 #제출 gpa
grade2=0 #열람 gpa

while x==1:
    print("""작업을 선택하세요.
            1. 입력
            2. 출력
            3. 조회
            4. 계산
            5. 종료""")
            
    x=int(input())

    if x == 1: #입력 기능
        user_input = input("과목명과 학점, 평점을 입력하세요 : ")
        a, b, c = user_input.split(',') #split
        
        unit = GPA_calculator(a) #unit 클래스
        
        unit.add_subject_name(a) #unit을 과목명, 학점, 평점 리스트에 추가
        unit.add_score(int(b))
        unit.add_gpa(get_gpa_score(c))

        if c!="F": #열람, 제출용
            score2+=int(b)
            grade2+=get_gpa_score(c)

            score1+=int(b) #제출 총 학점
            grade1+=get_gpa_score(c) #제출 총 GPA

        else: #열람용
            score2+=int(b) #열람 총 학점
            grade2+=get_gpa_score(c) #열람 총 GPA


            
        units.append(unit) #유닛 리스트 추가

        print("입력되었습니다.")
    
    elif x == 2: #출력 기능
        for unit in units: #unit이 유닛 리스트에 있으면
            for i in range(len(unit.subject_name_list)): #n번 입력한 과목명, 학점, 평점 리스트 원소 출력
                print("[", unit.subject_name_list[i], ']', unit.score_list[i], "학점 : ", unit.gpa_list[i])

        x=1

    elif x == 3: #조회 기능
        subject_name = input("조회할 과목명을 입력하세요: ")

        for unit in units: #unit이 유닛 리스트에 있으면
            if subject_name in unit.subject_name_list: #해당 과목명이 리스트에 있는 경우
                index = unit.subject_name_list.index(subject_name) #과목명의 위치 반환
                print("[", subject_name, ']', unit.score_list[index], "학점 : ", get_grade(unit.gpa_list[index]))
                break

            else: #해당 과목명이 리스트에 없는 경우
                print("해당하는 과목이 없습니다.")

        x=1

    elif x == 4: #계산 기능
        M = sum(unit.score_list[i] * unit.gpa_list[i] for unit in units for i in range(len(unit.subject_name_list)) if unit.gpa_list[i] != 0) / score1
        N = sum(unit.score_list[i] * unit.gpa_list[i] for unit in units for i in range(len(unit.subject_name_list))) / score2
        # sum(학점 * 평점) / sum(학점) 출력 --- 제출학점 : F 학점 제외

        print("제출용 : ", score1, "학점 (GPA : ", round(M,2), ")\n") #제출용 학점, GPA 출력
        print("열람용 : ", score2, "학점 (GPA : ", round(N,2), ")") #열람용 학점, GPA 출력

        x=1

    elif x==5: #종료 기능
        print("프로그램을 종료합니다.")
        break