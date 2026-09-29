from feedback import feedbacks
from leader import leaders

def compare_leaders():
    print("==========LEADER COMPARISON========")
    
    for leader in leaders:
        total = 0
        count = 0
        
        for item in feedbacks:
            
            if item["leader"]==leader["name"]:
                     total += item["rating"]
                     count +=1
        if count>0 :
             avg=total/count
        else:
              avg=0
        print("Leader:",leader["name"])
        print("Party:",leader["party"])
        print("Total points:",total) 
        print("Average Rating:",avg)
        print("Rated works:",count)
        print("-----------------------")                   
                        
#compare_leaders()                        