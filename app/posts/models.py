from app import db

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'schema': 'alma'}

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def as_dict(self):
        return {
            'id': self.id,
            'text': self.text,
            'latitude': self.latitude,
            'longitude': self.longitude
        }
    
    def __lt__(self, other):
        return self.id < other.id