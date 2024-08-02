##Archived messages

def unsent_messages(short_msg, sent_msg):
    """Pass msgs"""
    while short_msg:
        current_msgs = short_msg.pop()
        print(f"(Sending messages: {current_msgs})")
        sent_msg.append(current_msgs)
#        greeting = f"This is your text {unsent}"
#        print (greeting)

def show_msgs(sent_msg):
        """test"""
        print("\nThe following has been printed:")
        for sent_message in (sent_msg):
            print(sent_message)

short_msg = ['the', 'text', 'message']
sent_msg = []
unsent_messages(short_msg[:], sent_msg)
print(f"{short_msg}")
show_msgs(sent_msg)