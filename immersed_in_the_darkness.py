#------------------------------------------------Immersed in the darkness---------------------------------------------
#Μιχάλης Γρίβας
#started : 27/03/2020
#finished : 03/05/2020

#################################################Περιγραφή#############################################################
#Είναι ένα text adventure, που είσαι ένας ντεντέκτιβ και προσπαθείς να εξιχνιάσεις μια δολοφονία
#Υπάρχουν 3 ύποπτοι, και οι 3 είχαν κίνιτρο να σκοτώσουν το θύμα την κληρονομιά του, αφού ήταν στενοί φίλοι του
#Πάς στο σπίτι που έγινε η δολοφονία και ψάχνεις για στοιχεία που έχουν αφήσει οι ύποπτοι
#Χρησιμοποιώντας αντικείμενα και ανοίγοντας μυστικά περάσματα φτάνεις τελικά στον σκοπό σου επιλέγοντας τον ένοχο
#Υπάρχουν 30 δωμάτια και 11 αντικείμενα
#Πάρε έναν καφέ, κάτσε άνετα στο γραφείο σου και άρχισε να παίζεις!!!

#Σημείωση: μην αρχίσεις να μελετάς τον κώδικα, πρώτα παίξε το παιχνίδι.

#-------------------------------------------Imports--------------------------------------------------------
import os #used to find the path

from pathlib import Path


#-------------------------------------Lists--------------------------------------

rooms = [ "Βρίσκεσαι στο χωλ.Παραλίγο να σκοντάψεις.",#0
          "Βρίσκεσαι στο σαλόνι.Βλέπεις ένα μαχαίρι με αίμα στο πάτωμα.Η σκάλα είναι δυτικά.",#1
          "Βρίσκεσαι στη σκάλα.Είσαι στον 1ο όροφο.",#2
          "Βρίσκεσαι στο καθιστικό.Όλα είναι φυσιολογικά.",#3
          "Βρίσκεσαι στο 1ο μπάνιο.Βλέπεις σπασμένα μπουκαλάκια, μια βρύση να στάζει.",#4
          "Βρίσκεσαι στον 1ο διάδρομο.Βλέπεις έναν σπασμένο πίνακα στο πάτωμα.",#5
          "Βρίσκεσαι στην τραπεζαρία.",#6
          "Βρίσκεσαι στο Spa.",#7
          "Βρίσκεσαι στο 2ο μπάνιο.Μια απαίσια μυροδιά πλημυρίζει το δωμάτιο.",#8
          "Βρίσκεσαι στη βιβλιοθήκη.Μερικά βιβλία έχουν πέσει από τα ράφια τους.",#9
          "Βρίσκεσαι στο βεστιάριο.Μυρίζει ναφθαλίνη.",#10
          "Βρίσκεσαι στο γραφείο.Βλέπεις κάτι πεταμένα χαρτιά στο πάτωμα.",#11
          "Βρίσκεσαι στο 2ο εργαστήριο.",#12
          "Βρίσκεσαι στο 1ο εργαστήριο.Στα ράφια βλέπεις μπουκαλάκια με δοιάφορα παράξενα υγρά.",#13
	      "Είσαι στον διακοσμημένο χώρο.Πάνω στους τοίχους είναι κρεμασμένα μερικά πορτραίτα.",#14
          "Είσαι στο παρατηρητήριο.",#15
          "Είσαι στη 2η βιβλιοθήκη.",#16
          "Είσαι στον 2ο διάδρομο.Όλα είναι φυσιολογικά.",#17
          "Είσαι στη βεράντα.Ακούς τον άνεμο να περνά από τα δέντρα ουρλιάζοντας.\nΒλέπεις μία ετοιμόροπη σκάλα κινδύνου στα δυτικά σου.Αν ανέβεις υπάρει κίνδυνος να πέσεις.",#18
          "Είσαι στο 2ο γραφείο.",#19
          "Είσαι στον 3ο διάδρομο.Βλέπεις στο πάτωμα δύο κηλίδες αίμα.",#20
          "Είσαι στο 1ο υπνοδωμάτιο.Βλέπεις μία μεγάλη κηλίδα αίματος στο πάτωμα.",#21
          "Είσαι στο 2ο υπνοδωμάτιο.",#22
          "Βρίσκεσαι στο 3ο μπάνιο.Βλέπεις έναν σπασμένο καθρέυτη.",#23
          "Βρίσκεσαι στην αίθουσα πινκ πονκ.",#24
          "Έφτασες στην αίθουσα προσωπικών δεδομένων.",#25
          "Έφτασες στην αποθήκη.",#26
          "Έφτασες στην δέυτερη κουζίνα.",#27
          "Έφτασες στην κουζίνα.Αντιλαμβάνεσαι την κίνηση ενός ποντικού.",#28
          "Έφτασες στην σκάλα κινδύνου.Για να ανέβεις στην ταράτσα πήγαινε νότια.",#29
          "Έφτασες στην ταράτσα."]#30

