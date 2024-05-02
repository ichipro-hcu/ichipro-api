from sqlalchemy import create_engine
import os
import sys

print("> db/__init__")

try:
    engine = create_engine(
        f"{os.environ['db_dialect']}://{os.environ['username']}:{os.environ['password']}@{os.environ['host']}/{os.environ['database']}",
        echo=True,
    )
except KeyError as e:
    print(f"The Environment Variables is unavailable: {e}")
    sys.exit()
