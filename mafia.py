from random import randint
from time import sleep


###--------------------------------------
###Creation of all the lists 
###--------------------------------------

#list of all possible roles other than civilians 
roles = ['mafia', 'mafia', 'doctor', 'detective', 'pizzaman']

#number of roles
num_players = [0, 1, 2, 3, 4]

#player order of roles
play = []

#list of living people
living = []

#list of dead people
dead = []



###--------------------------------------
###Various game variables
###--------------------------------------

#number of mafia alive
maf = 2

#wait time between text
wait_time = 2.4

#night number
night = 1



###--------------------------------------
###Values for if people are alive or dead
###--------------------------------------

#True if player is alive, False if not
alive = True

#True if doctor is alive, False if not
doc = True

#True if doctor is alive, False if not
pm = True

#True if doctor is alive, False if not
det = True


###--------------------------------------
###Functions for npc roles to do their thing
###--------------------------------------

#mafia chooses one random person to kill
def maf_kill():
    kill = randint(0, len(living)-1)
    return kill

#doctor chooses one random person to save
def doc_save():
    save = randint(0, len(living)-1)
    return save

#pizzaman chooses one random person to deliver pizza to
def pizza():
    piz = randint(0,len(living)-1)
    return piz


#check if player dies
def check_dead(x):
    if x == 0:
        return False



###--------------------------------------
###Introduction text
###--------------------------------------
name = input("What's your name? ")
sleep(1)
print('\n' + name + " had just moved into the quiet little town of Potato Town. Unknown to them though, was that this seemingly quiet town was actually overrun by mafia members.")
sleep(wait_time)
print("\nEach night, the mafia will kill one person.")
sleep(wait_time)
print("\nEach night, the doctor will save one person.") 
sleep(wait_time)
print("\nEach night, the detective will learn the identity of one person.")
sleep(wait_time)
print("\nAnd each night, the pizzaman will deliver a pizza to one person.")
sleep(wait_time)
print("\nWelcome to mafia.")
sleep(wait_time)
sleep(wait_time)
    


