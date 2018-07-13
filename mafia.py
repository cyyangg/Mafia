from random import randint
from time import sleep
#player is player 0

#player roles
roles = ['mafia', 'mafia', 'doctor', 'detective', 'pizzaman']
#number of players
num_players = [0, 1, 2, 3, 4]
#player order of roles
play = []

#list of living people
living = []

#list of dead people
dead = []

#number of mafia
maf = 2



wait_time = 3


#night number
night = 1


#is the player alive
alive = True

#is the doctor alive
doc = True

#is the pizzaman alive
pm = True

#is the detective alive
det = True




#mafia kills
def maf_kill():
    kill = randint(0, len(living))
    return kill

#doctor heals
def doc_save():
    save = randint(0, len(living))
    return save

#pizzaman delivers
def pizza():
    piz = randint(0,len(living))
    return piz


#check if player dies
def check_dead(x):
    if x == 0:
        return False


name = input("What's your name? ")
sleep(1)
print('\n' + name + " had just moved into the quiet little town of Potato Town. Unknown to them though, was that this seemingly quiet town was actually overrun by mafia members.")
sleep(wait_time)
print("\nEvery night, the mafia would kill one person of Potato Town.")
sleep(wait_time)
print("\nEvery night, the doctor would save one person of Potato Town.") 
sleep(wait_time)
print("\nEvery night, the detective would learn the identity of one person of Potato Town.")
sleep(wait_time)
print("\nAnd every night, the pizzaman would deliver a pizza to one person of Potato Town.")
sleep(wait_time)
print("\nWelcome to mafia.")
sleep(wait_time)
    

