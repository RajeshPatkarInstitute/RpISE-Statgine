name = ['Anuradha','Yojesh','Suhrad']
print('Please enter any letter')
lettersearch=input()
count = 0

for v in range(len(name)):
    for i in range(len(name[v])):
       if lettersearch.lower() in name[v][i] or lettersearch.upper() in name[v][i]:
            count += 1
print(lettersearch,'appeared for',count,'times')


