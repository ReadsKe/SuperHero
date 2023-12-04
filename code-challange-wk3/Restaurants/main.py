from customer import Customer
from restaurant import Restaurant
from review import Review



## functionality Implementation
customer1 = Customer("Samuel", "Kimote")
customer2 = Customer("Philip", "Nduati")
customer3 = Customer("Peter", "Maina")

restaurant1 = Restaurant("Cafe XYZ")
restaurant2 = Restaurant("Pizza Palace")
restaurant3 = Restaurant("cafe Latte")

Review(customer1, restaurant2, 4.3)
Review(customer2, restaurant2, 4.1)
Review(customer3, restaurant1, 5)

#Reviews per
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer1, restaurant2, 3)
review3 = Review(customer1, restaurant1, 3)

review1 = Review(customer2, restaurant1, 3.5)
review2 = Review(customer2, restaurant2, 4.3)
review3 = Review(customer2, restaurant1, 1.5)
# Add_reviews
customer1.add_review(restaurant1, 4)
customer1.add_review(restaurant1, 5)

##---> number of reviews per customer 
num_reviews = customer1.num_reviews
print(f"Number of reviews for {customer1.full_name()}: {customer1.num_reviews}")

##--> Accessing information Printing Customer Name 
#print(customer1.full_name())
#print (customer2.full_name())
#print (customer3.full_name())

##--> Accessing information Printing all customer instances 
all_customers = customer1.get_customers_list()

if all_customers:
    print("List of Customers:")
    for customer in all_customers:
        print(f"  {customer.full_name()}")
else:
    print("No customers found.")

##--> name search--- find_by_name(
# found_customer = Customer.find_by_name("samuel Kimote")
# if found_customer:
#     print(f"Found customer: {found_customer.full_name()}")
# else:
#     print("Customer not found.")

 ##--> Find all customers with a given name
# customers_with_given_name = Customer.find_all_by_given_name("samuel")
# for customer in customers_with_given_name:
#     print(f"Customer with given name 'John': {customer.full_name()}")
    
##--> Accessing information printing Restaurant Name 
#print(restaurant1.name)
#print(restaurant2.name)
#print(restaurant3.name)

##--> Accessing information Printing all restaurant instances
all_restaurants = restaurant1.get_all_restaurants()

if all_restaurants:
    print("List of Restaurants:")
    for restaurant in all_restaurants:
        print(f"{restaurant.name}")
else:
    print("No restaurants found.")


##--> restaurant reviews 
# print(f"Customer: {customer1.full_name()}, Restaurant: {restaurant2.get_name()}")
# for review in restaurant2.get_reviews():
#     if review.get_customer() == customer1:
#         print(f"  Rating: {review.get_rating()}")
#     else:
#         print(f"No reviews")

##--> Restaurants reviews per customer 
# def reviews_per_customer(customer):
#     customer_reviews = [review for review in Review.get_all_reviews() if review.get_customer() == customer]
#     if customer_reviews:
#         print(f"Reviews by {customer.full_name()}:")
#         for review in customer_reviews:
#             print(f"  Restaurant: {review.get_restaurant().get_name()}, Rating: {review.get_rating()}")
#     else:
#         print(f"No reviews found for {customer.full_name()}")

# reviews_per_customer(customer1)
# reviews_per_customer(customer2)



##--> Average star rating for a restaurant based on its reviews
average_rating = restaurant1.average_star_rating()
print(f"Average Rating- {restaurant1.get_name()}: {average_rating}")
    


