import unittest
from unittest.mock import Mock

from src.controller.user_controller import UserController
from src.model.user_model import UserModel, UserEntity

class TestUserController(unittest.TestCase):
    def setUp(self) -> None:
        self._user_model = UserModel()
        self._user_controller = UserController(self._user_model)
    
    def test_should_create_a_user(self):    
        user_entity = UserEntity("johndoe@email.com", "Johndoe@123")
        self._user_model = Mock(return_value=user_entity)        
        
        result = self._user_controller.create_user(user_entity.email, user_entity.password)

        self.assertEqual(result, user_entity)