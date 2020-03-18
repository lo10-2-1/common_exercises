import random as rnd

def main():
    bear = Bear()
    fish = Fish()
    river = Ecosystem(20)
    river.fill_ecosys(bear, fish, river)
    print(river, end='')
    for i in range(6):
        river = river.fill_ecosys(bear, fish, river)
        if bear == fish in river:
            bear.eating(bear, fish, river)
        elif bear == bear in river:
            if bear.gender == bear.gender:
                bear.fighting(river)
            else:
                bear.mating(river)
        elif fish == fish in river:
            if fish.gender == fish.gender:
                fish.fighting(river)
            else:
                fish.mating(river)
        print(*river, end='')


class Ecosystem():
    '''List of objects of Bears, Fish and None.
    Move objects in itself.
    Creation consists of filling list with objects and then shuffling them.
    '''
    class_instances = []
    
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.class_instances = [0] * self.max_capacity

    def fill_ecosys(self, obj1, obj2, obj_eco:list):
        '''Fills ecosystem with objects (animals) of two different types and None.
        Returns shuffled list.
        '''
        third = len(self.class_instances)//3
        for i in range(third + 1):
            self.class_instances[i] = None
        for j in range(third, (third*2)+1):
            self.class_instances[j] = obj1
        for k in range(third*2, len(self.class_instances)):
            self.class_instances[k] = obj2
        return rnd.shuffle(self.class_instances)

    def move_ecosys(self, class_instances:list):
        '''Moves ecosystem one step further. 
        All objects randomly move into adjacent list location or stay still.
        Returns list with all moves done
        '''
        for i in range(len(class_instances)):
            self.class_instances[i] = self.class_instances[rnd.randint(i-1, i+1)]
    
    # def __iter__(self):
    #     return self


class Animals():
    def __init__(self):
        self.gender = rnd.choice(['male', 'female'])
        self.strength = rnd.randint(0, 5)

    def mating(self, obj_eco:list):
        #Нужно чтобы когда на одном индексе сталкивались животные разных полов,
        #они размножались (на индексе новый объект), а сами расходились по старым индексам
        self.animal1 = Animals()
        self.animal2 = Animals()
        if self.animal1.gender != self.animal2.gender in obj_eco:
            self.animal1 = self.animal2 = Animals()

    def fighting(self, obj_eco:list):
        #Нужно чтобы когда на одном индексе сталкивались животные одного пола,
        #они сравнивали свою силу, и тот у кого сила больше занимал весь индекс (убивал другого)
        self.animal1 = Animals()
        self.animal2 = Animals()
        if self.animal1.gender != self.animal2.gender in obj_eco:
            if self.animal1.strength >= self.animal2.strength:
                self.animal1 = self.animal2
            else:
                self.animal2 = self.animal1


class Bear(Animals):
    def __init__(self):
        self.type_of_animal = 'carnivorus'

    def eating(self, obj_bear, obj_food, obj_eco:list):
        #Нужно чтобы когда на одном индексе сталкивались медведь и рыба,
        #медведь съедал рыбу (весь индекс занимает медведь)
        self.obj_bear = Bear()
        self.obj_food = Fish()
        if self.obj_food == obj_bear in obj_eco:
            self.obj_food = self.obj_bear


class Fish(Animals):
    def __init__(self):
        self.type_of_animal = 'food'

if __name__ == '__main__':
    main()