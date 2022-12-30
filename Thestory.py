def Mainmenu():

    print ("A Cold Ride")
    print ("By Claidi Carabas")
    print  ("Type A to start")
    Option = input  ("Type B to leave")

    if Option == ("A"):
        Opening()
    elif Option == ("B"):
        print ("Goodbye")
    else:
        Mainmenu()

def Opening():

    print ("... It's a cold, snowy, misty night... You are biking right by a highway at a fast pace and your bike eventually breaks down.")
    print ("You leave the bike in a snowy ditch and keep walking.")
    print ("You eventually reach a road sign right by the highway. You rest your arm against the sign and wait for a car to drive by.")
    print ("As soon as you see a car approach, you stick your thumb up. The car slows down and stops by the side of the highway...")
    print ("The door on the passanger side opens. Revealing an empty seat and a an older man in the driver's seat...")
    print ("The Driver: 'Good evening. Got yourself lost now have you?'")
    print (" A = ''I need to get as far away from here as possible. My bike broke down and i need a lift.''")
    Option = input  (" B = [lie] 'I was on my way to the nearest town but my bike broke down.'")

    if Option == ("A"):
        motive_truth()
    elif Option == ("B"):
        motive_lie()
    else:
        Opening()
        
def motive_truth():
    print ("The Driver: 'I can help you out. There's a town not far from here. Hop in...")
    print ("You step in the car. The driver looks friendly enough. He looks middle aged, sporting a brown beard and wearing a dark blue beanie.")
    print ("The Driver:'Tell me. What were you doing out there in the mist?'")
    print ("A: I was running away.")
    print ("B: [lie] I was out trying to hunt down Cryptids")
    Option = input ("C: ... ")
    
    if Option == ("A"):
        running()
    elif Option == ("B"):
        cryptids()
    elif Option == ("C"):
        dotdotdot()
    else:
        motive_truth
      
      
def motive_lie():
    print ("The Driver: 'Is that so?")
    print ("I was heading to the nearest town as well. Hop in, we'll be there shortly. It's dangerous to walk this road alone on foot.'")
    print ("You step in the car. The driver looks friendly enough. He looks middle aged, sporting a brown beard and wearing a dark blue beanie.")
    print ("The Driver: 'So how did you get lost out there?'")
    print ("A: I was running away.")
    print ("B: [lie]' I was out trying to hunt down Cryptids'")
    Option = input ("C: ... ")

    if Option == ("A"):
        running()
    elif Option == ("B"):
        cryptids()
    elif Option == ("C"):
        dotdotdot()  
    else: motive_lie    

def running():
    print ("The Driver: 'Running from what. Did you do something?'")
    print ("You: 'No... I just... Need to get away. I didn't steal or kill anyone if that's what you're thinking!'")
    print ("The Driver: 'Alright, calm down. I'm not acusing you of anything. What's your name, kid?")
    print ("Brandon: 'Brandon... My name is Brandon.'")
    print ("The Driver: 'Brandon? Personally i've always liked that name... Got any... Got any family around?'")
    print ("A:' I live with my mother and younger sister... But i can't be around them right now...'")
    print ("B:[lie]'I don't have any family around anymore... I-it's a long story...'")
    Option = input ("C: ... ")
    
    if Option == ("A"):
        truth1()
    elif Option == ("B"):
        liar1()
    elif Option == ("C"):
        threedot()
    else:
        running()    
   
    
def cryptids():
    print ("The Driver: 'Cryptids? Well then, you might have found the right place.")
    print ("There are many strange rumours about this highway... By the way. What's your name?'")
    print ("Brandon: My name is Brandon. i urm... I'm trying to go viral by discovering a cryptid on this misty road.")
    print ("The Driver: 'Brandon... I have always liked that name... This road is mostly empty. I rarely see any other cars pass by.'")
    print ("Brandon: 'How come. Cryptids scare them away?'")
    print ("The Driver:'You could say that. But there are shorter roads into town.'")
    print ("Tell me Brandon. Got any family around?'")
    print ("A:'I live with my mother and younger sister... But i can't be around them right now...'")
    print ("B:[lie]'I don't have any family around anymore... I-it's a long story...")
    Option = input ("C: ... ")

    if Option == ("A"):
        truth1()
    elif Option == ("B"):
        liar1()
    elif Option == ("C"):
        threedot()
    else:
        cryptids()

def dotdotdot():    
    print ("The Driver: 'Not much of a talker are you?")
    print ("Do you have any family that would be looking for you?'")
    print ("A: 'My mother and my younger sister i'm afraid...")
    print ("B:[lie]'I don't have any family left...'")
    Option = input ("C: ...")
    
    if Option ==("A"):
        truth1()
    elif Option == ("B"):
        liar1()
    elif Option == ("C"):
        threedot2()
    else: 
        dotdotdot()    

def truth1():
    print ("The Driver: 'Do they know you're out here?'")
    print ("Brandon: 'No... I can't talk with them... Not right now.'")
    print ("The Driver: 'Sorry, kid... Time to go...")
    print ("The Driver now begins to drive into the snowy mist...")
    print ("The mist makes it impossible to see from the side mirrors. the only thing visible is the road")
    print ("You look around the car. You notice a Santa Claus bobblehead on The Driver's dashboard, A radio playing soft Christmas tunes.")
    print ("You feel both comfortable and on edge. You don't trust this stranger. But no bad signs have shown yet.")


def liar1():
    print ("The Driver: 'I'm sorry, kid. Do you have a home?")
    print ("Brandon: 'urm... no i don't. I'm always on the road, y'know?'")
    print ("The Driver: 'I see. We better get going.'")
    print ("The Driver now begins to drive into the snowy mist...")
    print ("The mist makes it impossible to see from the side mirrors. the only thing visible is the road")
    print ("You look around the car. You notice a Santa Claus bobblehead on The Driver's dashboard, A radio playing soft Christmas tunes.")
    print ("You feel both comfortable and on edge. You don't trust this stranger. But no bad signs have shown yet.")
    
    
def threedot():
    print ("The Driver: 'aye... Touchy subject? very well. Let's go.'")
    print ("The Driver now begins to drive into the snowy mist...")
    print ("The mist makes it impossible to see from the side mirrors. the only thing visible is the road")
    print ("You look around the car. You notice a Santa Claus bobblehead on The Driver's dashboard, A radio playing soft Christmas tunes.")
    print ("You feel both comfortable and on edge. You don't trust this stranger. But no bad signs have shown yet.")    
  
    
def threedot2():
    print ("The Driver fully turns his eyes to the round when he sees that you give him no response. He refrains from asking more questions and starts driving into the mist. ")
    print ("The mist makes it impossible to see from the side mirrors. the only thing visible is the road")
    print ("You look around the car. You notice a Santa Claus bobblehead on The Driver's dashboard, A radio playing soft Christmas tunes.")
    print ("You feel both comfortable and on edge. You don't trust this stranger. But no bad signs have shown yet.")