moves = [ [1, -1, -1, 6],#0
          [3, 0, -1, 2],#1
          [24, -1, 1, -1],#2
          [-1, 1, -1, 28],#3
          [-1, -1, -1, 5],#4
          [-1, 28, 4, 10],#5
          [-1, -1, 0, -1],#6
          [8, -1, -1, -1],#7
          [9, 7, -1, -1],#8
          [11, 8, 28, 13],#9
          [-1, -1, 5, -1],#10
          [-1, 9, -1, 12],#11
          [-1, -1, 11, -1],#12
          [-1, -1, 9, -1],#13
          [25, 15, -1, -1],#14
          [14, -1, -1, -1],#15
          [-1, -1, -1, 27],#16
          [20, 27, -1, 19],#17
          [19, -1, 27, 29],#18
          [-1, 18, 17, -1],#19
          [23, 17, 24, 21],#20
          [22, -1, 20, -1],#21
          [-1, 21, 23, -1],#22
          [-1, 20, -1, 22],#23
          [-1, 2, -1, 20],#24
          [-1, 14, -1, 24],#25
          [-1, 10, -1, -1],#26
          [17, -1, -1, 18],#27
          [5, -1, 3, 9],#28
          [-1, 30, 18, -1],#29
          [29, -1, -1, -1] ]#30

#============================================================================================================
#------------------------------------------------Functions---------------------------------------------------
#============================================================================================================          

def getInput(moves, room):
    directions = ['β', 'ν', 'α', 'δ']
    destinations = moves[room]
    posibleMoves = []
    index = 0
    print('Εξόδοι: ')
    for i in destinations:
        if i != -1:
            print(directions[index])
            posibleMoves.append(directions[index])
        index += 1
    print('')
    userinput = ''
    while userinput not in posibleMoves:
        userinput = input('Πού θες να πας; ')
    return directions.index(userinput)

