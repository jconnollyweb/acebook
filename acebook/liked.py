from acebook.db import get_db

class Liked():
   def user_likes_post(self, user_id, post_id):
    db = get_db()
    db.execute('INSERT INTO likes (users_id, posts_id)'
      ' VALUES (?, ?)',
      (user_id, post_id)
      )
    db.commit()