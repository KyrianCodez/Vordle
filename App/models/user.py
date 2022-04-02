from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column('username', db.String, nullable=False, unique=True)
    password = db.Column('password',db.String(120), nullable=False)
    highscore = db.Column(db.Integer)
    active = db.Column(db.Boolean, default=True, nullable = False)
    auth = db.Column(db.Boolean, default=False, nullable = False)
    anon = db.Column(db.Boolean, default=False, nullable = False)


    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.highscore = -9999
        self.active = True
        self.auth = False
        self.anon = False

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            'highscore': self.highscore,
            'active': self.active,
            'auth':self.active,
            'anon': self.anon
        }
    def set_auth(self, auth):
        self.auth = auth;
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)