def selectAction(room, moves, item): #select the action from{κ, χ, ε, φ, α, κωδ}
    global book1
    global book2
    global book3
    global item1
    global item2
    global item3
    global lastbook
    global paper
    global ticket
    global passage
    global cage
    global door
    global ite
    global act
    global first_save
    global used_handle
    global used_rope
    item = ite
    
    if item == 0:
        print('Ενέργειες = κ(κίνηση), χ(χρήση), α(αντικείμενα), ε(αποθήκευση και έξοδος), φ(επαναφορά).')
        action = input('Τί ενέργεια θα κάνεις; ')
        i = 0
        while i != 10:
            if action == 'κ' and item == 0: #move
                direction = getInput(moves, room)
                destinations = moves[room]
                room = destinations[direction]
                return room
                
                        
                
            if action == 'χ' and item == 0: #use an item
                
                if handle == True and room == 30 and used_handle == False:
                    hfl = moves[27]
                    hfl[2] = int(16)
                    print('Βάζεις την λαβή στο άνοιγμα του μοχλού και τραβάς.')
                    print('Ακούς έναν θόρυβο που γίνεται σε ένα άλλο μέρος του σπιτιού.\nΈνα μυστικό πέρασμα ανοίγει κάπου αλλού.\n')
                    used_handle = True
                    return room
                    
                    
                if item1 == True and room == 10 and passage == False:
                    passage = True
                    des = moves[10]
                    des[0] = int(26)
                    pas = moves[26]
                    pas[1] = int(10)
                    room = 10
                    print('Άνοιξες μια καταπακτή με το πιρούνι.Για να μπείς πήγαινε βόρεια.\n')
                    return room
                    
                #print(item2, room, door)    
                if item2 == True and room == 24 and door == False:
                    door = True
                    rom = moves[24]
                    rom[2] = 25
                    print('Άνοιξες την κλειδωμένη πόρτα με το κλειδί! Για να μπείς πήγαινε ανατολικά.\n')
                    return room
                    

                if item3 == True and room == 8 and paper == False:
                    paper = True
                    print('Επιασες το χαρτί.Γράφει έναν αριθμό:9136.\n')
                    return room
                    

                if  room == 18  and used_rope == False and rope == True: 
                    print('Έδεσες την σκάλα γερά. Τώρα μπορείς να περάσεις άφοβα.\n')
                    used_rope = True
                    return room
                
            if action == 'κωδ' and room == 25 and item == 0: #password
                passwo = input('Δώσε τον κωδικό: ')
                if passwo == '9136':
                    cage = True
                    lastbook = True
                    print('Άνοιξες το χρηματοκιβώτιο!Βρήκες ένα ημερολόγιο.\n')
                    return room
                else:
                    print('Λάθος κωδικός.')
                    action = input('Τί ενέργεια θα κάνεις; ')
                    continue

            if action == 'ε' and item == 0: #save
                if first_save == True:
                    ensurance = input('Αποθηκέυοντας το σημείο που βρίσκεσαι χάνεις κάθε προηγούμενη αποθήκευση.\nΕίσαι σίγουρος οτί θέλεις να αποθηκέυσεις(πίσω:ο, συνέχεια:ν);')
                else:
                    ensurance = 'ν'
                    
                if ensurance == 'ν' or first_save == False:
                    first_save = False
                    r = room
                    file = open(save_file_path, 'w')
                    file.truncate()
                    file.write(str(room))
                    file.write('\n')
                    file.write(str(item1))
                    file.write('\n')
                    file.write(str(item2))
                    file.write('\n')
                    file.write(str(item3))
                    file.write('\n')
                    file.write(str(book1))
                    file.write('\n')
                    file.write(str(book2))
                    file.write('\n')
                    file.write(str(book3))
                    file.write('\n')
                    file.write(str(lastbook))
                    file.write('\n')
                    file.write(str(paper))
                    file.write('\n')
                    file.write(str(rope))
                    file.write('\n')
                    file.write(str(handle))
                    file.write('\n')
                    file.write(str(door))
                    file.write('\n')
                    file.write(str(passage))
                    file.write('\n')
                    file.write(str(cage))
                    file.write('\n')
                    file.write(str(used_handle))
                    file.write('\n')
                    file.write(str(used_rope))
                    file.write('\n')
                    file.write(str(first_save))
                    file.write('\n')
                    file.close()
                    print('Saved...')
                    endgame = True
                    room = 'e'
                    return room
                elif ensurance == 'ο':
                    pass


            if action == 'φ': #load
                act = 112
                return room
                
            
            if action == 'α' and item == 0: #αντικείμενα
                if book1 == True:
                    print('\nΚείμενο 1ου ημερολογίου: ', text1)
                if book2 == True:
                    print('\nΚείμενο 2ου ημερολογίου: ', text2)
                if book3 == True:
                    print('\nΚείμενο 3ου ημερολογίου: ', text3)
                if lastbook == True:
                    print('\nΚείμενο προσωπικού ημερολογίου: ', lastText)
                print('') #to leave a space
                if paper == True:
                    print('Κείμενο χαρτιού: 9136.')
                if item1 == True:
                    print('Έχεις βρεί το πιρούνι.')
                if item2 == True:
                    print('Έχεις βρεί το κλεδί.')
                if item3 == True:
                    print('Έχεις βρεί τη σκούπα.')
                if rope == True:
                    print('Έχεις βρεί το σχοινί.')
                if handle == True:
                    print('Έχεις βρεί τη λαβή.')
                if (book1 and book2 and book3 and lastbook and item1 and item2 and item3) == False:
                    print('Δεν έχεις βρεί κανένα άλλο αντικείμενο.\n')
                return room
                
            else:
                action = input('Τί ενέργεια θα κάνεις; ')
                continue
        else:
            return room

#==========================================================================================================
#------------------------------------------------Variables-------------------------------------------------
#==========================================================================================================

