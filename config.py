class Config(object):
    SECRET_KEY = '1d03808cf4ee4e980b53d8847bdd53ee'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
