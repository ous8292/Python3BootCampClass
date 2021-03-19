class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def speak(self):
        print('This your parent speaking')


    # def i_am(self):
    #     print(f'{self.name} {self.level} {self.hp}')



class Npc(Character):
    def __init__(self, name, hp, level, gold):
        super().__init__(name, hp, level)
        self.gold = gold
        # self.name = name
        # self.hp = hp
        # self.level = level

    def speak(self):
        super().speak()
        print('I heard there was a monster around last night!')
        print(self.name)
        print(self.gold)

def make_name():
    return 'Fred'

name = make_name()

#prefered way of doing it, big explicit
x = Npc(name, '1', '1','2000')
x.speak()


# #not explicit
# x = Npc(make_name(), '1', '1','2000')
# x.speak()



# class NPC(Character):
#     def __init__(self, name, hp, level):
#         super().__init__(name,hp,level)
#
#     def speak(self):
#         return "{0} says: 'I heard there was a monster running around last night"



# Jerry = Character('Jerry', '100', '20')
# Jim = Npc('Jim', '1000', '2')
#
# Jerry.i_am()
# print(print('Jerry', '20', '100'))
# print(Jim.speak())