import __init__  # type: ignore
import db  # type: ignore
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

print("> db/migrate.py")

# セッション開始
sessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=__init__.engine)
session = sessionLocal()  # セッション開始

# 実行テスト
print(
    session.execute(
        text("SELECT 'Execution Test: Your Authorization is available.'")
    ).first()
)

# マイグレーション
try:
    db.Base.metadata.create_all(__init__.engine)
except Exception as e:
    print("\033[31mMigration Error:\033[0m", e)
else:
    pass

session.close()
