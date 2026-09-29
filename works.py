works = [
    {
        "id": 1,
        "leader": "Rahul Kumar",
        "work": "Road Construction & Repair",
        "area": "Main Road, Shivpur",
        "cost": 500000,
        "status":"completed"
       
    },
    {
        "id": 2,
        "leader": "Amit Kumar",
        "work": "School Improvement",
        "area": "Primary School, Shivpur",
        "cost": 300000,
        "status":"completed"
       
    },
    {
       "id":3,
        "leader": "Prince singh",
        "work": "Poor Family Support",
        "area": "Ward 2, Shivpur",
        "cost": 150000,
        "status":"completed"
        
    }
]

def view_works():
    print("=========WORKS=========")
    for work in works:
        print("ID:",work["id"])
        print("Leader:",work["leader"])
        print("Work:",work["work"])
        print("Area:",work["area"])
        print("Cost:",work["cost"])
        print("Status:",work["status"])
        print("-------------------")    
    
  
    
    
    

'''def view_pending_works():
    print("===== PENDING WORKS =====")

    for work in works:
        if work["status"] == "pending":
            print("ID:", work["id"])
            print("Leader:", work["leader"])
            print("Work:", work["work"])
            print("Area:", work["area"])
            print("Cost:", work["cost"])
            print("Status:", work["status"])
            print("--------------------")
            
def view_verified_works():
    print("===== VERIFIED WORKS =====")

    for work in works:
        if work["status"] == "Verified":
            print("ID:", work["id"])
            print("Leader:", work["leader"])
            print("Work:", work["work"])
            print("Area:", work["area"])
            print("Cost:", work["cost"])
            print("--------------------")            
'''

        
def view_my_works():
    work_id = int(input("Enter your id:"))
    
    for work in works:
        if work["id"]== work_id:
            print("\n==========MY WORKS========")
            print("work ID:",work["id"])
            print("name:",work["leader"])
            print("Area:",work["work"])
           
            return
    print("Work not found")        