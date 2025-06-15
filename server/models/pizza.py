from server.app import db 

class pizza(db.Model):
    __tablename__ = 'pizza'

    id = db.column(db.integer, primary_key=True)
    name = db.column(db.string, nullables=False)
    ingridients = db.column(db.string, nullables=False)
    price = db.column(db.float, nullables=False)

    def __repr__(self):
        return f"<Pizza {self.name}>"
    
                     