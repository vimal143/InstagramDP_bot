from datetime import datetime


def date_time():
    dt=datetime.now()
    return dt

def sample_responses(input_text):
    user_message=str(input_text).lower()


    if user_message in("hello","hi","hey"):
        return "Hey! what's going on"

    if user_message in("who are you","who r u","who are you?"):
        return "I am InstaDp Downloader boat"

    if user_message in("time","time?",):
        current_dt=date_time()
        return str(current_dt.strftime("%d/%m/%y, %H:%M:%S"))

    
    return "Sorry, I didn't get you"    

            
            