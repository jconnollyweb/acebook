from seleniumbase import BaseCase
from faker import Faker

fake = Faker()
class TestRegister(BaseCase):
  def test_registration(self):
    self.open('http://127.0.0.1:5000/auth/register')
    username = fake.name()
    self.type('input[name="username"]', username)
    self.type('input[name="password"]', "12345678")
    self.click('input[value="Register"]')
    self.assert_text("Profile")
    self.assert_text(username)
    self.assert_text("Welcome")