room = 0
endgame = False
item1 = False  #πιρούνι
item2 = False  #κλειδί
item3 = False  #σκούπα
book1 = False  #1ο ημερολόγιο
book2 = False  #2ο ημερολόγιο
book3 = False  #3ο ημερολόγιο
lastbook = False  #προσωπικό ημερολόγιο
paper = False  #χαρτί
door = False  #πόρτα
rope = False  #σχοινί
handle = False  #λαβή

ite = 0
act = 0
des = moves[10]
pas = moves[26]
rom = moves[24]
hfl = moves[27]

passage = False  #μονοπάτι βεστιάριο-αποθήκη
cage = False  #χρηματοκιβώτιο
used_handle = False  #χρήση μοχλού
used_rope = False  #χρήση σχοινιου

first_save = True #η πρώτη φορά αποθήκευσης

save_file_path = str(os.path.dirname(os.path.realpath(__file__)) + '/save.txt')
review_file_path = str(os.path.dirname(os.path.realpath(__file__)) + '/review.txt')

path = Path(str(os.path.dirname(os.path.realpath(__file__)) + '/save.txt'))


text1 = 'John Inbet,\nΤην νύχτα της δολοφόνίας βρισκόμουν σε ένα επαγκελματικό\nταξίδι, πολύ μακριά από εδώ, στην Νέα Υόρκη,από τις 7/7/2015.'

text2 = 'Nick Dumpler, \nΕίχα πάει για μπόουλινγκ κοντά στο σπίτι του Α.Γ.Νόστου. Είχαμε ένα κόλπο:\nΕίχαμε φτιάξει μία μπάλα που κινείται μόνη της και με καθοδηγούσε από ένα μικρόφωνο που είχα στα μαλιά μου.\nΞαφνικά σταμάτησε να μου μιλάει. \nΠήγα στο σπίτι του για να δώ αν ήταν καλά, αλλά όταν έφτασα στο σπίτι του είδα μόνο το πτώμα του.\nΕίχε πεθάνει.' #2ο ημερολόγιο-κείμενο

text3 = 'Andrew Plemer,\nΔυστυχώς δεν μπόρεσα να πάω στην κηδία τού φίλου μου Α.Γ.Νόστου.\nΉμουν στο νοσοκομείο και είχα μια σοβαρή εγχείρηση.' #3ο ημερολόγιο-κείμενο

lastText = '7/7/2015\nΠήγα να δώ τον φίλο μου Andrew Plemer.Ήταν στο νοσοκομείο και είχαι μια εγχείρηση.\nΗταν τόσο χάλια που δέν μπορούσε ούτε να μιλήσει.\n \n8/7/2015\n(Πρωί)Άρχισα να ετοιμάζομαι για το ταξίδι που θα έκανα με τον John Inbet στις(--καμένη σελίδα--)\nΕίχα αρχίσει να υποπτέυομαι οτί κάποιος ήθελε να το κακό μου.' #πρωοπικό ημερολόγιο-κείμενο


#=============================================================================================================
#------------------------------------------------Start adventure----------------------------------------------
#=============================================================================================================

print('---------------------------------------Immersed in the darkness--------------------------------------------')
print('Tips:\nΝα διαβάζεις προσεκτικά τα δεδομένα που σου δίνονται πρίν προχωρήσεις.\nΣτα περισσότερα δωμάτια βλέπεις κάποια διακοσμητικά αντικείμενα\nή νιώθεις μερικά πράγματα τα οποία δεν βοηθάνε στην λύση του μυστηρίου.')
print('The adventure starts.')
print('\n2015\n')
print('Είσαι ένας ντεντέκτιβ.\n')
print('Α.Γ.Νοστος:Δολοφονήθηκε στις 8/7/2015 την στιγμή που είχε μια κλήση με κάποιον ή κάποιους.')
print('Υπάρχουν 3 υπόπτοι.')
print('Ο κάθε ύποπτος έχει αφήσει ένα ημερολόγιο που δίνει κάποια στοιχεία.')
print('Η αποστολή σου είναι να βρείς τον δολοφόνο με τα στοιχεία που σου δίνονται.')
print('Πάς στο σπίτι που έγινε η δολοφονία.\n')
print('Μπορείς να κινηθείς: β = βόρεια, ν = νότια, α = ανατολικά, δ = δυτικά.\n')

