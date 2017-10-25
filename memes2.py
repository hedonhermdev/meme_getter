import sys

import os
import datetime
import scraper
import urllib.request
from multiprocessing.dummy import Pool as ThreadPool

print(sys.version)

def get_memes(profile, num):
    failed = []
    def get_pic(p):
        try:
            post = scraper.PostPage(p)
            print("Successfully opened %s" % p)
            urllib.request.urlretrieve(post.post_meta()['Media'], "memes/" + p + ".jpg")
        except Exception as e:
            print(e)
            print("Failed to open %s" % p)
            failed.append(p)
    try:
        profile = scraper.ProfilePage(profile)
        pool = ThreadPool(8)
        posts = profile.profile_meta()['Recent Posts'][:num]
        print("Successfully opened profile page.")
        print(posts)
        memes = pool.map(get_pic, posts)
        print("***\n")
        print("TIME: %s \n" % str(datetime.datetime.now()))
        print("SUCCESSFULLY COLLECTED MEMES. \n")
        memes = pool.map(get_pic, failed)
    except Exception as e:
        print("Failed to open profile page.")
        print(str(e))

if __name__ == '__main__':
    num = 12
    if len(sys.argv) == 3:
        num = int(sys.argv[2])
    get_memes(sys.argv[1], num)
