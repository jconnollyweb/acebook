from acebook.db import get_db

class Like():
  def __init__(self, user_id, post_id):
    self.user_id = user_id
    self.post_id = post_id

  @classmethod
  def create(cls, user_id, post_id):
    db = get_db()
    if Like.find(user_id, post_id) is not None:
      print("Username already in database")
    else:
      db.execute(
        'INSERT INTO likes (users_id, posts_id)'
        ' VALUES (?, ?)',
        (user_id, post_id)
      )
      db.commit()

  @classmethod
  def all(cls):
    db = get_db()
    likes = db.execute(
      'SELECT l.id, u.username, posts_id'
      ' FROM likes l JOIN user u ON l.users_id = u.id'
    ).fetchall()

    return [
      Like(
        like['username'],
        like['posts_id'],
      ) for like in likes
    ]
    
  @classmethod
  def find(cls, user_id, post_id):
    db = get_db()
    like = db.execute(
      'SELECT id, users_id, posts_id FROM likes WHERE users_id = ? AND posts_id = ?', (user_id, post_id)
    ).fetchone()
    if like:
      return Like(like['users_id'], like['posts_id'])
    else:
      return None
# class Liked():
#   def user_likes_post(self, user_id, post_id):
#     db = get_db()
#     db.execute('INSERT INTO likes (users_id, posts_id)'
#       ' VALUES (?, ?)',
#       (user_id, post_id)
#       )
#     db.commit()
  
#   #Currently not in use but could be useful later??? :)   
#   def user_retrieve(self, user_id):
#       likes = get_db().execute('SELECT username'
#         ' FROM likes l JOIN user u ON l.users_id = u.id'
#         ' WHERE u.id = ?',
#         (user_id,)
#       ).fetchone()
      
#       return likes['username']
    
  def username_list(self, post_id):
      liked_list = get_db().execute('SELECT DISTINCT username'
        ' FROM likes l JOIN user u ON l.users_id = u.id'
        ' WHERE l.posts_id = ?',
        (post_id,)
      ).fetchall()
      return liked_list
    
    
      
