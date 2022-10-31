print("\n\t********************* Hii I am Mind Reader!! ****************************\n")
print("\n\tThink about any of the given character and I will try to guess who it is : \n")
print(" 1.Arijit Singh \n 2.Alia Bhatt \n 3.Narendra Modi \n 4.Kareena Kapoor \n 5.Tanmay Bhatt\n")
 

import numpy as np

 #characterstics of each person 

def singer(tanmay,alia, karena, arijit, modi):
    arijit += 1
    return np.array([tanmay,alia, karena, arijit, modi])
def actor(tanmay,alia, karena, arijit, modi):
    tanmay += 1
    alia += 1
    karena += 1
    return np.array([tanmay,alia, karena, arijit, modi])
def producer(tanmay,alia, karena, arijit, modi):
    tanmay += 1
    alia += 1
    return np.array([tanmay,alia, karena, arijit, modi])
def comedian(tanmay,alia, karena, arijit, modi):
    tanmay += 1
    return np.array([tanmay,alia, karena, arijit, modi])
def youtuber(tanmay,alia, karena, arijit, modi):
    tanmay += 1
    return np.array([tanmay,alia, karena, arijit, modi])
def male(tanmay,alia, karena, arijit, modi):
    tanmay += 1
    modi += 1
    arijit += 1
    return np.array([tanmay,alia, karena, arijit, modi])
def female(tanmay,alia, karena, arijit, modi):
    alia += 1
    karena += 1
    return np.array([tanmay,alia, karena, arijit, modi])
def politicain(tanmay,alia, karena, arijit, modi):
    modi += 1
    return np.array([tanmay,alia, karena, arijit, modi])
def married(tanmay,alia, karena, arijit, modi):
    karena += 1
    alia += 1
    arijit += 1
    return np.array([tanmay,alia, karena, arijit, modi])
def haveKids(tanmay,alia, karena, arijit, modi):
    karena += 1
    return np.array([tanmay,alia, karena, arijit, modi])
def WonFilmfare(tanmay,alia, karena, arijit, modi):
    alia += 1
    karena += 1
    arijit += 1
    return np.array([tanmay,alia, karena, arijit, modi])
def greater50(tanmay,alia, karena, arijit, modi):
    modi += 1
    return np.array([tanmay,alia, karena, arijit, modi])



#  question realted to character 

a = int(input("Is your character male?\n 1.Yes \n 2.No \n"))
if a == 1:
    one = male(0,0,0,0,0)
elif a == 2:
    one = female(0,0,0,0,0)
else :
    print("Sorry can't find your character :<")
    
b = int(input("Is your character a comedian?\n 1.Yes \n 2.No \n 3.Not Sure \n"))
if b == 1:
    one += comedian(one[0],one[1],one[2],one[3],one[4])
   
c = int(input("Is your character a politician?\n 1.Yes \n 2.No \n 3.Not Sure \n"))
if c == 1:
    one += politicain(one[0],one[1],one[2],one[3],one[4])
    
d = int(input("Is your character a producer?\n 1.Yes \n 2.No \n 3.Not Sure \n"))
if d == 1 or d == 3:
    one += producer(one[0],one[1],one[2],one[3],one[4])
   
e = int(input("Does your character a sings?\n 1.Yes \n 2.No \n 3.Not Sure \n"))
if e == 1 or e==3:
    one += singer(one[0],one[1],one[2],one[3],one[4])
  
f = int(input("Is your character married?\n 1.Yes \n 2.No \n 3.Not Sure \n"))
if f == 1:
    one += married(one[0],one[1],one[2],one[3],one[4])
g = int(input("Does your character have kids?\n 1.Yes \n 2.No \n 3.Not Sure \n"))
if g == 1:
    one += haveKids(one[0],one[1],one[2],one[3],one[4])
h = int(input("Does your character have won filmfare?\n 1.Yes \n 2.No \n"))
if h == 1:
    one += WonFilmfare(one[0],one[1],one[2],one[3],one[4])
i = int(input("Is your character older than 50 years?\n 1.Yes \n 2.No \n 3.Not Sure \n"))
if i == 1:
    one += greater50(one[0],one[1],one[2],one[3],one[4])
j = int(input("Is your character an actor?\n 1.Yes \n 2.No \n 3.Not Sure \n"))
if j == 1:
    one += actor(one[0],one[1],one[2],one[3],one[4])


   
#compare the character with highest match of traits


two = np.array(['Tanmay Bhat','Alia Bhatt', 'Karena Kapoor', 'Arijit Singh', 'Narendra Modi'])
print(f"You are thinking of : {two[one.argmax()]}")