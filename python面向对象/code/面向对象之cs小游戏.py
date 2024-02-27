"""

使用面向对象的方法来简单实现一个cs小游戏
有2个类 一个警察 一个 匪徒
警察
    队员血量200
    队长血量300
匪徒
    血量300
警察可以炸 匪徒 直接掉200血
他们都可以看自己的血量  都可以射击 每次射击 扣除对面5滴血 可以扫射 扫射 10点血

"""


class People:
    def __init__(self, name):
        self.HP = 0
        self.name = name

    def show_hp(self):
        print("{}的血量为{}".format(self.name, self.HP))

    def shoot(self, people):
        people.HP -= 5
        people.show_hp()

    def strafe(self, people_list):
        for people in people_list:
            people.HP -= 10
            people.show_hp()
            if people.HP <= 0:
                print("{} is dead".format(people))
            else:
                pass


class Police(People):
    def __init__(self, name, role):
        super().__init__(name)
        self.name = name
        if role == "队员":
            self.HP = 200
        else:
            self.HP = 300

    def bomb(self, bandits):
        for bandit in bandits:
            bandit.HP -= 200
            bandit.show_hp()


class Bandit(People):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.HP = 300


if __name__ == "__main__":
    p1 = Police("xxx", "队员")
    p2 = Police("zzz", "队员")
    p3 = Police("ccc", "队长")

    b1 = Bandit("xsaxa")
    b2 = Bandit("dasdasd")
    print("".center(20, "*"))
    p1.shoot(b2)
    p1.bomb([b2])
    print("{}炸了{} 、{}、 {}".format(b1.name, p1.name, p2.name, p3.name))
    b2.strafe([p1, p2, p3])
