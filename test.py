class Role:
    def __init__(self, name):
        self.name = name

    def attack(self):
        return 0


class Magicer(Role):
    def __init__(self, name, level):
        super().__init__(name)
        if 1 <= level <= 10:
            self.level = level
        else:
            self.level = 1

    def attack(self):
        return self.level * 5


class Soldier(Role):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def attack(self):
        return self.damage


class Team:
    def __init__(self, member=None):
        if member is None:
            member = []
        self.member = member

    def addMember(self, member):
        if len(self.member) <= 6:
            self.member.append(member)
        else:
            print("小队成员已达上限")

    def attackSum(self):
        sum = 0
        for i in self.member:
            sum += i.attack()
        return sum


song = Magicer("asd",5)
liu = Magicer("asd",7)
li = Soldier("asd",5)
xx = Soldier("asd",8)
team = Team()
team.addMember(song)
print(team.attackSum())
team.addMember(liu)
print(team.attackSum())
team.addMember(li)
print(team.attackSum())
team.addMember(xx)
print(team.attackSum())

