leaders = [
    {"id":1, "name":"Rahul Kumar","village":"Sivpur","party":"Jan Seva Party"},
    {"id":2,"name":"Amit kumar","village":"Sivpur","party":"Gram Seva Party"},
    {"id":3,"name":"Prince singh","village":"Sivpur","party":"Lok Kalayan Party"}
]

def view_leaders():
    print("==========LEADERS=========")
    
    for leader in leaders:
        print("ID:",leader["id"])
        print("name:",leader["name"])
        print("village:",leader["village"])
        print("party:",leader["party"])
        
        print("----------------------------")     
        
        
        
def view_profile():
    leader_id=int(input("Enter your id:"))
    
    for leader in leaders:
        if leader["id"]== leader_id:
            print("\n==========LEADER PROFILE========")
            print("ID:",leader["id"])
            print("name:",leader["name"])
            print("Village:",leader["village"])
            print("Party:",leader["party"])
            return
    print("Leader not found")        