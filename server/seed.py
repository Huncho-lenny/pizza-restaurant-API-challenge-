from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    r1 = Restaurant(name="Joe's Pizza", address="123 Main St")
    r2 = Restaurant(name="Luigi's", address="456 Elm St")

    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p3 = Pizza(name="Veggie", ingredients="Tomato, Mozzarella, Peppers, Onions, Olives")

    db.session.add_all([r1, r2, p1, p2, p3])
    db.session.commit()

    rp1 = RestaurantPizza(price=12, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=15, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=10, restaurant_id=r2.id, pizza_id=p3.id)
    rp4 = RestaurantPizza(price=13, restaurant_id=r2.id, pizza_id=p1.id)

    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        seed_data()
        print("Database seeded!")