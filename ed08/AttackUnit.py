class AttackUnit:  # 공격 유닛
    def __init__(self, name, hp, damage):  # 생성자
        self.name = name  # self.name  인스턴스 변수
        self.hp  = hp
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

# 공격 유닛 생성: 화염 방사병 유닛, 5시 방향으로 공격
flamethrower1 = AttackUnit('화염방사병', 50, 16)  # 객체 생성: 체력 50, 공격력 16
flamethrower1.attack("5시")  # 5시 방향으로 공격

# damaged 메서드 호출: flamethrower1 공격하는 중 피해를 받음
flamethrower1.damaged(25)
flamethrower1.damaged(25)