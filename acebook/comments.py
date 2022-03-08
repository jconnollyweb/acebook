from acebook.db import get_db

class Comments():
  def __init__(self, user_id, post_id, comment_body, created):
    self.user_id = user_id
    self.post_id = post_id
    self.comment_body = comment_body
    self.created = created

  @classmethod
  def create(cls, user_id, post_id, comment_body):
    db = get_db()
    db.execute(
      'INSERT INTO comments (users_id, posts_id, comment_body)'
      ' VALUES (?, ?, ?)',
      (user_id, post_id, comment_body)
    )
    db.commit()

  @classmethod
  def all(cls):
    db = get_db()
    comments = db.execute(
      'SELECT c.id, users_id, posts_id, comment_body, created'
      ' FROM comments c JOIN user u ON c.users_id = u.id'
      ' ORDER BY created DESC'
    ).fetchall()

    return [
      Comments(
        comment['users_id'],
        comment['posts_id'],
        comment['comment_body'],
        comment['created']
      ) for comment in comments
    ]
    
# class Comments():
#   def user_comments_on_post(self, user_id, post_id, comment_id):
#     db = get_db()
#     db.execute('INSERT INTO comments (users_id, posts_id, comment_id)'
#       ' VALUES (?, ?, ?)',
#       (user_id, post_id, comment_id)
#       )
#     db.commit()

#   def comment_list(self, post_id):
#         comment_list = get_db().execute('SELECT username, comment_id, created'
#           ' FROM comments c JOIN user u ON c.users_id = u.id'
#           ' WHERE c.posts_id = ?'
#           ' ORDER BY created DESC',
#           (post_id,)
#         ).fetchall()
#         return comment_list