from fastapi import Depends, HTTPException, status, FastAPI, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

print("> router/user/user.py")

oa2Scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()
router = APIRouter()

# パスワードによる OAuth2 Credential について、以下のページを参照しています。
# https://fastapi.tiangolo.com/ja/tutorial/security/simple-oauth2/

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


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm):
    hitUserData = fake.get(form_data.username)
    if not hitUserData:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = User(**hitUserData)
    hashed_password = user.password
    if not hashed_password == user.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {"access_token": user.uniqueId, "token_type": "bearer"}


@router.get("/me")
async def read_users_me(token: str = Depends(oa2Scheme)):
    result = {
        "id": "01HX3HTE70BHNDTNXE9FSGKNQY",
        "uniqueId": "testuser",
        "expireTime": "2021-10-01T00:15:00",
    }
    return result
