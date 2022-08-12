# class josh():
#     course1="core python"
#     course2="adv python programming"
# print(josh.course1)                                  # core python
# print(josh.course2)                                  # adv python programming
# print(josh.course1,josh.course2)                      # core python adv python programming
# p=josh()
# print(p.course1)                                      # core python
# print(p.course2)                                      # adv python programming
# print(p.course1+" "+p.course2)                        # core python adv python programming

class animal:
    livingthing=True

    def eat():
        print("eating")
        
    def sleep():
        print("sleep")   

class goat(animal): 

    def grass():
        print("it's eating grass") 
        
    def herb():
        print("it is harbivorus")    

    def sleep():
        print("don't sleep you are 800Rs kg")

print(goat.livingthing)                         # True  
print(animal.livingthing)                       # true
goat.grass()                                    # it's eating grass
goat.eat()                                      # eating
goat.sleep()                                    # don't sleep you are 800Rs kg
animal.eat()                                    #       eating                                      
animal.sleep()                                   #   sleep

animal.herb()                                #  AttributeError: type object 'animal' has no attribute 'herb'















