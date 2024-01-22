from src.controller.user_controller import UserController

class UserView():
    def __init__(self, user_controller: UserController) -> None:
        self._user_controller = user_controller

    def create_user(self):
        print("Digite o email: ")
        email = input()
        print("Digite a senha: ")
        password = input()
        user_entity = self._user_controller.create_user(email, password)
        print(user_entity)
