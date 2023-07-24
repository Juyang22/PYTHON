'''
https://docs.python.org/ko/3/reference
'''


class Unit:
    def __init__(self):
        print('Unit 생성자')

class Flyable:
    def __init__(self):
        print('Flyable 생성자')

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()  # Unit 생성자 -> 순서상 가장 먼저 상속받은 클래스에 접근
                            # 다중 상속 시 각 부모 클래스의 이름을 명시해서 접근하는 것을 추천

        Unit.__init__(self)     # Unit 생성자
        Flyable.__init__(self)  # Flyable 생성자

troopship = FlyableUnit()