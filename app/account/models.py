# Models specific to user profiles

class IgtieUser():
    pass


class UserBase(IgtieUser):
    pass


class UserLogin(UserBase):
    pass


class UserLoginResponse(IgtieUser):
    pass


class UserRegister(UserBase):
    pass


class UserRegisterResponse(UserBase):
    pass


class UserRead(UserBase):
    pass


class UserUpdate(IgtieUser):
    pass
