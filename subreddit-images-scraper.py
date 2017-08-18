import praw
import urllib
import os
import getpass

y = getpass.getuser()

if not os.access("/home/" + y + "/pictures/", os.F_OK):
   os.mkdir("/home/" + y + "/pictures/")

os.chdir("//home/" + y + "/pictures/")
print "working directory is now " + os.getcwd()


user_agent = praw.Reddit(user_agent = "hello_ua", client_id = "", client_secret = "") #fill the client_id and client_secret fields
urls = []
counter = 1
for submission in user_agent.subreddit('all').top(limit=1000):
    if submission.url not in urls:
        if len(submission.url.split(".")[-1].strip("/")) == 3:
            urls.append(submission.url)
            urllib.urlretrieve(submission.url, str(counter) + "." + submission.url.split(".")[-1])
            counter += 1

