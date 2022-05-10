from instafollower import InstaFollower
import time

insta_follower = InstaFollower()
time.sleep(5)
insta_follower.login()
time.sleep(5)
insta_follower.find_followers()
