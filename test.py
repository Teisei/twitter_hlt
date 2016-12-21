#coding=UTF-8
_author_ = "yanyao"

from twitter import *

my_auth = OAuth(token="719348056827633664-sMMJNecL1IzAYiPG4SFUqTVmqW2aMuf",
                token_secret="5WwPmSvFKbzroWeMLPBKhCyw8JFJY27lrwkiVmihFHig4",
                consumer_key="8JbFCHUN0gj3GduG9Yi9poRQe",
                consumer_secret="YqxvHw9j4KObanExFptFTCjBk4jrZFCtOAzYPl3BZXgVvdSX0Q"
                )
t = Twitter(auth=my_auth)
max_id = None
for _ in range(10):
<<<<<<< HEAD
    if max_id is None:
=======
    if True:
>>>>>>> 64da65a4db5abe3b40d30a047c559e65155f625c
        ans = t.search.tweets(q="#atheism", count=100)
    else:
        ans = t.search.tweets(q="#atheism", count=100, max_id=max_id)
    max_id = ans[u"search_metadata"][u"max_id"]
    for item in ans[u"statuses"]:
        print "\n-------------------------------------------"
        print item[u"text"].strip().encode("utf-8")
        print "-------------------------------------------\n"


