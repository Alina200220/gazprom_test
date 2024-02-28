from sqlalchemy import create_engine

# connection to database
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# creating engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)



