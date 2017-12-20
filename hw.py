class Animal:
    weight = 0
    feed = ''
    age = 0
    amount_feed_per_day = 0

    def count_feed_for_period(self, period):
        print("Count the feed for the period:", period,
              self.amount_feed_per_day * period)


class Mammal(Animal):
    pass


class Bird(Animal):
    pass
