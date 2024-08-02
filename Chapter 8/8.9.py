##Messages

def show_messages(msgs):
    """Pass msgs"""
    for unsent in msgs:
        greeting = f"This is your text {unsent}"
        print (greeting)

short_msg = ['the', 'text', 'message']
show_messages(short_msg)