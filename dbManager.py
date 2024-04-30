from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


class DbManager(object):
    db = None

    def __init__(self):
        return

    def initialize_db(self, app):
        self.db = SQLAlchemy()
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite3:///database.db"
        app.config["SECRET_KEY"] = "db_password"
        self.db.init_app(app)

        class Data(self.db.model, UserMixin):
            id = self.db.column(self.db.Integer, primary_key=True)
            device_id = self.db.column(self.db.String(100), nullable=False)
            date = self.db.column(self.db.String(10), nullable=False)
            time = self.db.column(self.db.String(20), nullable=False)
            # fare lo storage dei dati effettivi usando notazione csv
            temperature = self.db.column(self.db.String(50), nullable=False)
            humidity = self.db.column(self.db.String(50), nullable=False)
            heat_index = self.db.column(self.db.String(50), nullable=False)
            light = self.db.column(self.db.String(50), nullable=False)

        with app.app_context():
            self.db.create_all()


    def query_data(self, data):
        pass