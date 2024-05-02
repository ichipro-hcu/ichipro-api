import __init__  # type: ignore
import ulid
import enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Boolean, Enum, DateTime, SmallInteger
from sqlalchemy.sql import func

print("> db/db.py")

Base = declarative_base()


class Faculty(enum.Enum):
    共通 = 0
    学部国際 = 1
    学部情報 = 2
    学部芸術 = 3
    博士国際 = 5
    博士情報 = 6
    博士芸術 = 7
    博士平和 = 8


class dayOfWeek(enum.Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Int = 7  # 集中講義


class User(Base):
    __tablename__ = "user"
    id = Column(String(26), default=ulid.ulid(), primary_key=True)
    uniqueId = Column(String(15), unique=True)
    email = Column(String(64), unique=True)
    isEmailExist = Column(Boolean, default=False)
    password = Column(String(128))
    faculty = Column(Enum(Faculty))
    department = Column(String(8), default=0)
    grade = Column(Integer(), default=1)
    createTime = Column(DateTime(), server_default=func.now())
    updateTime = Column(DateTime(), onupdate=func.now())
    iconUrl = Column(String(128), default="")
    classes = Column(String(1), default="Z")


class EmailValid(Base):
    __tablename__ = "emailValid"
    user_id = Column(String(26), ForeignKey("user.id"), primary_key=True)
    authcode = Column(String(6))
    expire_date = Column(DateTime(), server_default=func.now())
    completed = Column(Boolean(), default=False)


class UserSetClass(Base):
    __tablename__ = "userSetClass"
    id = Column(String(26), default=ulid.ulid(), primary_key=True)
    user_id = Column(String(26), ForeignKey("user.id"))
    title = Column(String(48))
    where = Column(String(16), default="未設定")
    dayOfWeek = Column(Enum(dayOfWeek))
    timeOfDay = Column(SmallInteger(), default=0)
    updateTime = Column(DateTime())
    note = Column(String(200), default="")
    year = Column(SmallInteger())
    term = Column(SmallInteger())
    isNotifyAttendCheck = Column(Boolean(), default=False)


class ClassToAttend(Base):
    __tablename__ = "classToAttend"
    userSetClass_Id = Column(
        String(26), ForeignKey("userSetClass.id"), primary_key=True
    )
    attendance = Column(SmallInteger(), default=0)
    absence = Column(SmallInteger(), default=0)
    behind = Column(SmallInteger(), default=0)


class AccessLog(Base):
    __tablename__ = "accessLog"
    id = Column(Integer(), autoincrement=True, primary_key=True)
    createAt = Column(DateTime(), server_onupdate=func.now())
    accessIP = Column(DateTime())
    user_id = Column(String(26), ForeignKey("user.id"))
