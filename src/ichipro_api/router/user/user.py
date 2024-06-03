from fastapi import Depends, HTTPException, status, FastAPI, APIRouter

print("> router/user/user.py")

oa2Scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()
router = APIRouter()

fake = {
    "testuser": {
        "id": "01HX3HTE70BHNDTNXE9FSGKNQY",
        "uniqueId": "testuser",
        "email": "example@example.com",
        "isEmailExist": True,
        "password": "fakehashedsecret",
        "faculty": "学部情報",
        "department": "情報工学",
        "grade": 1,
        "createTime": "2021-10-01T00:00:00",
        "updateTime": "2021-10-01T00:00:00",
        "iconUrl": "",
        "classes": "Z",
    }
}


class User:
    id: str
    uniqueId: str
    email: str
    isEmailExist: bool
    password: str
    faculty: str
    department: str
    grade: int
    createTime: str
    updateTime: str
    iconUrl: str
    classes: str

