import praw
import os
import subprocess

browser = 'chromium'
r = praw.Reddit(user_agent='reddit_dzen')
subname = "unixporn" # Enter the subreddit name here
submissions = r.get_subreddit(subname).get_new(limit=10)
titles = []
urls = []
text = ""
i = 0
for x in submissions:
    text += "^ca(3," + browser + " " + x.url + " ) " + x.title + "^ca()\n"
text = "(echo \""+ subname + "\"\necho \"" + text + "\") | dzen2 -p -x '" + str(int(subprocess.check_output(["xdotool getmouselocation | grep -oE 'x:[[:digit:]]{2,3}' | sed 's/x://'",""],shell=True).decode('utf-8'))-200) + "' -y '20' -w '400' -l '11' -sa 'c' -ta 'c' -e 'onstart=uncollapse;button1=exit' -fn  -*-ohsnapu-medium-r-normal-*-11-*-*-*-*-*-*-*"
print(text)
os.system(text)
