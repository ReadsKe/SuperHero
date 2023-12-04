from review import Review
class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def get_reviews(self):
        from review import Review  # avoiding circular dependency
        return [review for review in Review.all_reviews if review.get_restaurant() == self]

    def get_customers(self):
        from review import Review  # avoiding circular dependency
        return list(set([review.get_customer() for review in Review.all_reviews if review.get_restaurant() == self]))

    def average_star_rating(self):
        ratings = [review.get_rating() for review in self.get_reviews()]
        return sum(ratings) / len(ratings) if len(ratings) > 0 else 0

    def get_all_restaurants(self):
        return Restaurant.all_restaurants
    

