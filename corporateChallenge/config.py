import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Путь к вашей базе данных
    SQLALCHEMY_TRACK_MODIFICATIONS = False