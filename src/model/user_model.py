from dataclasses import dataclass

from util.logger import Logger


@dataclass
class UserEntity():    
    email: str
    password: str


class UserModel():
    def save_user(self, userEntity: UserEntity) -> UserEntity:
        Logger.info("saving user")
        Logger.info("user saved")
        return userEntity