#------------------------------------------------Main program----------------------------------------------
#==========================================================================================================
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

while endgame != True:
    if room == 'e': #when save room = e
        break

    if act == 112: #load
        if path.is_file() == True:
            print('\nloading...')
            file = open(save_file_path, 'r')
            room = int(file.readline())
            item1 = file.readline()
            item2 = file.readline()
            item3 = file.readline()
            book1 = file.readline()
            book2 = file.readline()
            book3 = file.readline()
            lastbook = file.readline()
            paper = file.readline()
            rope = file.readline()
            handle = file.readline()
            door = file.readline()
            passage = file.readline()
            cage = file.readline()
            used_handle = file.readline()
            used_rope = file.readline()
            first_save = file.readline()
            file.close()
            ite = 0
            act = 0

            if item1 == 'True\n':
                item1 = True
            else:
                item1 = False
            if item2 == 'True\n':
                item2 = True
            else:
                item2 = False
            if item3 == 'True\n':
                item3 = True
            else:
                item3 = False
            if book1 == 'True\n':
                book1 = True
            else:
                book1 = False
            if book2 == 'True\n':
                book2 = True
            else:
                book2 = False
            if book3 == 'True\n':
                book3 = True
            else:
                book3 = False
            if lastbook == 'True\n':
                lastbook = True
            else:
                lastbook = False
            if paper == 'True\n':
                paper = True
            else:
                paper = False
            if rope == 'True\n':
                rope = True
            else:
                rope = False
            if handle == 'True\n':
                handle = True
                #print(cage)
            else:
                handle = False
            if door == 'True\n':
                door = True
            else:
                door = False
            if passage == 'True\n':
                passage = True
            else:
                passage = False
            if cage == 'True\n':
                cage = True
            else:
                cage = False
            if used_handle == 'True\n':
                used_handle = True
            else:
                used_handle = False
            if used_rope == 'True\n':
                used_rope = True
            else:
                used_rope = False
            if first_save == 'True\n':
                first_save = True
            else:
                first_save = False
            print('Το παιχνίδι είναι έτοιμο από εκεί που το είχες αφήσει!\n') #here load finishes
        else:
            print('\nΔεν υπάρχει προηγούμενη αποθήκευση.\n')
            ite = 0
            act = 0
            continue

    if (book1 and book2 and book3 and lastbook) == True:
            print('Έχεις όλα τα στοιχεία που χρειάζεσαι για να βρείς τον ένοχο:\n')
            print('\nΚείμενο 1ου ημερολογίου:',text1)
            print('\nΚείμενο 2ου ημερολογίου:',text2)
            print('\nΚείμενο 3ου ημερολογίου:',text3)
            print('\nΚείμενο προσωπικού ημερολογίου: ', lastText)
            bad = input("\nΠοιός είναι ο ένοχος('j'=J.Inbet, 'n'=N.Dumpler, 'a'=A.Plemer); ")
            i = True
            while i == True:
                if bad == 'j':
                    print('Μπράβο, νίκησες!!!')
                    print('Ο ένοχος πήγε στην φυλακή και είσαι ζωντανός, θα μπορούσες να είχες πεθάνει σε αυτή την αποστολή.')
                    endgame = True
                    i = False
                elif bad == 'n' or 'a':
                    print('Πας στο σπίτι των υπόπτων για να τους πληροφορήσεις σχετικά, αλλά όταν πας\n στο σπίτι του J.Inbet σε σκοτώνει, επειδή αυτός είναι ο πραγματικός ένοχος.')
                    print('Έχασες, η περιπέτεια τελείωσε!')
                    endgame = True
                    i = False
                else:
                    print('Λάθος γράμμα, προσπάθησε ξανά: ')
                


    elif room != 112 or ite != 1:
        print(rooms[room])
        if room == 25:
            if cage == False and lastbook == False:
                print('Βλέπεις ένα κλειδωμένο χρηματοκιβώτιο. Για να ανοίξει χρειάζεται κωδικό.')
                print('Μπορείς να χρησιμοποιήσεις την ενέργεια "κωδ"(κωδικός) για να βάλεις τον κωδικό στο χρηματοκιβώτιο.\n')
                room = selectAction(room, moves, 5)
            if cage == True:
                if lastbook == False:
                    print('Βρήκες το προσωπικό ημερολόγιο του θύματος.\n')
                    room = selectAction(room, moves, 0)
                if lastbook == True:
                    room = selectAction(room, moves, 0)
            

        elif room == 27:
            if used_handle == True:
                if hfl[2] != 16:
                    hfl[2] = int(16)
                print('Στα ανατολικά σου βλέπεις ένα άνοιγμα.\n')
                
            else:
                print('Ο τοίχος φαίνεται λίγο παράξενος.\nΣαν να υπάρχει ένα μυστικό πέρασμα.\n')
            room = selectAction(room, moves, 0)
            continue

        elif room == 29 and used_rope == False:
            print('Η ετοιμόρροπη σκάλα δεν άντεξε το βάρος σου και έπεσε.')
            print('Έχασες, η περιπέτεια τελείωσε.\n')
            break

        elif room == 4 and rope == False:
            rope = True
            print('Πήρες ένα σχοινί.\n')
            room = selectAction(room, moves, 0)

        elif room == 13 and handle == False:
            handle = True
            print('Βρήκες μία λαβή μοχλού.\n')
            
            room = selectAction(room, moves, 0)

        elif room == 6 and item1 == False:
            item1 = True
            print('Βρήκες ένα πιρούνι.\n')
            room = selectAction(room, moves, 0)

        elif room == 10:
            if passage == False:
                print('Βλέπεις μία καταπακτή αλλά δεν μπορείς να την ανοίξεις.')
            else:
                print('Βλέπεις το άνοιγμα της καταπακτής βόρεια.\n')
                if des[0] != int(26):
                    des[0] = int(26)
            room = selectAction(room, moves, 0)

        elif room == 24:
            if door == False:
                print('Στο βάθος της αίθουσας βλέπεις μία κλειδωμένη πόρτα.')
                room = selectAction(room, moves, 0)
            if door == True:
                if door == True:  
                    if rom[2] != 25:
                        rom[2] = 25
                room = selectAction(room, moves, 0)


            
        elif room == 26 and item2 == False:
            item2 = True
            print('Βρήκες ένα κλειδί.')
            room = selectAction(room, moves, 0)
            
        elif room == 12 and book1 == False:
            book1 = True
            print('Βρήκες το πρώτο ημερολόγιο.')
            room = selectAction(room, moves, 0)

        elif room == 8 and paper == False:
            print('Βλέπεις ένα χαρτί κάτω από ένα έπιπλο.Θα χρειαστείς κάτι μακρύ για να το πιάσεις.')
            room = selectAction(room, moves, 0)

                    
        elif room == 15 and book2 == False:
            book2 = True
            print('Βρήκες το δεύτερο ημερολόγιο.')
            room = selectAction(room, moves, 0)

        elif room == 16 and book3 == False:
            book3 = True
            print('Βρήκες το τρίτο ημερολόγιο.')
            room = selectAction(room, moves, 0)

        elif room == 22 and item3 == False:
            item3 = True
            print('Βρήκες μία σκούπα.')
            room = selectAction(room, moves, 0)

        elif room == 30 and used_handle == False:
            print('Βλέπεις μία έναν μοχλό αλλά του λείπει η λαβή.')
            room = selectAction(room, moves, 0)

        else:
            room = selectAction(room, moves, 0)
    else:
        continue

#================================================================================================================
#---------------------------------------------------game finished------------------------------------------------
#================================================================================================================

if room != 'e':
    print('-------------------------------------The game finished------------------------------------------')
    print('Ενα παιχνίδι του Μιχάλη Γρίβα.\n')
    evaluation = input("Αξιολογήστε το παιχνίδι με ('γ'=κακό, 'β'=καλό, 'α'=πολύ καλό): ")
    f = open(review_file_path, 'w')
    f.write(evaluation)
    f.close()

    if evaluation == 'γ':
        print('Μπρρρρρρρρ, η γιαγιά μου παίζει καλύτερα.')
    elif evaluation == 'β':
        print('Χμμμ, Τυχαία κέρδισες.')
    elif evaluation == 'α':
        print('Ευχαριστώ πολύ αν και δεν είναι και κανένα φοβερό παιχνίδι.')
    else:
        pass
