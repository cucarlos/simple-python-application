import unittest

from src.model.user_model import UserModel, UserEntity

user_model = UserModel()

class TestUserModel(unittest.TestCase):
    def test_should_save_a_user(self):
        email = "johndoe@email.com"
        password = "Johndoe@123"
        user_entity = UserEntity(email, password)
    
        result = user_model.save_user(user_entity)
    
        self.assertEqual(result.email, email)
        self.assertEqual(result.password, password)
