# database.py
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


Base = declarative_base()


load_dotenv()

db_user = os.getenv("DATABASE_USERNAME")
db_pass = os.getenv("DATABASE_PASSWORD")
db_host = os.getenv("HOST")
db_name = os.getenv("DB_NAME")
db_port = os.getenv("DB_PORT","5433")


db_url = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
# db_url = f"postgresql+asyncpg://{os.getenv('DATABASE_USERNAME')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
print("url: ",db_url)
engine = create_async_engine(db_url, future=True) 
async_session = sessionmaker(
    engine, class_=AsyncSession,expire_on_commit=False
)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
# Async session maker
async def get_session():
    async with async_session() as session:
        yield session

