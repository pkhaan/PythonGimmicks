class Player:  # Τάξη παίκτη
    def __init__(self, name):
        self.name = name  # το όνομα του παίκτη
        self.help = [1, 1]  # λίστα με τις βοήθειες του παίκτη
        self.answersOfPlayer = []  # λίστα με τις απαντήσεις του παίκτη
        self.helpSum = 0  # πλήθος βοηθειών που απομένουν στον παίκτη (αρχικοποίηση)
        self.score = 0  # συνολική βαθμολογία του παίκτη

    def useSkip(self):  # Ακυρώνει τη βοήθεια skip για τον παίκτη
        self.help[0] = 0

    def use5050(self):  # Ακυρώνει τη βοήθεια 50/50 για τον παίκτη
        self.help[1] = 0

    def helpsLeft(self):  # Μετράει και επιστρέφει το πλήθος των βοηθειών που απομένουν στον παίκτη
        self.helpSum = 0
        for i in range(2):
            self.helpSum += self.help[i]
        return self.helpSum

    def giveAnswer(self, q, a):  # Αποθηκεύει την απάντηση που έδωσε ο παίκτης στην αντίστοιχη λίστα
        self.answersOfPlayer.append(a)

    def addPoints(self, points):  # Προσθέτει πόντους στο συνολικό σκορ του παικτη
        self.score = self.score + points
#***************************** ΤΕΛΟΣ ΤΑΞΗΣ Player ***********************************************

#*****************Eκτύπωση ερώτησης και τις αντίστοιχες σε αυτήν απαντήσεις***********************
def printQnA(n):  
    print(questions[n])
    for i in range(4):
        print(str(i+1) + '.', answers[n][i])

#* Συνάρτηση που εκτυπώνει το μενού των επιλογών του χρήστη (απάντηση, skip, 50/50) και επιστρέφει την επιλογή του ****
def printMenu(pl):  
    if players[pl].helpsLeft() == 2:
        print('Πατήστε 1 για να απαντήσετε, 2 για skip, 3 για 50/50:')
        while True:
            ans = int(input())
            if ans == 1:
                # καταχώρηση απάντησης
                return 'answer'
            elif ans == 2:
                # χρήση skip
                players[pl].useSkip()
                return 'skip'
            elif ans == 3:
                # χρήση 50/50
                players[pl].use5050()
                return '5050'
            else:
                print('Επιλέξτε ξανά')
    elif players[pl].helpsLeft() == 1 and players[pl].help[0] == 1:
        print('Πατήστε 1 για να απαντήσετε, 2 για skip')
        while True:
            ans = int(input())
            if ans == 1:
                # καταχώριση απάντησης
                return 'answer'
            elif ans == 2:
                # χρήση skip
                players[pl].useSkip()
                return 'skip'
            else:
                print('Επιλέξτε ξανά')
    elif players[pl].helpsLeft() == 1 and players[pl].help[1] == 1:
        print('Πατήστε 1 για να απαντήσετε, 2 για 50/50')
        while True:
            ans = int(input())
            if ans == 1:
                # καταχώριση απάντησης
                return 'answer'
            elif ans == 2:
                # χρήση 50/50
                players[pl].use5050()
                return '5050'
            else:
                print('Επιλέξτε ξανά')
    elif players[pl].helpsLeft() == 0 and players[pl].help[1] == 0:
        return 'answer'

#** Συνάρτηση που προσομοιώνει τη βοήθεια 50/50 εμφανίζοντας τις μισές απαντήσεις για την δοσμένη ερώτηση
def help5050(q):  
    if correct[q] == 0 or correct[q] == 1:
        # εμφάνιση 2 πρώτων απαντήσεων
        print(questions[q])
        print('1.',answers[q][0])
        print('2.',answers[q][1])
        while True:
            sel = int(input('Επιλέξτε απάντηση (1-2): '))
            if sel == 1 or sel == 2:
                return sel
            else:
                print('Επιλέξτε ξανά')
    elif correct[q] == 2 or correct[q] == 3:
        # εμφάνιση 2 τελευταίων απαντήσεων
        print(questions[q])
        print('3.',answers[q][2])
        print('4.',answers[q][3])
        while True:
            sel = int(input('Επιλέξτε απάντηση (3-4): '))
            if sel == 3 or sel == 4:
                return sel
            else:
                print('Επιλέξτε ξανά')

#** Έλεγχος εγκυρότητας της δοσμένης απάντησης και καταχώριση πόντων στον παίκτη
def checkAnswer(q, a, pl):  
    if correct[q] == a:
        print('Σωστή απάντηση')
        players[pl].addPoints(10)
    else:
        print('Λάθος απάντηση. Η σωστή απάντηση ήταν', answers[q][correct[q]])
        
