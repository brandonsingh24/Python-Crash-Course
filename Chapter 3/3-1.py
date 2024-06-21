3-1

friends=['Cloud', 'Barrett', 'vincent', 'Tifa', 'Cid', 'Yuffie']

print(friends[0])
###Just doing some tricks. 
message=f"Sephiroth's opponent in FF7 was {friends[0]} and not {friends[-1]}. \nAlthough, {friends[2].title()} has a compelling case."
print(message)

message2=f"Don't get me wrong, {friends[1]} is still a compelling character"
print(message2)


appendtest=[]
print(appendtest)
appendtest.append('function')
print(appendtest)
appendtest.insert(1, 'covid')
print(appendtest)
appendtest.insert(0, 'vaccine')
print(appendtest)
appendtest.del (0, 'vaccine')