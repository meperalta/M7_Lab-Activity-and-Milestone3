#Maria Eden Peralta
#Narch 6, 2022
#Milestone 3_Adventure Game Outline: Module Development


print("Hello, Welcome to my first adventure game!")

ans = input('Are you ready to play (yes/no): ')
score = 0
total_q = 5

if ans.lower() == 'yes':
    ans = input('1. What is the most scariest animal in the forest? (lion/bear) ')
    if ans.lower() == 'lion':
        score += 1
        print('correct')
    else:
        print('Incorrect')
        
    ans = input('2. Are you going to fight a lion to save your life? (yes/no) ')
    if ans.lower() == 'yes':
        score += 1
        print('correct')
    else:
        print('Incorrect')

    ans = input('3. How are you going to fight? (shoot/run) ')
    if ans.lower() == 'shoot':
        score += 1
        print('correct')
    else:
        print('Incorrect')


    ans = input('4. The lion roared? (shoot/run) ')
    if ans.lower() == 'shoot':
        score += 1
        print('correct')
    else:
        print('Incorrect')

    ans = input('5. The lion attack you? (shoot/run) ')
    if ans.lower() == 'shoot':
        score += 1
        print('correct')
    else:
        print('Incorrect')

    print('Thank you for playing, you survive!, score, "wins correct move.')
    mark = (score/total_q) * 100

    print("Mark:", str(mark) + '%')

    print("Goodbye")

    
