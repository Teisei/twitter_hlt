#coding=UTF-8
_author_ = "yanyao"

from twitter import *
import re

my_auth = OAuth(token="719348056827633664-sMMJNecL1IzAYiPG4SFUqTVmqW2aMuf",
                token_secret="5WwPmSvFKbzroWeMLPBKhCyw8JFJY27lrwkiVmihFHig4",
                consumer_key="8JbFCHUN0gj3GduG9Yi9poRQe",
                consumer_secret="YqxvHw9j4KObanExFptFTCjBk4jrZFCtOAzYPl3BZXgVvdSX0Q"
                )
t = Twitter(auth=my_auth)

def main():
    max_id = None
    for _ in range(10):
        if max_id is None:
            ans = t.search.tweets(q="#atheism", count=100)
        else:
            ans = t.search.tweets(q="#atheism", count=100, max_id=max_id)
        max_id = get_next_max_id(ans[u"search_metadata"][u"next_results"])
        for item in ans[u"statuses"]:
            print "\n-------------------------------------------"
            print item[u"text"].strip().encode("utf-8")
            print "-------------------------------------------\n"


def get_next_max_id(next_query_str):
    pattern = re.compile(u"\?max_id=(\d*)")
    match = pattern.match(next_query_str)
    if match is not None:
        return int(match.group(1))
    else:
        return 0
if __name__ == "__main__":
    #t1 = get_next_max_id(u'?max_id=811542643846975487&q=%23atheism&count=100&include_entities=1')
    #pass
    main()

