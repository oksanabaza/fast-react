from sqlalchemy import create_engine, MetaData
import pymysql

engine = create_engine("mysql+pymysql://root:password@localhost:3306/test")
meta = MetaData()
conn = engine.connect()
