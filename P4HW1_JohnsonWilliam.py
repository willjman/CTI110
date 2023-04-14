#CTI-110
#P4HW1 - Score List
# William Jonnson
#4/14/2023
#

list = []
total = 0

num_of_scores = int(input('How many scores do you want to enter?'))
print()
for x in range(num_of_scores):
    score = float(input('Enter score #{} : '.format(x + 1)))
    while True:
        if score < 0 or score > 100:
            score = float(input('INVALID Score entered!!!!\nScore should be between 0 and 100\nEnter score again:'))
                                
        else:
            list.append(score)
            break
print()

print('----------Results-----------')
print(f'Lowest Score: {min(list)}')
list.remove(min(list))         
print(f'Modified List:' ,list )
avg = sum(list) / 4
print(f'Scores Average:', avg,)
if avg >= 90:
 print('Grade: A')
else:
    if avg > 80:
     print('Grade: B')
    else:
        if avg > 70:
            print('Grade: C')
        else:
             if avg < 70:
               print('Grade: F')
             else:print("you need to do better")
print('-----------------------')   
