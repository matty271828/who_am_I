'''
Matthew Maclean: Who am I? Run this script and find out
Created by Matthew Maclean on 27/01/2022
'''
# imports
from os import system, name

# Function will be used to clear the console
def clear():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac and Linux
    else:
        _ = system('clear')

# ------------Create HashTable from scratch to store menu options ---------------------
class HashTable(object):
    # Initiate array with empty values.
    def __init__(self, length=7):
        self.array = [None] * length

    # Define the index for a specific key, for more complexity, a hash function could be used here
    def hash(self, key):
        return int(key)

    # Add a value to array by its key
    def add(self, key, value):
        index = self.hash(key)
        # This index already contain some values. Add to end of list stored in this index.    
        if self.array[index] is not None:
            self.array[index].append([key, value])

        # Index is empty. Initiate a list and append the key-value-pair
        else:
            self.array[index] = []
            self.array[index].append([key, value])

    # Use a key to retrieve a value
    def get(self, key):
        index = self.hash(key)
        # No value found at index
        if self.array[index] is None:
            raise KeyError()
        else:
            # Loop through key-value-pairs and find if key exists. If it does then return its value.
            for kvp in self.array[index]:
                print(kvp[1])          

# ----------------------------- Create and fill hash table -------------------------------------
ht = HashTable()

ht.add(0, "My name is Matthew Maclean. I am an aspiring Software Engineer currently studying at the University of Birmingham."); ht.add(0, "I have a keen interest in all things outer space and in combating climate change."); ht.add(0, "I see this role as a fantastic opportunity to combine these three interests.")
ht.add(1, "I have the following technical skills:"); ht.add(1, "Python (Proficient)"); ht.add(1, "Java (Proficient)"); ht.add(1, "C/C++ (Working Knowledge)"); ht.add(1, "Use of source control")
ht.add(2, "I am motivated by:"); ht.add(2, "Making an impact"); ht.add(2, "Developing my skills"); ht.add(2, "Working with others")
ht.add(3, "My formal education consists of:"); ht.add(3, "University of Birmingham - MSc Computer Science - Predicted distinction"); ht.add(3, "University of Manchester - 2:1 BSc Physics")
ht.add(4, "I have the following work experience:"); ht.add(4, "2.5yrs as a structural engineer at a 10 person consultancy."); ht.add(4, "Developed an engineer's mindset and improved my problem solving skills."); ht.add(4, "Had to learn new skills and concepts quickly to meet frequent project deadlines.");
ht.add(5, "Please find my Github profile at:"); ht.add(5, "https://github.com/matty271828")
ht.add(6, "Email: matthewrossmaclean@gmail.com"); ht.add(6, "Phone: +44 7429 600 755")
        
# ----------------------------- Run menu from here -------------------------------------
run_menu = True
while run_menu == True:
    # Print menu
    print("0 - Who am I?\n1 - Technical skills\n2 - Motivation\n3 - Education\n4 - Professional Experience\n5 - Github\n6 - Contact details\n7 - Exit")

    # Ask for user input
    option = input("Please enter what you would like to learn about\n")
    clear()

    # Retieve users selected option
    if option == "7":
        print("You can contact me using {email address} or {phone number}\nThanks for reading! I hope to hear from you soon!")
        break
    else:
        try:
            ht.get(option)
            print(" ")
        except:
            continue
