class horse:
    def __init__(self, name, big, color):
        self.name = name
        self.big = big
        self.color = color



class lu:
    def __init__(self, name, big, color):
        self.name = name
        self.big = big
        self.color = color


class luozi:
    def __init__(self,horse, lu):
        self.name = horse.name + lu.name
        self.big = int(horse.big) + int(lu.big)
        self.color = horse.color + lu.color

    def Printing(self):
        print(self.name,"   ",self.big," ",self.color," ")

xx = horse('xx',10, "white")
xxx = lu('xxx',20, "pink")

xxxx = luozi(xx,xxx)

xx.aaa="aaa"
horse.aaa="aaa111"
print(xx.aaa)
# xxxx.Printing()