###--------------------------------------
###Actual game
###--------------------------------------
while True: 
    #choose number of players you start out with
    start_players = input("\n \n \nHow many players would you like to play with? You can play with minimum of 5. ")
    

    if int(start_players) < 5:
        print("Not enough players. End game.")
        break
    else:
        #make rest of roles civilians
        for players in range(5, int(start_players)):
            roles.append('civilian')
            num_players.append(players)
    
    #add player numbers to list of living people
    for i in range (len(num_players)):
        living.append(num_players[i])
        
        
    #assign player roles randomly
    for i in range(len(num_players)):
        x = randint(0, len(roles)-1)
        play.append(roles[x])
        del roles[x]
        #print(roles)
        #print(play_roles)
       
       
    #player is player 0
    player = play[0]
    
    #create list of npcs
    npc = ['']
    for i in range(1,len(play)):
        npc.append(play[i])
        
    #print(play)
    #print(npc)
        
    
    print("\nYou are player 0, the " + player)
    sleep(wait_time)
    
    
    
    ###--------------------------------------
    ###While the player is alive, do their thing then accuse
    ###--------------------------------------
    while alive == True:
    
        print("\n____________________________________")
        print("NIGHT " + str(night))
        print("____________________________________")
        sleep(wait_time)
         
         
        ###--------------------------------------
        ###if player is mafia
        ###--------------------------------------
        if player == "mafia":
            #if partner mafia is alive
            if npc.index('mafia') in living:
                print("You and player " + str(npc.index('mafia')) + " are mafia together.")
                sleep(wait_time)
            #if player is only mafia alive
            else:
                print("You are the mafia.")
                sleep(wait_time)
                
                
            print(living)
            print("These are the living people.")
            sleep(wait_time)
            
            #player kills someone
            kill = input("\nChoose someone to kill tonight: ")
            print("\nYou have killed player " + kill)
            sleep(wait_time)
            
            print("\nGo to sleep.")
            sleep(wait_time)
            
            
            #if the doctor is alive, save a person
            if doc == True:
                #doctor chooses to save a person
                save = doc_save()
                #print(save)
            else:
                save = 100
                
                
            #if doctor doesn't save the killed person, remove from living list and add to dead list
            if save != int(kill):
                living.remove(int(kill))
                dead.append(int(kill))
            #print(living)
            #print(dead)
            
            
            #if the mafia was killed, subtract 1 from the mafia count
            if play[int(kill)] == 'mafia':
                maf -= 1
            #if the doctor was killed
            elif play[int(kill)] == 'doctor':
                doc = False
            #if the pizzaman was killed
            elif play[int(kill)] == 'pizzaman':
                pm = False
            #if the detective was killed
            elif play[int(kill)] == 'detective':
                det = False
                
            
            sleep(wait_time)
            
            
            
            print("\n____________________________________")
            print("MORNING")
            print("____________________________________")
            sleep(wait_time)
            
            print("Last night, a tragedy occured.")
            sleep(wait_time)
            
            
            #if the player was killed
            if check_dead(int(kill)) == False:
                print("\nYou, " + name + " were killed! Sucks for you.")
                alive = False
                break
            #if an npc was killed
            else:
                print("\nPlayer " + kill + " was killed!")
                sleep(wait_time)
                print("\nPlayer " + kill + " was the " + play[int(kill)] + '!')
                sleep(wait_time)
            
            
            #if the doctor saved the dead person
            if save == int(kill):
                print("\nFortunately the doctor was able to save them so they didn't die!")
                sleep(wait_time)
                
                if play[int(kill)] == 'mafia':
                    maf += 1
            #if the doctor saved a different person
            elif save < 100:
                print("\nThe doctor chose to save Player " + str(save))
                sleep(wait_time)
                
            elif doc == False:
                print("\nThe doctor is dead and couldn't save anyone.")
                sleep(wait_time)
            
            
            #if pizzaman is alive, they deliver pizza
            if pm == True:
                print("\nThe pizza was delivered to Player " + str(pizza()))
                sleep(wait_time)
                
            else:
                print("\nThe pizzaman is dead and can't deliver pizza.")
                sleep(wait_time)
            
            print("\nThere are " + str(maf) + " mafia left")
            sleep(wait_time)
            
            night += 1
            
        
        ###--------------------------------------
        ###if player is doctor
        ###--------------------------------------
        elif player == 'doctor':
            print("\nYou are the doctor.")
            sleep(wait_time)
            
            print(living)
            print("These are the living people.")
            sleep(wait_time)
            
            #player chooses to save someone
            save = input("\nChoose someone to save tonight: ")
            print("\nYou have saved player " + save)
            sleep(wait_time)
            
            print("\nGo to sleep.")
            sleep(wait_time)
            
            
            
            #if the mafia is alive, kill a person
            if maf > 0:
                #mafia chooses to kill a person
                kill = maf_kill()
                #print(kill)
            
            
                
            #if doctor doesn't save the killed person, remove from living list and add to dead list
            if int(save) != kill:
                living.remove(kill)
                dead.append(kill)
            #print(living)
            #print(dead)
            
            
            #if the mafia was killed, subtract 1 from the mafia count
            if play[kill] == 'mafia':
                maf -= 1
            #if the doctor was killed
            elif play[kill] == 'doctor':
                doc = False
            #if the pizzaman was killed
            elif play[kill] == 'pizzaman':
                pm = False
            #if the detective was killed
            elif play[kill] == 'detective':
                det = False
                
            
            sleep(wait_time)
            print("\n____________________________________")
            print("MORNING")
            print("____________________________________")
            sleep(wait_time)
            
            
            print("Last night, a tragedy occured.")
            sleep(wait_time)
            
            
            #if the player was killed
            if check_dead(int(kill)) == False:
                print("\nYou, " + name + " were killed! Sucks for you.")
                alive = False
                break
            #if npc was killed
            else:
                print("\nPlayer " + str(kill) + " was killed!")
                sleep(wait_time)
                
                print("\nPlayer " + str(kill) + " was the " + play[kill] + '!')
                sleep(wait_time)
                
               
               
            #if the doctor saved the dead person
            if int(save) == kill:
                print("\nFortunately the doctor was able to save them so they didn't die!")
                sleep(wait_time)
                #if they were mafia, add one mafia
                if play[kill] == 'mafia':
                    maf += 1
            #if doctor saved a rando
            else:
                print("\nThe doctor chose to save Player " + str(save))
                sleep(wait_time)
                
            
            
            #if pizzaman is alive, they deliver pizza
            if pm == True:
                print("\nThe pizza was delivered to Player " + str(pizza()))
                sleep(wait_time)
            #if pizzaman is dead   
            else:
                print("\nThe pizzaman is dead and can't deliver pizza.")
                sleep(wait_time)
            
            print("\nThere are " + str(maf) + " mafia left")
            sleep(wait_time)
            
            night += 1
            
            
            
        ###--------------------------------------
        ###if player is detective
        ###--------------------------------------
        elif player == 'detective':
            print("\nYou are the detective.")
            sleep(wait_time)
            
            print(living)
            print("These are the living people.")
            sleep(wait_time)
            
            #player chooses someone to identify                        
            id = input("\nChoose someone to identify tonight: ")
            
            #if chosen is mafia, print
            if play[int(id)] == 'mafia':
                print("Player " + id + " is mafia.")
            #if chosen not mafia, priny
            else:
                print("Player " + id + " is mafia.")
            
            sleep(wait_time)
            
            print("\nGo to sleep.")
            
            
            
            #if the mafia is alive, kill a person
            if maf > 0:
                #mafia chooses to kill a person
                kill = maf_kill()
                #print(kill)
            
                
                
            #if the doctor is alive, save a person
            if doc == True:
                #doctor chooses to save a person
                save = doc_save()
                #print(save)
            #if doctor is dead
            else:
                save = 100
                
             
             
            #if doctor doesn't save the killed person, remove from living list and add to dead list
            if int(save) != kill:
                living.remove(kill)
                dead.append(kill)
            #print(living)
            #print(dead)
            
            
            
            #if the mafia was killed, subtract 1 from the mafia count
            if play[kill] == 'mafia':
                maf -= 1
            #if the doctor was killed
            elif play[kill] == 'doctor':
                doc = False
            #if the pizzaman was killed
            elif play[kill] == 'pizzaman':
                pm = False
            #if the detective was killed
            elif play[kill] == 'detective':
                det = False
                
            
            
            sleep(wait_time)
            print("\n____________________________________")
            print("MORNING")
            print("____________________________________")
            sleep(wait_time)
            
            
            print("Last night, a tragedy occured.")
            sleep(wait_time)
            
            #if the player was killed
            if check_dead(int(kill)) == False:
                print("\nYou, " + name + " were killed! Sucks for you.")
                alive = False
                break
            #if npc was killed
            else:
                print("\nPlayer " + str(kill) + " was killed!")
                sleep(wait_time)
                
                print("\nPlayer " + str(kill) + " was the " + play[kill] + '!')
                sleep(wait_time)
            
                
                
            #if the doctor saved the dead person
            if save == int(kill):
                print("\nFortunately the doctor was able to save them so they didn't die!")
                sleep(wait_time)
                #if it was mafia, add one to mafia
                if play[int(kill)] == 'mafia':
                    maf += 1
            #if doctor saved rando
            elif save < 100:
                print("\nThe doctor chose to save Player " + str(save))
                sleep(wait_time)
            #if doctor is dead    
            elif doc == False:
                print("\nThe doctor is dead and couldn't save anyone.")
                sleep(wait_time)
                
            
            
            #if pizzaman is alive, they deliver pizza
            if pm == True:
                print("\nThe pizza was delivered to Player " + str(pizza()))
                sleep(wait_time)
            #if pizzaman is dead
            else:
                print("\nThe pizzaman is dead and can't deliver pizza.")
                sleep(wait_time)
            
            #print how many mafia there are left
            print("\nThere are " + str(maf) + " mafia left")
            sleep(wait_time)
            
            night += 1
       
       
        
        ###--------------------------------------
        ###if player is pizzaman
        ###--------------------------------------
        elif player == 'pizzaman':
            print("\nYou are the pizzaman.")
            sleep(wait_time)
            
            print(living)
            print("These are the living people.")
            sleep(wait_time)
            
            #player chooses to deliver pizza to someone
            piz = input("\nChoose someone to deliver a pizza to tonight: ")
            
            print("You delivered a pizza to Player " + str(piz))
            
            sleep(wait_time)
            
            print("\nGo to sleep.")
            
            
            
            #if the mafia is alive, kill a person
            if maf > 0:
                #mafia chooses to kill a person
                kill = maf_kill()
                #print(kill)

                
            
            #if the doctor is alive, save a person
            if doc == True:
                #doctor chooses to save a person
                save = doc_save()
                #print(save)
            #if doctor is dead
            else:
                save = 100
                
                
            #if doctor doesn't save the killed person, remove from living list and add to dead list
            if int(save) != kill:
                living.remove(kill)
                dead.append(kill)
            #print(living)
            #print(dead)
            
            
            #if the mafia was killed, subtract 1 from the mafia count
            if play[kill] == 'mafia':
                maf -= 1
            #if the doctor was killed
            elif play[kill] == 'doctor':
                doc = False
            #if the pizzaman was killed
            elif play[kill] == 'pizzaman':
                pm = False
            #if the detective was killed
            elif play[kill] == 'detective':
                det = False
                
            
            sleep(wait_time)
            
            print("\n____________________________________")
            print("MORNING")
            print("____________________________________")
            sleep(wait_time)
            
            print("Last night, a tragedy occured.")
            sleep(wait_time)
            
            
            #if the player was killed
            if check_dead(int(kill)) == False:
                print("\nYou, " + name + " were killed! Sucks for you.")
                alive = False
                break
            #if npc was killed
            else:
                print("\nPlayer " + str(kill) + " was killed!")
                sleep(wait_time)
                
                print("\nPlayer " + str(kill) + " was the " + play[kill] + '!')
                sleep(wait_time)
            
            
            
            #if the doctor saved the dead person
            if save == int(kill):
                print("\nFortunately the doctor was able to save them so they didn't die!")
                sleep(wait_time)
                #if saved is mafia, add one mafia
                if play[int(kill)] == 'mafia':
                    maf += 1
            #if doctor saved rando
            elif save < 100:
                print("\nThe doctor chose to save Player " + str(save))
                sleep(wait_time)
            #if doctor is dead
            elif doc == False:
                print("\nThe doctor is dead and couldn't save anyone.")
                sleep(wait_time)
                
                
            #pizzaman does their thing      
            print("\nThe pizza was delivered to Player " + int(piz))
            sleep(wait_time)
           
            #print how many mafia are left
            print("\nThere are " + str(maf) + " mafia left")
            sleep(wait_time)
            
            night += 1
            
            
        
        ###--------------------------------------
        ###if player is civilian
        ###--------------------------------------
        elif player == 'civilian':
            print("\nYou are a civilian and so you will sleep.")
            print("\nGo to sleep.")
            sleep(wait_time)
            sleep(wait_time)
            
            
            
            #if the mafia is alive, kill a person
            if maf > 0:
                #mafia chooses to kill a person
                kill = maf_kill()
                #print(kill)
 
                
                
            #if the doctor is alive, save a person
            if doc == True:
                #doctor chooses to save a person
                save = doc_save()
                #print(save)
            #if doctor is dead
            else:
                save = 100
                
                
                
            #if doctor doesn't save the killed person, remove from living list and add to dead list
            if int(save) != kill:
                living.remove(kill)
                dead.append(kill)
            #print(living)
            #print(dead)
            
            
            #if the mafia was killed, subtract 1 from the mafia count
            if play[kill] == 'mafia':
                maf -= 1
            #if the doctor was killed
            elif play[kill] == 'doctor':
                doc = False
            #if the pizzaman was killed
            elif play[kill] == 'pizzaman':
                pm = False
            #if the detective was killed
            elif play[kill] == 'detective':
                det = False
               
               
            
            sleep(wait_time)
            print("\n____________________________________")
            print("MORNING")
            print("____________________________________")
            sleep(wait_time)
            
            print("Last night, a tragedy occured.")
            sleep(wait_time)
            
            
            
            #if the player was killed
            if check_dead(int(kill)) == False:
                print("\nYou, " + name + " were killed! Sucks for you.")
                alive = False
                break
            #if npc was killed
            else:
                print("\nPlayer " + str(kill) + " was killed!")
                sleep(wait_time)
                
                print("\nPlayer " + str(kill) + " was the " + play[kill] + '!')
                sleep(wait_time)
            
            
            
            #if the doctor saved the dead person
            if save == int(kill):
                print("\nFortunately the doctor was able to save them so they didn't die!")
                sleep(wait_time)
                #if mafia saved, re add mafia
                if play[int(kill)] == 'mafia':
                    maf += 1
            #if doctor saved rando
            elif save < 100:
                print("\nThe doctor chose to save Player " + str(save))
                sleep(wait_time)
            #if doctor is dead    
            elif doc == False:
                print("\nThe doctor is dead and couldn't save anyone.")
                sleep(wait_time)
                
                
            
            #if pizzaman is alive, they deliver pizza
            if pm == True:
                print("\nThe pizza was delivered to Player " + str(pizza()))
                sleep(wait_time)
            #if pizzaman is dead   
            else:
                print("\nThe pizzaman is dead and can't deliver pizza.")
                sleep(wait_time)
            
            #print how many mafia are left
            print("\nThere are " + str(maf) + " mafia left")
            sleep(wait_time)
            
            night += 1
                
        else: break
        
        
        ###--------------------------------------
        ###accusations
        ###--------------------------------------
        
        #if there are no more mafia end
        if maf <= 0:
            print("\nThere are no more mafia! The town is saved!")
            break
        #if player is mafia and is still alive end
        if (len(living) <= 1) or (len(living) == 2 and maf == 2):
            print("You have won. The town of Potato is no more.")
            break
        
        
        print("\nIt's time to accuse!")
        sleep(wait_time)
        
        print(living)
        print("These are the living")
        sleep(wait_time)
        
        #player chooses someone to accuse
        accuse = input("\nChoose a player to accuse: ")
        
        print("You have chosen to accuse Player " + accuse)
        
        sleep(wait_time)
        
        
        #npc chooses someone to accuse
        accuse2 = randint(0, len(living) - 1)

        print("\nThe town has decided to accuse Player " + living[int(accuse2)])
        
        
        
        print("\nAfter much debate, the town has decided to...")
        sleep(wait_time)
         
        #town decides who to kill 
        majority = randint(0,3)
        
        #player vote gets 50% chance of death
        if majority == 0 or majority == 1:
            print("\nKill Player " + accuse)
            
            #if the mafia was killed, subtract 1 from the mafia count
            if play[int(accuse)] == 'mafia':
                print("\nPlayer " + accuse + " was actually the " + play[int(accuse)] + '!')
                maf -= 1
            #if the doctor was killed
            elif play[int(accuse)] == 'doctor':
                print("\nPlayer " + accuse + " was actually the " + play[int(accuse)] + '!')
                doc = False
            #if the pizzaman was killed
            elif play[int(accuse)] == 'pizzaman':
                print("\nPlayer " + accuse + " was actually the " + play[int(accuse)] + '!')
                pm = False
            #if the detective was killed
            elif play[int(accuse)] == 'detective':
                print("\nPlayer " + accuse + " was actually the " + play[int(accuse)] + '!')
                det = False
            elif play[int(accuse)] == 'civilian':
                print("\nPlayer " + accuse + " was actually the " + play[int(accuse)] + '!')
                det = False
          
          
        #town vote gets 25% chance of death  
        elif majority == 2:
            print("\nKill Player " + living[int(accuse2)])
            
            #if the mafia was killed, subtract 1 from the mafia count
            if play[int(accuse)] == 'mafia':
                print("\nPlayer " + accuse + " was actually the " + play[int(accuse)] + '!')
                maf -= 1
            #if the doctor was killed
            elif play[int(accuse)] == 'doctor':
                print("\nPlayer " + accuse + " was actually the " + play[int(accuse)] + '!')
                doc = False
            #if the pizzaman was killed
            elif play[int(accuse)] == 'pizzaman':
                print("\nPlayer " + accuse + " was actually the " + play[int(accuse)] + '!')
                pm = False
            #if the detective was killed
            elif play[int(accuse)] == 'detective':
                print("\nPlayer " + accuse + " was actually the " + play[int(accuse)] + '!')
                det = False
            elif play[int(accuse)] == 'civilian':
                print("\nPlayer " + accuse + " was actually the " + play[int(accuse)] + '!')
                det = False
            
            
            living.remove(int(accuse))
            dead.append(int(accuse))
            
        
        #no one dies gets 25% chance
        else:
            print("\nNot kill anyone.")
         
        sleep(wait_time)
        
        
        #if no more mafia members end
        if maf <= 0:
            print("\nThere are no more mafia! The town is saved!")
            break
        #if player and mafia are only ones remaining end
        elif (len(living) <= 1) or (len(living) == 2 and maf == 2):
            print("You have won. The town of Potato is no more.")
            break
        #otherwise continue
        else:
            print("\nThere are " + str(maf) + " mafia left.")
            sleep(3)
         
        print("Go to sleep.")
        sleep(wait_time)
    
    break
         
        
            
    
        