while True: 
    #number of players you start out with
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
        
        
    #assign player roles
    for i in range(len(num_players)):
        x = randint(0, len(roles)-1)
        play.append(roles[x])
        del roles[x]
        #print(roles)
        #print(play_roles)
        
    #player is player 0
    player = play[0]
    
    #list of npcs
    npc = ['']
    for i in range(1,len(play)):
        npc.append(play[i])
        
    print(play)
    print(npc)
    
    print("\nYou are player 0, the " + player)
    sleep(wait_time)
    
    while alive == True:
    
        print("\n____________________________________")
        print("NIGHT " + str(night))
        print("____________________________________")
        sleep(wait_time)
         
        #if player is mafia
        if player == "mafia":
            print("You and player " + str(npc.index('mafia')) + " are mafia together.")
            sleep(wait_time)
            
            print(living)
            print("These are the living people.")
            sleep(wait_time)
            
            kill = input("\nChoose someone to kill tonight: ")
            print("\nYou have killed player " + kill)
            sleep(wait_time)
            
            print("\nGo to sleep.")
            sleep(wait_time)
            
            #if the doctor is alive, save a person
            if doc == True:
                #doctor chooses to save a person
                save = doc_save()
                print(save)
            else:
                save = 100
                
            #if doctor doesn't save the killed person, remove from living list and add to dead list
            if save != int(kill):
                living.remove(int(kill))
                dead.append(int(kill))
            print(living)
            print(dead)
            
            
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
            
            
            print("Last night, a tragedy occured.")
            sleep(wait_time)
            
            #if the player was killed
            if check_dead(int(kill)) == False:
                print("\nYou, " + name + " were killed! Sucks for you.")
                alive = False
                break
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
            
        
        elif player == 'doctor':
            print("\nYou are the doctor.")
            sleep(wait_time)
            
            print(living)
            print("These are the living people.")
            sleep(wait_time)
            
            save = input("\nChoose someone to save tonight: ")
            print("\nYou have saved player " + save)
            sleep(wait_time)
            
            print("\nGo to sleep.")
            sleep(wait_time)
            
            
            #if the mafia is alive, kill a person
            if maf > 0:
                #mafia chooses to kill a person
                kill = maf_kill()
                print(kill)
            else:
                kill = 100
                
            #if doctor doesn't save the killed person, remove from living list and add to dead list
            if int(save) != kill:
                living.remove(kill)
                dead.append(kill)
            print(living)
            print(dead)
            
            
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
            
            
            print("Last night, a tragedy occured.")
            sleep(wait_time)
            
            #if the player was killed
            if check_dead(int(kill)) == False:
                print("\nYou, " + name + " were killed! Sucks for you.")
                alive = False
                break
            else:
                print("\nPlayer " + str(kill) + " was killed!")
                sleep(wait_time)
                
                print("\nPlayer " + str(kill) + " was the " + play[kill] + '!')
                sleep(wait_time)
                
                
            #if the doctor saved the dead person
            if int(save) == kill:
                print("\nFortunately the doctor was able to save them so they didn't die!")
                sleep(wait_time)
                
                if play[kill] == 'mafia':
                    maf += 1
            else:
                print("\nThe doctor chose to save Player " + str(save))
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
            
        
        elif player == 'detective':
            print("\nYou are the detective.")
            sleep(wait_time)
            
            print(living)
            print("These are the living people.")
            sleep(wait_time)
            
            id = input("\nChoose someone to identify tonight: ")
            
            if play[int(id)] == 'mafia':
                print("Player " + id + " is mafia.")
            else:
                print("Player " + id + " is mafia.")
            
            sleep(wait_time)
            
            print("\nGo to sleep.")
            
            #if the mafia is alive, kill a person
            if maf > 0:
                #mafia chooses to kill a person
                kill = maf_kill()
                print(kill)
            else:
                kill = 100
                
                
            #if the doctor is alive, save a person
            if doc == True:
                #doctor chooses to save a person
                save = doc_save()
                print(save)
            else:
                save = 100
                
                
            #if doctor doesn't save the killed person, remove from living list and add to dead list
            if int(save) != kill:
                living.remove(kill)
                dead.append(kill)
            print(living)
            print(dead)
            
            
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
            
            
            print("Last night, a tragedy occured.")
            sleep(wait_time)
            
            #if the player was killed
            if check_dead(int(kill)) == False:
                print("\nYou, " + name + " were killed! Sucks for you.")
                alive = False
                break
            else:
                print("\nPlayer " + str(kill) + " was killed!")
                sleep(wait_time)
                
                print("\nPlayer " + str(kill) + " was the " + play[kill] + '!')
                sleep(wait_time)
            
                
                
            #if the doctor saved the dead person
            if save == int(kill):
                print("\nFortunately the doctor was able to save them so they didn't die!")
                sleep(wait_time)
                
                if play[int(kill)] == 'mafia':
                    maf += 1
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
            
            
        elif player == 'pizzaman':
            print("\nYou are the pizzaman.")
            sleep(wait_time)
            
            print(living)
            print("These are the living people.")
            sleep(wait_time)
            
            piz = input("\nChoose someone to deliver a pizza to tonight: ")
            
            print("You delivered a pizza to Player " + int(piz))
            
            sleep(wait_time)
            
            print("\nGo to sleep.")
            
            
            #if the mafia is alive, kill a person
            if maf > 0:
                #mafia chooses to kill a person
                kill = maf_kill()
                print(kill)
            else:
                kill = 100
                
            
            #if the doctor is alive, save a person
            if doc == True:
                #doctor chooses to save a person
                save = doc_save()
                print(save)
            else:
                save = 100
                
                
            #if doctor doesn't save the killed person, remove from living list and add to dead list
            if int(save) != kill:
                living.remove(kill)
                dead.append(kill)
            print(living)
            print(dead)
            
            
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
            
            
            print("Last night, a tragedy occured.")
            sleep(wait_time)
            
            
            #if the player was killed
            if check_dead(int(kill)) == False:
                print("\nYou, " + name + " were killed! Sucks for you.")
                alive = False
                break
            else:
                print("\nPlayer " + str(kill) + " was killed!")
                sleep(wait_time)
                
                print("\nPlayer " + str(kill) + " was the " + play[kill] + '!')
                sleep(wait_time)
            
            
            
            #if the doctor saved the dead person
            if save == int(kill):
                print("\nFortunately the doctor was able to save them so they didn't die!")
                sleep(wait_time)
                
                if play[int(kill)] == 'mafia':
                    maf += 1
            elif save < 100:
                print("\nThe doctor chose to save Player " + str(save))
                sleep(wait_time)
                
            elif doc == False:
                print("\nThe doctor is dead and couldn't save anyone.")
                sleep(wait_time)
                
                
                
            print("\nThe pizza was delivered to Player " + int(piz))
            sleep(wait_time)
           
            
            print("\nThere are " + str(maf) + " mafia left")
            sleep(wait_time)
            
            night += 1
            
            
        
        elif player == 'civilian':
            print("\nYou are a civilian and so you will sleep.")
            print("\nGo to sleep.")
            sleep(wait_time)
            sleep(wait_time)
            
            
            
            #if the mafia is alive, kill a person
            if maf > 0:
                #mafia chooses to kill a person
                kill = maf_kill()
                print(kill)
            else:
                kill = 100
                
                
            #if the doctor is alive, save a person
            if doc == True:
                #doctor chooses to save a person
                save = doc_save()
                print(save)
            else:
                save = 100
                
                
                
            #if doctor doesn't save the killed person, remove from living list and add to dead list
            if int(save) != kill:
                living.remove(kill)
                dead.append(kill)
            print(living)
            print(dead)
            
            
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
            
            
            print("Last night, a tragedy occured.")
            sleep(wait_time)
            
            #if the player was killed
            if check_dead(int(kill)) == False:
                print("\nYou, " + name + " were killed! Sucks for you.")
                alive = False
                break
            else:
                print("\nPlayer " + str(kill) + " was killed!")
                sleep(wait_time)
                
                print("\nPlayer " + str(kill) + " was the " + play[kill] + '!')
                sleep(wait_time)
            
            
            #if the doctor saved the dead person
            if save == int(kill):
                print("\nFortunately the doctor was able to save them so they didn't die!")
                sleep(wait_time)
                
                if play[int(kill)] == 'mafia':
                    maf += 1
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
                
        else: break
        
        if maf <= 0:
            print("\nThere are no more mafia! The town is saved!")
            break
        
        print("\nIt's time to accuse!")
        sleep(wait_time)
        
        print(living)
        print("These are the living")
        sleep(wait_time)
        
        accuse = input("\nChoose a player to accuse: ")
        
        print("You have chosen to accuse Player " + accuse)
        
        sleep(wait_time)
        
        print("After much debate, the town has decided to...")
        
        majority = randint(0,1)
        
        if majority == 0:
            print("\nKill Player " + accuse)
            
            #if the mafia was killed, subtract 1 from the mafia count
            if play[int(accuse)] == 'mafia':
                print("\nPlayer " + accuse + " was actually " + play[int(accuse)] + '!')
                maf -= 1
            #if the doctor was killed
            elif play[int(accuse)] == 'doctor':
                print("\nPlayer " + accuse + " was actually " + play[int(accuse)] + '!')
                doc = False
            #if the pizzaman was killed
            elif play[int(accuse)] == 'pizzaman':
                print("\nPlayer " + accuse + " was actually " + play[int(accuse)] + '!')
                pm = False
            #if the detective was killed
            elif play[int(accuse)] == 'detective':
                print("\nPlayer " + accuse + " was actually " + play[int(accuse)] + '!')
                det = False
            elif play[int(accuse)] == 'civilian':
                print("\nPlayer " + accuse + " was actually " + play[int(accuse)] + '!')
                det = False
            
            
            living.remove(int(accuse))
            dead.append(int(accuse))
            
        
        else:
            print("\nNot kill Player " + accuse)
         
        sleep(wait_time)
        
        if maf <= 0:
            print("\nThere are no more mafia! The town is saved!")
            break
        else:
            print("\nThere are " + str(maf) + " mafia left.")
            sleep(3)
         
        print("Go to sleep.")
        sleep(wait_time)
    
    break
         
        
            
    
        