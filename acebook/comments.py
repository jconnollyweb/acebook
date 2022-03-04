from acebook.db import get_db

class Comments():
  def user_comments_on_post(self, user_id, post_id, comment_id):
    db = get_db()
    db.execute('INSERT INTO comments (users_id, posts_id, comment_id)'
      ' VALUES (?, ?, ?)',
      (user_id, post_id, comment_id)
      )
    db.commit()

  def comment_list(self, post_id):
        comment_list = get_db().execute('SELECT username, comment_id, created'
          ' FROM comments c JOIN user u ON c.users_id = u.id'
          ' WHERE c.posts_id = ?'
          ' ORDER BY created DESC',
          (post_id,)
        ).fetchall()
        return comment_list