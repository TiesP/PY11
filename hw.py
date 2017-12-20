class Animal:
    weight = 0
    feed = ''
    age = 0
    amount_feed_per_day = 0

    def __init__(self, amount_feed_per_day):
        self.amount_feed_per_day = amount_feed_per_day

    def count_feed_for_period(self, period):
        print("Count the feed for the period:", period,
              self.amount_feed_per_day * period)


class Mammal(Animal):
    gives_milk = False


class Bird(Animal):
    gives_eggs = False


class Cow(Mammal):
    gives_milk = True


class Goat(Mammal):
    gives_milk = True


class Sheep(Mammal):
    pass


class Pig(Mammal):
    pass


class Duck(Bird):
    gives_eggs = True


class Chicken(Bird):
    gives_eggs = True


class Goose(Bird):
    gives_eggs = True

d = Duck(10)
d.count_feed_for_period(5)
