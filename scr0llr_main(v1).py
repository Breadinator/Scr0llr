import praw
import os.path as path
from time import sleep, strftime

#Bot created by the Breadinator in python 3.4.4
#To setup, setup praw and configure praw.ini to have your bot, bot1 in praw.ini, actually exist.
#Then create files called 'words.txt' and 'subreddits.txt' in the directory of this program or let the program generate the itself.
#Add what flag words you want to pick up in words.txt and what subreddits you wish to search in subreddits.txt

reddit = praw.Reddit('bot1')

watchlist_words = []
watchlist_subreddits = []
logged = []


#Check if files exist
if not path.exists("words.txt"):
    with open("words.txt", "w+") as f0:
        print("Please add your flag words to words.txt.")
        wait = input('Press enter to exit.')
        f0.close
        quit()
if not path.exists("subreddits.txt"):
    with open("subreddits.txt", "w+") as f1:
        print("Please add your subreddits to subreddits.txt.")
        wait = input('Press enter to exit.')
        f1.close
        quit()
if not path.exists("log.txt"):
    with open("log.txt", "w+") as f2:
        print("log.txt file created.")
        f2.close

#Read files, add words line by line to the corresponding list then close
with open("words.txt", "r") as f0:
    watchlist_words = [line.strip() for line in f0]
    f0.close
with open("subreddits.txt", "r") as f1:
    watchlist_subreddits = [line.strip() for line in f1]
    f1.close
with open("log.txt", "r") as f2:
    logged = [line.strip() for line in f2]
    f2.close

### UNCOMMENT FOLLOWING TWO LINES FOR TESTING PURPOSES(to see if your flag words and subreddit list has been successful) ###
#print(watchlist_words)
#print(watchlist_subreddits)

#Ask if you wish to log users
log = input("Do you wish to log identified users? (y/n)\n>")
if log == 'y':
    log = 'true'
    print('Logging mode enabled')
elif log == 'yes':
    log = 'true'
    print('Logging mode enabled')
else:
    log = 'false'
    print('Logging mode disabled')
print('\n------------------------------\n')

#Main block
while 1:
    for subreddit in watchlist_subreddits:
        hits = 0
        print('Scanning ' + str(subreddit).upper() + ' at ' + strftime("%X"))
        subreddit = reddit.subreddit(subreddit)
        for submission in subreddit.new(limit=5):
            for word in watchlist_words:
                with open("log.txt", "r") as f2:
                    logged = [line.strip() for line in f2]
                    #print(logged) #Testing purposes
                    f2.close
                try:
                    if word in submission.title or submission.selftext:
                        print("\nTitle: ", str(submission.title))
                        #print("Text: ", submission.selftext) #add for additional information
                        #print("Score: ", submission.score) #add for additional information
                        print("User: ", str(submission.author))
                        
                        if log == 'true':
                            with open("log.txt", "a+") as f2:
                                logno = 0
                                for person in logged:
                                    if person == str(submission.author):
                                        logno += 1
                                if logno == 0:
                                    logged = [line.strip() for line in f2]
                                    if str(submission.author) not in logged:
                                        f2.write(str(submission.author) + "\n")
                                        f2.close
                                
                        hits += 1
                        break
                    #else: #Uncomment these lines for testing
                        #print("Safe result.\n")
                except UnicodeEncodeError:
                    print('(A UnicodeEncodeError error occurred)')
                    pass
        if hits == 0:
            print("No results found.")
        print('\n------------------------------\n')
        sleep(10) #This is used as only a certain amount of bot queries(if that's the right word) are allowed. Max is 1 per 2 seconds.
