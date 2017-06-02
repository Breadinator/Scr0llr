# Scr0llr
Browses subreddits, that you set, to look for key words, that you set, and - if instructed - logs the usernames of the authors who wrote the post. Written in python 3.4.4

# Instructions
Run it once. It will create a words.txt file in which one places all flag words(one per line).
Run it again. It will then create a subreddits.txt file in which one places all the subreddits you wish to watch(one per line).
Run it yet again. This is where you will start off if those file are already made. It will prompt you if you wish to log users and create a log.txt file if one doesn't already exist. Then, leave it to run. It will cycle through the subreddits in order, with one search every 10 seconds, and say which users flag.

# Prerequisites
1. Python - it definately works in version 3.4.4
2. Praw for python - configure the praw.ini to have a bot named bot1.
3. An internet connection!
