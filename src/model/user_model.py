from dataclasses import dataclass


@dataclass
class UserEntity():    
    email: str
    password: str


class UserModel():
    def save_user(self, userEntity: UserEntity) -> UserEntity:
        print("saving user")
        print("user saved")
        return userEntity
