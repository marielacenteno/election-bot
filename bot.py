import praw
import random
import datetime
import time
import textblob

# FIXME:
# copy your generate_comment functions from the week_07 lab here
def generate_comment_0():
    joes = ['Joe', 'Joe Biden', 'Joseph Robinette Biden', 'Biden', 'Vice President Biden', 'VP Biden']
    joe = random.choice(joes)

    whys = [' is the best choice possible. ', ' is our best shot at fixing our country. ', ' is awesome. ', ' is a decent man. ', ' is not Trump. ']
    why = random.choice(whys)

    whats = ['Go vote for ', 'Believe in ', 'Support ']
    what = random.choice(whats)

    outputs = ['Joe Biden. ', 'a better America. ', 'a better future. ', 'a safer America. ', 'a better economy. ']
    output = random.choice(outputs)

    signouts = ['Biden2020.', 'Go Biden! ', 'BidenHarris2020. ', 'HarrisBiden2020.']
    signout = random.choice(signouts)

    text = joe + why + what + output + signout
    return text



def generate_comment_1():
    joes = ['Joe', 'Joe Biden', 'Joseph Robinette Biden', 'Biden', 'Vice President Biden', 'VP Biden']
    joe = random.choice(joes)

    whos = ['the American people.', 'others.', 'humans.', 'his country.', 'the constitution.', 'morals.']
    who = random.choice(whos)

    whats = ['like other politicians. ', 'like Donald trump. ', 'insensitive to the plight of the average Americans. ', 'careless about American lives. ']
    what = random.choice(whats)

    characteristics = ['humble.', 'kind.', 'responsible.', 'caring.', 'understanding.', 'experienced.', 'wise.']
    characteristic = random.choice(characteristics)

    whys = [' you believe in human decency. ', ' you care about your country. ', ' you love America. ', ' you believe in democracy. ']
    why = random.choice(whys)

    text = joe + " cares about " + who + " He is not " + what + "He is " + characteristic + " Vote for Biden if" + why
    return text

def generate_comment_2():

    joes = ['Joe', 'Joe Biden', 'Joseph Robinette Biden', 'Biden', 'Vice President Biden', 'VP Biden']
    joe = random.choice(joes)

    whats = [' broken country. ', ' country. ', ' economy. ', ' public health crisis. ']
    what = random.choice(whats)

    baracks = [' President Obama. ', ' President Barack Obama. ', ' Obama. ', ' Barack Obama. ']
    barack = random.choice(baracks)

    whens = [' during these uncertain times. ', ' in this moment in history. ', ' right now. ', ' to heal our nation. ']
    when = random.choice(whens)

    text = joe + " will fix our" + what + "He got us out of the Great Recession with" + barack + "Our country needs someone like " + joe + when
    return text

def generate_comment_3():

    trumplovers = [' are people still voting for ', ' do people still like ', ' do people still believe in ', ' are people considering voting for ']
    trumplover = random.choice(trumplovers)

    whos = [' Trump?', ' President Trump?', ' Donald Trump?', ' Donald?']
    who = random.choice(whos)

    whats = [' supposed to ', ' going to ', ' promising to ', ' trying to ']
    what = random.choice(whats)

    friends = [' his repulsive friends ', ' his incompetent cabinet ', ' his nepotism ', ' his corruption ']
    friend = random.choice(friends)

    swamps = [" he's created.", " he's cultivated.", " he's managed to create.", " that DC has become under the Trump presidency"]
    swamp = random.choice(swamps)

    text = "Why" + trumplover + who + " Wasn't he" + what + "drain the swamp? All he did was make it dirtier with" + friend + "in the white house. An ogre wouldn't even get near the swamp" + swamp
    return text

def generate_comment_4():

    whos = ['Donald Trump ', 'Trump ', 'President Trump ', 'Donald ', 'Donny ']
    who = random.choice(whos)

    whats = [' the most incompetent ', ' the worst ', ' the most destructive ', ' the most careless ']
    what = random.choice(whats)

    ncares = [' anyone. ', ' Americans. ', ' the constitution. ', ' morals. ']
    ncare = random.choice(ncares)

    ycares = [' his big ego.', ' his big macs.', ' his steaks.', ' his own interests.']
    ycare = random.choice(ycares)

    bads = [' careless ', ' untrustworthy ', ' hateful ', ' selfish ']
    bad = random.choice(bads)

    text = who + "is" + what + "president of all time. He is" + bad + "and he clearly doesn't care about" + ncare + "He only cares about" + ycare
    return text


def generate_comment_5():

    names = ['The current president', 'Mr. Trump', 'President Trump', 'The failed businessman disguised as a politician']
    name = random.choice(names)

    whos = [' himself.', ' his party.', ' the white house.' , ' his wife.']
    who = random.choice(whos)


    whats = [' supposed to ', ' going to ', ' trying to ']
    what = random.choice(whats)

    areas = [' an entire country?', ' millions?', ' all Americans?', ' the most influential country in the world?']
    area = random.choice(areas)


    results_of_presidency = [' more political turmoil than ever.', ' more political tensions than ever.', ' more social unrest than ever.', ' an unprecedented level of overall hatred in our nation.', ' the worst economic crisis of modern American history.', ' the worst public health crisis in modern American history.']
    result_of_presidency = random.choice(results_of_presidency)

    text = name + " can't even take care of" + who + " How is he" + what + "take care of" + area + " That's right, he hasn't. Four years of him and we have gotten" + result_of_presidency

    return text
#print('text =', generate_comment_5())

def generate_comment():
    options = [generate_comment_0, generate_comment_1, generate_comment_2, generate_comment_3, generate_comment_4, generate_comment_5]
    comment = random.choice(options)
    text = comment()
    return text



