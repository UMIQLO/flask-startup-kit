class Config(object):
    pass


class ProdConfig(Config):
    DEBUG = False
    SECRET_KEY = 'b49bcd2251f538ee9429340e1a969307'
    # mysql connection uri
    SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1/dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'b49bcd2251f538ee9429340e1a969307'
    # mysql connection uri
    SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1/dev'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
