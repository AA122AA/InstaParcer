import instaloader
from instaloader import Profile
import time

def login(L):
    L.login("shkolniebudni", "Workonelove122")
    profile = Profile.from_username(L.context, "kim_asja")
    return profile

def parcing(profile):  
    i = 0  
    t0 = int(time.time())
    print("start parcing at {}!".format(str(t0)))
    f = open("{}_followers.txt".format(profile.username), "w")
    for followers in profile.get_followers():
        i += 1
        f.write(followers.username + "\n")
        print(followers.username)
        if i % 5 == 0:
            print("stop")
            time.sleep(2)
    f.close()
    done = int(time.time())- t0
    print("{}s was waisted".format(str(done)))

def main():
    L = instaloader.Instaloader()
    profile = login(L)
    followers = profile.get_followers()
    print(followers)

    

if __name__ == "__main__":
    main()