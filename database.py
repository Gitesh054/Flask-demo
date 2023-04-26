from sqlalchemy import create_engine

engine = create_engine('sqlite:///comp.db', echo=True)
engine.connect()