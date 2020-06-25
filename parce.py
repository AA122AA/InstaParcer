import instaloader
from instaloader import Profile
import time

L = instaloader.Instaloader()

L.login("gromartem", "Memesonelove122")
profile = Profile.from_username(L.context, "dianapagalina")

i = 0

print("start parcing!")
f = open("{}_followers.txt".format(profile.username), "w")
for followers in profile.get_followers():
    i += 1
    f.write(followers.username + "\n")
    print(followers.username)
    if i % 5 == 0:
        print("stop")
        time.sleep(2)
f.close()
print("end")

