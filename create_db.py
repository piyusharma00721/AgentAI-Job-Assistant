from sqlalchemy import create_engine
from database.models import Base  # adjust this if your model file is named differently

# Replace this with your real DB URL (likely you already have it in settings)
DATABASE_URL = "postgresql://postgres:Piyush007_@localhost:5432/agenticai"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully.")
