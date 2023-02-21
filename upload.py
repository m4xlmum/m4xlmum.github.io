# -*- coding: utf-8 -*-
#微信：huguo00289
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts

username="poem"
password="zyq.20011204"
apiurl="http://117.50.192.131/index.php/action/xmlrpc" #网站xmlrpc路径

wp = Client(apiurl,username, password)
print(wp)

post = WordPressPost()
post.title = '文章标题2'
post.content = '文章内容'
post.post_status = 'publish' #文章状态，不写默认是草稿，private表示私密的，draft表示草稿，publish表示发布

post.terms_names = {
    'post_tag': ['test', 'firstpost'], #文章所属标签，没有则自动创建
    'category': ['Introductions', 'Tests'] #文章所属分类，没有则自动创建
 }

post.id = wp.call(posts.NewPost(post))
print(post.id)