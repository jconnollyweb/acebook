from seleniumbase import BaseCase

class TestAuth(BaseCase):
  def test_login(self):
    self.open('http://localhost:5000/auth/login')
    self.type('input[name="username"]', "Eddie")
    self.type('input[name="password"]', "123")
    self.click('input[value="Log In"]')
    self.assert_text("New")
