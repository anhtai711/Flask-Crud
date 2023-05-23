from distutils.debug import DEBUG


class Config(object):
    DEBUG = True
    SECRET_KEY = "1231312313123"
    
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root@localhost/restfull_crud1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False