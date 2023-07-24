'''
https://docs.python.org/ko/3/reference
'''


class Unit:

    def __init__(self, name, hp, speed):  # speed 추가
        # 인스턴스 변수: self.변수명 = 값
        self.name = name  # 인스턴스 변수 name에 전달값 name 할당
        self.hp   = hp    # 인스턴스 변수 hp에 전달값 hp 할당
        self.speed = speed  # 지상 이동 속도

    def move(self, location):  # 이동 동작 정의
        print('[지상 유닛 이동]')
        # {누가} {어떤} 방향으로 이동합니다. [속도: {}]
        print('{0}: {1} 방향으로 이동합니다. [속도: {2}]'.format(self.name, location, self.speed))


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


# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass  # 미완성이지만 프로그램은 정상적으로 동작


supply_depot = BuildingUnit("보급고", 500, "7시")