#********************************************************************************************************
#***************************************** ΚΥΡΙΩΣ ΠΡΟΓΡΑΜΜΑ *********************************************
#********************************************************************************************************

#Αρχικοποίηση λιστών ερωτήσεων και απαντήσεων
questions = []
answers = []

# Άνοιγμα αρχείου ερωτήσεων και απαντήσεων και αρχικοποίηση των αντίστοιχων λιστών
f = open('qna.txt', 'r') 
for i in range(11):
    questions.append(f.readline().rstrip())
    answers.append([])
    for j in range(4):
        answers[i].append(f.readline().rstrip())

f.close()

# Δημιουργία λίστας με στοιχεία τις θέσεις των σωστών απαντήσεων στις παραπάνω ερωτήσεις
correct = []
for i in range(11):
    for j in range(4):
        if 'ΣΩΣΤΗ' in answers[i][j]:
            answers[i][j] = answers[i][j].replace(' ΣΩΣΤΗ', '')
            correct.append(j)

# Εκτύπωση οδηγιών
print('------- ΟΔΗΓΙΕΣ -------')
print("""Καλωσορίσατε στο παιχνίδι ερωτήσεων με θέμα: Γενικές Γνώσεις. 
Στο παιχνίδι συμμετέχουν τρεις παίκτες. 
Κάθε παίκτης απαντάει σε 10 ερωτήσεις.
Κάθε παίκτης έχει δύο βοήθειες: το skip και το 50/50.""")

# Αρχικοποίηση παικτών
print('------- ΕΙΣΑΓΩΓΗ ΟΝΟΜΑΤΩΝ -------')
players = []
for i in range(3):
    name = input('Εισάγετε το όνομα του ' + str(i + 1) + 'ου παίκτη: ')
    players.append(Player(name))

# Κύριο loop 10 ερωτήσεων για κάθε παίκτη
for i in range(10):
    print('------- ', i + 1, 'η ΕΡΩΤΗΣΗ -------')
    # Loop που προτρέπει κάθε παίκτη να παίξει
    for j in range(3):
        print('------- ', j + 1, 'ος ΠΑΙΚΤΗΣ(', players[j].name, ') -------')
        # Εμφάνιση ερώτησης και απαντήσεων με χρήση της printQnA(i)
        printQnA(i)
        # Εμφάνιση μενού επιλογών παίκτη (απάντηση, βοήθειες) και καταχώριση της επιλογής του
        selection = printMenu(j)
        if selection == 'answer':
            while True:
                answer = int(input('Επιλέξτε μία απάντηση από τις παραπάνω (1-4): '))
                if 1 <= answer <= 4:
                    break
                else:
                    print('Επιλέξτε ξανά')
            players[j].giveAnswer(i, answer-1)
            checkAnswer(i, answer-1, j)
        elif selection == 'skip':
            printQnA(10)
            selection = printMenu(j)
            if selection == 'answer':
                while True:
                    answer = int(input("Επιλέξτε μία απάντηση από τις παραπάνω (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    else:
                        print('Επιλέξτε ξανά')
                players[j].giveAnswer(10, answer-1)
                checkAnswer(10, answer-1, j)
            elif selection == '5050':
                # κλήση συνάρτησης 50/50
                answer = help5050(10)
                players[j].giveAnswer(i, answer-1)
                checkAnswer(10, answer-1, j)
        elif selection == '5050':
            # κλήση συνάρτησης 50/50
            answer = help5050(i)
            players[j].giveAnswer(i, answer-1)
            checkAnswer(i, answer-1, j)

# Προσαύξηση της βαθμολογίας κάθε παίκτη σύμφωνα με τις βοήθειες που δεν χρησιμοποίησε
for i in range(3):
    players[i].addPoints(players[i].helpsLeft() * 5)

# Εμφάνιση τελικής κατάταξης και νικητή
allScores = [[], []]
print('------- ΤΕΛΙΚΟ ΣΚΟΡ -------')
for i in range(3):
    allScores[0].append(players[i].name)
    allScores[1].append(players[i].score)
	
for i in range(3):
    print(allScores[0][i],':',allScores[1][i], 'ΒΑΘΜΟΙ')

best = max(allScores[1])
if allScores[1].count(best) > 1:
    print('ΔΕΝ ΥΠΑΡΧΕΙ ΝΙΚΗΤΗΣ')
else:
    winner = allScores[0][allScores[1].index(best)]
    print('ΝΙΚΗΤΗΣ Ο', winner, 'ME', best, 'ΒΑΘΜΟΥΣ')

# Τερματισμός
print('------- ΤΕΛΟΣ ΠΑΙΧΝΙΔΙΟΥ -------')
