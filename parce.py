import instaloader
from instaloader import Profile
import time

def login(L):
    L.login("shkolniebudni", "Workonelove122")
    profile = Profile.from_username(L.context, "dianapagalina")
    return profile

def parsing(profile):  
    i = 0  
    t0 = int(time.time())
    print("start parcing at {}!".format(str(t0)))
    f = open("{}_followers.txt".format(profile.username), "w")
    for followers in profile.get_followers():
        i += 1
        f.write(followers.username + "\n")
        print(followers.username)
        if i % 10 == 0:
            print("stop")
            time.sleep(3)
    f.close()
    done = int(time.time())- t0
    print("{}s was waisted".format(str(done)))

def main():
    L = instaloader.Instaloader()
    profile = login(L)
    parsing(profile)

    

if __name__ == "__main__":
    main()