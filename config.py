import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://username:password@localhost/mydatabase"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False