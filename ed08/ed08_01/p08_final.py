'''
https://docs.python.org/ko/3/reference
'''


class Unit:
    def __init__(self, name, hp, speed):  # speed 추가
        # 인스턴스 변수: self.변수명 = 값
        self.name = name  # 인스턴스 변수 name에 전달값 name 할당
        self.hp   = hp    # 인스턴스 변수 hp에 전달값 hp 할당
        self.speed = speed  # 지상 이동 속도
        # $1 안내 문구 출력
        # {} 유닛을 생성했습니다.
        print('{0} 유닛을 생성했습니다.'.format(name))

    def move(self, location):  # 이동 동작 정의
        # $2 출력문 삭제
        # print('[지상 유닛 이동]')
        # {누가} {어떤} 방향으로 이동합니다. [속도: {}]
        print('{0}: {1} 방향으로 이동합니다. [속도: {2}]'.format(self.name, location, self.speed))

    # $3
    # 메서드: 첫 번째 인자는 self
    def damaged(self, damage):  # damage만큼 유닛 피해
        # 피해 정보
        # 남은 체력 출력
        # 남은 체력이 0 이하면 파괴
        print('{0}: {1}만큼 피해를 입었습니다.'.format(self.name, damage))

        # 유닛의 체력에서 전달받은 damage만큼 감소
        self.hp -= damage
        print('{0}: 현재 체력은 {1}입니다.'.format(self.name, self.hp))

        if self.hp <= 0:  # 남은 체력이 0 이하면
            print('{0}: 파괴되었습니다.'.format(self.name))  # 유닛 파괴 처리

class AttackUnit(Unit):  # 공격 유닛 -> Unit 상속받음
    def __init__(self, name, hp, damage, speed):  # 생성자에 speed 추가
        # 부모 클래스의 생성자 호출
        Unit.__init__(self, name, hp, speed)  # 부모 생성자 호출 시 speed 추가
        self.damage = damage

    # 메서드: 첫 번째 인자는 self
    def attack(self, location):  # 전달 받은 방향으로 공격
        # \ : 공간이 좁아 두 줄로 표시
        print('{0}: {1} 방향 적군을 공격[공격력: {2}]'\
              .format(self.name, location, self.damage))
    ''' $4 여러 줄 comment
    def damaged(self, damage):  # damage만큼 유닛 피해
    # 피해 정보
    # 남은 체력 출력
    # 남은 체력이 0 이하면 파괴
    print('{0}: {1}만큼 피해를 입었습니다.'.format(self.name, damage))

    # 유닛의 체력에서 전달받은 damage만큼 감소
    self.hp -= damage
    print('{0}: 현재 체력은 {1}입니다.'.format(self.name, self.hp))

    if self.hp <= 0:  # 남은 체력이 0 이하면
        print('{0}: 파괴되었습니다.'.format(self.name))  # 유닛 파괴 처리
    '''


# 탱크 유닛
class Tank(AttackUnit):
    # 클래스 변수: 클래스명 밑에 정의, 클래스로부터 만들어진 모든 객체에 값이 일괄 적용
    # 시즈 모드: 탱크를 지상에 고정, 이동 불가, 공격력 증가
    siege_developed = False  # 시즈 모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1)  # 이름, 체력, 공격력, 이동 속도
        self.siege_mode = False  # 시즈 모드(해지 상태) 인스턴스 변수로 정의

    # 시즈 모드 설정
    def set_siege_mode(self):
        # 시즈 모드가 개발되어 있지 않으면 바로 return
        if Tank.siege_developed == False:  # 클래스 변수: 클래스명.클래스 변수
            return

        # 현재 일반 모드 -> 시즈 모드로 전환
        if self.siege_mode == False:
            print('{0}: 시즈 모드로 전환합니다.'.format(self.name))

            # 공격력 2배 증가
            self.damage *= 2

            # 시즈 모드 설정
            self.siege_mode = True

        # 시즈 모드일 때 -> siege_mode = False
        else:
            print('{0}: 시즈 모드를 해제합니다.'.format(self.name))
            # 공격력 절반으로 감소
            self.damage //= 2

            # 시즈 모드 해제
            self.siege_mode = False


# 보병 유닛
class Soldier(AttackUnit):
    # 생성자
    def __init__(self):
        #(self, name, hp, damage, speed)
        #       이름, 체력, 공격력, 이동 속도
        AttackUnit.__init__(self, "보병", 40, 5, 1)

    # 강화제: 일정 시간 동안 속도 및 공격력 증가, 체력 10 감소
    def booster(self):
        if self.hp > 10:
            self.hp -= 10  # 체력 10만큼 감소
            # {} 강화제를 사용 -> HP 10 감소
            print('{0} 강화제를 사용합니다. (HP 10 감소)'.format(self.name))
        else:
            #{} 체력이 부족하여 강화제를 사용할 수 없습니다.
            print('{0} 체력이 부족하여 강화제를 사용할 수 없습니다.'.format(self.name))


# 공중 Unit : 비행 가능
class Flyable:
    def __init__(self, flying_speed):  # 비행 속도
        self.flying_speed = flying_speed

    def fly(self, name, location):  # 유닛 이름, 비행 방향
        print('{0}: {1} 방향으로 날아갑니다. [속도: {2}]'.format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    # 유닛 이름, 체력, 공격력, 비행 속도
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)  # 유닛 이름, 체력, 공격력
        Flyable.__init__(self, flying_speed)  # 비행 속도

    def move(self, location):  # Unit에 있는 move 메서드를 오버라이딩
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 전투기 유닛
class Stealth(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "전투기", 80, 20, 5)
        self.cloaked = False  # 은폐 모드(해제 상태), 인스턴스 변수

    # 은폐 모드 정의 메서드
    def cloaking(self):

        # 은폐 모드 정의 메서드
        def cloaking(self):

            # 현재 은폐 모드일 때 -> 은폐 모드 해제
            if self.cloaked == True:
                print('{0}: 은폐 모드를 해제합니다.'.format(self.name))
                self.cloaked = False
            else:
                print('{0} : 은폐 모드를 설정합니다.'.format(self.name))
                self.cloaked = True


# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)  # 지상 건물 속도: 0, 건물은 지상 이동 불가\
        super().__init__(name, hp, 0)  # 클래스 이름 대신 super() 키워드 사용, self 생략 가능
        self.location = location  # location 인스턴스 변수 생성

supply_depot = BuildingUnit("보급고", 500, "7시")


# 게임 시작
def game_start():
    print('[알림] 새로운 게임을 시작합니다.')


# 게임 종료
def game_over():
    print('Player : Good Game')
    print('[Player] 님이 게임에서 퇴장했습니다.')

'''
<게임 실행하기>
    -> 게임 시작부터 종료까지 수행 시나리오
    1. 게임 시작
    2. 유닛 생성(보병 3, 탱크 2, 전투기 1)
    3. 전군 1시 방향으로 이동
    4. 탱크 시즈 모드 개발
    5. 공격 준비(보병 강화제, 탱크 시즈 모드, 전투기 은폐 모드)
    6. 전군 1시 방향 공격
    7. 전군 피해
    8. 게임 종료
'''

def main():
    pass


main()