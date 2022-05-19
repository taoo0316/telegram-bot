from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey! I am taoo0316 bot based in Singapore!"

    if user_message in ("how are you?","how is it going?"):
        return "Pretty good Sir!"
    
    if user_message in ("Who are you created by?","Who are you?"):
        return "Hey! I am created by Zhu Wentao, a CS student at Yale-NUS College in Singapore."
        
    if user_message in ("time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I don't understand you."