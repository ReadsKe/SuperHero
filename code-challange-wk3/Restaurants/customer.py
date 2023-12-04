from review import Review
class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        Customer.all_customers.append(self)

    def get_given_name(self): 
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    def get_customers_list(self):  
        return Customer.all_customers

    def restaurants(self):
        reviewed_restaurants = set([review.restaurant() for review in Review.all_reviews if review.customer() == self])
        print(f"Restaurants reviewed by {self.full_name()}: {', '.join([restaurant.get_name() for restaurant in reviewed_restaurants])}")
        return list(reviewed_restaurants)

    def add_review(self, restaurant, rating):
        Review(self, restaurant, rating)  

    def num_reviews(self):
        return len([review for review in Review.all_reviews if review.customer() == self])

    @classmethod
    def find_by_name(cls, name):
        return next((customer for customer in cls.all_customers if customer.full_name() == name), None)

    @classmethod
    def find_all_by_given_name(cls, given_name):
        return [customer for customer in cls.all_customers if customer.get_given_name() == given_name]
