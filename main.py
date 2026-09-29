from leader import view_leaders,view_profile
from works import view_works,view_my_works
from works import works
from feedback import give_feedback
from feedback import view_feedback
from comparison import compare_leaders
def main_menu():
    print("========================================")
    print("             NETA PARAKH                ")
    print("========================================")
    print("      ")
    print("[1] Public")
    print("[2] Leader")
    print("[3] Admin")
    print("[4] Exit")
def public_menu():
    while True:
     print("\n========PUBLIC PANEL========")
     print("[1] View leader")
     print("[2] View work")
     print("[3] Give feedback")
     print("[4] Compare leader")
     print("[5] Back") 
     choice = input("enter your choice:")
     
     if choice =="1":
        view_leaders()
        
     elif choice =="2":

          view_works()
     elif choice =="3":
         give_feedback()
         #print("give feedback")
     elif choice =="4":
         compare_leaders()
        # print("compare leader")
     elif choice =="5":
         print("Back to main menu")   
         break
     else: 
         print("invalid choice")               
def leader_menu():
    while True:
     print("\n========LEADER PANEL=========")
     print("[1] View profile")
    # print("[2] Add works")
     print("[2] View my works")
     print("[3] Logout") 
     
     choice = input("enter your choice:")
     
     
     if choice =="1":
         view_profile()
          #print("view profile")
     
     elif choice =="2":
         view_my_works()
         #print("view my works")
     elif choice =="3":
          print("logout")
          break
     else: 
         print("invalid choice:")      
    
def admin_menu():
    while True:
     print("\n========ADMIN PANEL==========")
     print("[1] View works")
     print("[2] View feedback")
     print("[3] Logout")       
     choice = input("enter your choice:")
     
     if choice == "1":
        view_works()
        #print("view works")
        
     elif choice == "2":
         view_feedback()
        #print("view feedback")     
     elif choice =="3":
        print("logout")   
        break
     else: 
         print("invalid choice")     
       
while True:
    main_menu()
    
    choice = input("Enter your choice:")
    
    if choice == "1":
     public_menu()
       #print("Welcome to Public Panel")
    elif choice == "2":
        leader_menu()
        
      # print("Welcome to Leader Panel")
    elif choice == "3":
        admin_menu()
       #print("Welcome to Admin Panel")
    elif choice == "4":
       print("Exit")
       break
    else:
       print("Invalid choice")

       