def save_feedback(feedback):
    file=open("feedback.txt","a")
    file.write(str(feedback)+"\n")
    file.close()

def load_feedback():
    file=open("feedback.txt","r")
    data=file.readlines()
    file.close() 
    return data   
    