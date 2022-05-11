import random # |
import time #   |importing the libraries I will need

d = 0#              |
h = 0#              |
m = 0#              |
s = 0#              |
completed = False#  | setting values back to normal

def new():
    d = random.randint(0,100) #  |
    h = random.randint(0,23) #   |
    m = random.randint(0,59) #    |
    s = random.randint(0,59) #    |setting the random time
    
    print(d,":",h,":",m,":",s) # displaying original time
    
    while not completed:
        if s == 0: # checks if seconds has reached zero
            if m == 0: # checks if minutes has reached zero 
                if h == 0: # checks if hours have reached zero
                    if d == 0: # checks if days have reached zero
                        print("Timer done") # timer completion method
                        
                        def choice(): # starts choice loop
                            com = input("Do you want to restart?(y/n)") # asks for restart
                            com = com[0] # selects first letter of input
                            com = com.lower() # puts variable into lowercase
                            if com == 'y': # checks if answer started with "y"
                                new() # calls function
                            elif com == 'n': # checks if answer started with "n"
                                quit() # closes program
                            else: # checks if answer starts with anythong other than "y" or "n" 
                                print("invalid option") # output fail message
                                choice() # loops back to choose option
                        choice() # starts option choice loop

                    else: #         |
                        d -= 1 #    |
                        h = 23 #    |
                        m = 59 #    |
                        s = 60 #    | changes clock at start of new day
                        
                else: #         |
                    h -= 1 #    |
                    m = 59 #    |
                    s = 60 #    | changes clock at start of new hour
                    
            else: #         |
                m -= 1 #    |
                s = 60 #    | changes clock at start of new minute
             
        time.sleep(1) # 1 second wait so that it actally is a timer and not just counting down
        s-=1 # counting down the seconds
        print(d,":",h,":",m,":",s) # output the time

new() # initial call to function