# connect to reddit 
reddit = praw.Reddit('bot')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jnnbga/florida_voters_switch_political_parties_ahead_of/'
submission = reddit.submission(url=reddit_debate_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

while True:
    try:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
        print()
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',submission.title)
        print('submission.url=',submission.url)

        # FIXME (task 0): get a list of all of the comments in the submission
        # HINT: this requires using the .list() and the .replace_more() functions
        all_comments = []
        num_comments = 0
        submission.comments.replace_more(limit = None)
        for comment in submission.comments.list():
            all_comments.append(comment)
            num_comments += 1





        # HINT: 
        # we need to make sure that our code is working correctly,
        # and you should not move on from one task to the next until you are 100% sure that 
        # the previous task is working;
        # in general, the way to check if a task is working is to print out information 
        # about the results of that task, 
        # and manually inspect that information to ensure it is correct; 
        # in this specific case, you should check the length of the all_comments variable,
        # and manually ensure that the printed length is the same as the length displayed on reddit;
        # if it's not, then there are some comments that you are not correctly identifying,
        # and you need to figure out which comments those are and how to include them.
        print('len(all_comments)=',len(all_comments))

        # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
        # HINT: 
        # use a for loop to loop over each comment in all_comments,
        # and an if statement to check whether the comment is authored by you or not
        not_my_comments = []
        for comment in all_comments:
            if str(comment.author) != 'maricenten':
                not_my_comments.append(comment)


        # HINT:
        # checking if this code is working is a bit more complicated than in the previous tasks;
        # reddit does not directly provide the number of comments in a submission
        # that were not gerenated by your bot,
        # but you can still check this number manually by subtracting the number
        # of comments you know you've posted from the number above;
        # you can use comments that you post manually while logged into your bot to know 
        # how many comments there should be. 
        print('len(not_my_comments)=',len(not_my_comments))

        # if the length of your all_comments and not_my_comments lists are the same,
        # then that means you have not posted any comments in the current submission;
        # (you bot may have posted comments in other submissions);
        # your bot will behave differently depending on whether it's posted a comment or not
        has_not_commented = len(not_my_comments) == len(all_comments)

        if has_not_commented:
            # FIXME (task 2)
            # if you have not made any comment in the thread, then post a top level comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit
            try:
                y = random.choice(not_my_comments)
                random_comment = reddit.comment(id = y)
                print('random comment id =', y)
                random_comment.reply(generate_comment())
                print('commented')
            except:
                len(not_my_comments) == 0
                print('     len of comment without replies = 0')



        else:
            # FIXME (task 3): filter the not_my_comments list to also remove comments that 
            # you've already replied to
            # HINT:
            # there are many ways to accomplish this, but my solution uses two nested for loops
            # the outer for loop loops over has_not_comments,
            # and the inner for loop loops over all the replies of the current comment from the outer loop,
            # and then an if statement checks whether the comment is authored by you or not
            comments_without_replies = []
            for comment in not_my_comments:
                replied = True
                for reply in comment.replies:
                    if str(reply.author) == 'maricenten':
                        replied == False
                if replied == True:
                    comments_without_replies.append(comment)
                    
                

            # HINT:
            # this is the most difficult of the tasks,
            # and so you will have to be careful to check that this code is in fact working correctly
            print('len(comments_without_replies)=',len(comments_without_replies))

            # FIXME (task 4): randomly select a comment from the comments_without_replies list,
            # and reply to that comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit
            comment = random.choice(comments_without_replies)
            comment.reply(generate_comment())


    except praw.exceptions.APIException:
        print('exception found')
        time.sleep(60)
        print('Done sleeping')

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should have a 50% chance of being the original submission
    # (url in the reddit_debate_url variable)
    # and a 50% chance of being randomly selected from the top submissions to the csci040 subreddit for the past month
    # HINT: 
    # use random.random() for the 50% chance,
    # if the result is less than 0.5,
    # then create a submission just like is done at the top of this page;
    # otherwise, create a subreddit instance for the csci40 subreddit,
    # use the .top() command with appropriate parameters to get the list of all submissions,
    # then use random.choice to select one of the submissions
    prob = random.random()
    if prob < .5:
        submission = reddit.submission(url=reddit_debate_url)
    else:
        top_threads = list(reddit.subreddit('csci040temp').top(time_filter='all'))
        x = random.choice(top_threads)
        submission = reddit.submission(x)


'''
# EXTRA CREDIT #

# Task 1, Section 1: Upvote any COMMENT mentioning my favorite candidate (1 point)  #

    submission.comments.replace_more(limit = None)
    for comment in submission.comments.list():
        if 'biden' in comment.body.lower():
            comment.upvote()
            print ('Comment Upvote')


    #Task 2, section 1: Upvoting SUBMISSION with my favorite candidate #
    

    for submission in reddit.submission(url=reddit_debate_url):
        if 'biden' in submission.title.lower():
            submission.upvote()
            print('Submission Upvote')

    #Task 3, Section 1: Sorting Comments and making my bot reply to higly upvoted comments #
    for comment in submission.comments.list():
        x = reverse(sorted(submission.comments.list())

    #Task 3, Section 2: Measuring sentiment
    submission.comments.replace_more(limit = None)
    for comment in submission.comments.list():
        blob = TextBlob(str(comment.body))
        sub = blob.sentiment.subjectivity
        polarity = blob.sentiment.polarity
        
        if 'biden' in comment.body.lower() and polarity > 0.5:
            comment.upvote()

        if 'trump' in comment.body.lower() and polarity > 0.5:
            comment.downvote()
        
        if 'biden' in comment.body.lower() and sentiment > 0:
            comment.upvote()

        if 'trump' in comment.body.lower() and sentiment > 0:
            comment.downvote()

        print('sentiment measured')
        

'''




