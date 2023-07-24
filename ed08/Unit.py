class Unit:

    def __init__(self, name, hp, damage):
        # 인스턴스 변수: self.변수명 = 값
        self.name   = name  # 인스턴스 변수 name에 전달값 name 할당
        self.hp     = hp    # 인스턴스 변수 hp에 전달값 hp 할당
        self.damage = damage

        print("{0} 유닛을 생성했습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 객체 생성: 객체명 = 클래스명(전달값1, 전달값2, ...)
soldier1 = Unit("보병", 40, 5)  # 보병1 생성
soldier2 = Unit("보병", 40, 5)  # 보병2 생성
tank     = Unit("탱크", 150, 35)  # 탱크 생성

# 전투기 유닛: 공중 유닛, 은폐 불가
stealth1 = Unit("전투기", 80, 5)  # 체력 80, 공격력 5

# 인스턴스 변수에 접근
print("유닛 이름: {0}, 공격력: {1}".format(stealth1.name, stealth1.damage))

# 은폐 기능
stealth2 = Unit("전투기", 80, 5)

# 업그레이드한 전투기만을 위한 특별한 인스턴스 변수 정의, 은폐 상태
stealth2.cloaking = True

if stealth2.cloaking == True:  # 은폐 상태이면
    print("{0}는 현재 은폐 상태입니다.".format(stealth2.cloaking))

# stealth1에 cloaking 상태 접근
# AttributeError: 'Unit' object has no attribute 'cloaking'
# if stealth1.cloaking == True:
#    print("{0}는 현재 은폐 상태입니다.".format(stealth2.cloaking))
