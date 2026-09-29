from works import works
from file_handler import save_feedback,load_feedback
import ast


feedbacks = []
data=load_feedback()
for line in data:
    feedbacks.append(ast.literal_eval(line.strip()))
    


def give_feedback():
    work_id = int(input("enter work ID:"))
    for work in works:
        if work["id"]==work_id:
            
            print("Leader:",work["leader"])
            print("Work:",work["work"])
            print("Area:",work["area"])
            
            rating = int(input("Give rating (1-10):"))     
            feedback = input("enter feedback:")
            #save_feedback(feedbacks[-1])
            feedbacks.append({
                "work_id":work_id,"leader":work["leader"],
                "rating":rating,
                "feedback":feedback
                })   
            save_feedback(feedbacks[-1])    
            print("Feedback submitted successfully!")
            break
        else:
            print("work id not found ")
           
            
            
   # give_feedback()            

def view_feedback():
    print("=============FEEDBACK============")
    
    for item in feedbacks:
        print("work ID:",item["work_id"])
        print("Leader:",item["leader"])
        print("Rating:",item["rating"])
        print("Feedback:",item["feedback"])
        
        print("-------------------------")   
        
        
