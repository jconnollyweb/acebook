import os
from acebook.db import get_db

class Post():

  @classmethod
  def create(cls, title, body, user_id, pic):
    db = get_db()
    if pic == None:
      db.execute(
        'INSERT INTO post (title, body, author_id)'
              ' VALUES (?, ?, ?)',
        (title, body, user_id)
      )
    else:
      db.execute(
        'INSERT INTO post (title, body, author_id, photo)'
              ' VALUES (?, ?, ?, ?)',
        (title, body, user_id, pic)
      )    
    db.commit()

  def writeTofile(data, name):
    if data == None:
      return None
    else:
    # Convert binary data to proper format and write it on Hard Disk
      filename = os.path.join("acebook/static/uploaded_pics", name)
      with open(filename, 'wb') as file:
          file.write(data)
      print("Stored blob data into: ", filename, "\n")
      return name

  @classmethod
  def all(cls):
    db = get_db()
    posts = db.execute(
      'SELECT p.id, title, body, created, author_id, username, photo'
      ' FROM post p JOIN user u ON p.author_id = u.id'
      ' ORDER BY created DESC'
    ).fetchall()  

    return [
      Post(
        post['title'],
        post['body'],
        post['id'],
        post['created'],
        post['author_id'],
        post['username'],
        Post.writeTofile(post['photo'], str(post['id']) + ".jpeg")
      ) for post in posts
    ]

  @classmethod
  def find_by_id(cls, id):
    post = get_db().execute(
      'SELECT p.id, title, body, created, author_id, username, photo'
      ' FROM post p JOIN user u ON p.author_id = u.id'
      ' WHERE p.id = ?',
      (id,)
    ).fetchone()

    return Post(
      post['title'],
      post['body'],
      post['id'],
      post['created'],
      post['author_id'],
      post['username'],
      post['photo']
      
    )

  def __init__(self, title, body, id, created, author_id, username, pic):
    self.title = title
    self.body = body
    self.id = id
    self.created = created
    self.author_id = author_id
    self.username = username
    self.pic = pic
    

  def update(self, title, body, id):
    db = get_db()
    db.execute(
      'UPDATE post SET title = ?, body = ?'
      ' WHERE id = ?',
      (title, body, id)
    )
    db.commit()

  def delete(self):
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (self.id,))
    db.commit()

  def liked(self, user_id):
    db = get_db()
    db.execute('INSERT INTO likes (users_id, posts_id)'
      ' VALUES (?, ?, ?)',
      (user_id, self.id)
      )
    db.commit()