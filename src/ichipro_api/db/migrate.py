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
    testUser = db.User()
    (
        testUser.uniqueId,
        testUser.email,
        testUser.password,
        testUser.faculty,
        testUser.department,
        testUser.grade,
        testUser.classes,
    ) = (
        "testuser",
        "test@sasakulab.com",
        "5ac2ac5ba94dbce933c6719ca250bf1752d938f43367af6618ab9e9e30b57df701dcda95287c5af56d8374abf292813efa07e1f287b9e4877ff17969b6735fe1",  # p@ssw0rd
        "学部情報",
        "情報科学",
        1,
        "E",
    )
    session.add(testUser)
    session.commit()
except Exception as e:
    print("\033[31mMigration Error:\033[0m", e)
else:
    pass

session.close()
