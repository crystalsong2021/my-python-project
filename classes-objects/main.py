#going to import the user and post

from user import User
from post import Post

app_user_one = User("nn@nn.com", "Crystal Song", "pwd1", "FullStack Engineer")
app_user_one.get_user_info()

app_user_two = User("testUser2@gmail.com", "Test user2", "pwd2", "Super Agent")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()