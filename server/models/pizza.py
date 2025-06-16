from server.extensions import db

class Pizza(db.Model):
    __tablename__ = 'pizza'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Pizza {self.name}>"
