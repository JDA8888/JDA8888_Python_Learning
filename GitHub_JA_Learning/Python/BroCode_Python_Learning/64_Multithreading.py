# Multithreading = Used to perform multiple tasks concurrently (multitasking)
# Good for I/O (Input and Output) bound tasks like reading files or fetching data from APIs
# threading.Thread(target=my_function)

import threading
import time


def walk_dog(first, last_name):
    time.sleep(8)
    print(f"You Finish walking {first} and {last_name}. ")
    
def take_out_trash():
    time.sleep(2)
    print("You take out the trash. ")
    
def get_mail():
    time.sleep(4)
    print("You get the mail. ")
    
walk_dog()
take_out_trash()
get_mail()

chore1 = threading.Thread(target=walk_dog, args=("Leo","Rocketman"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()    
print("All chores are complete.")