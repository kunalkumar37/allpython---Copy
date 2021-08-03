from sys import argv
script, user_name = argv

prompt='>'
print("hi %s , i'm the %s script.." % (user_name, script))
print("i'd like to ask you a few questions..")

print("do you like me %s" % (user_name))

#likes= raw_input(prompt)
likes = input(prompt)


