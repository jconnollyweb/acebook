from acebook.db import get_db

class Liked():
  def user_likes_post(self, user_id, post_id):
    db = get_db()
    db.execute('INSERT INTO likes (users_id, posts_id)'
      ' VALUES (?, ?)',
      (user_id, post_id)
      )
    db.commit()
  
  #Currently not in use but could be useful later??? :)   
  def user_retrieve(self, user_id):
      likes = get_db().execute('SELECT username'
        ' FROM likes l JOIN user u ON l.users_id = u.id'
        ' WHERE u.id = ?',
        (user_id,)
      ).fetchone()
      
      return likes['username']
    
  def username_list(self, post_id):
      liked_list = get_db().execute('SELECT DISTINCT username'
        ' FROM likes l JOIN user u ON l.users_id = u.id'
        ' WHERE l.posts_id = ?',
        (post_id,)
      ).fetchall()
      return liked_list
    
    
      
