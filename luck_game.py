ticket=input('Enter Ticket Number: ')
name=input('enter your name: ')
print('\n please choose the colors given below')
print('1) Red \t 2) Blue \t 3) Black \t 4) Yellow \t 5) Green')

import random

money=500
C=['red', 'blue', 'green', 'yellow', 'black']
i=1
while i<=5:
    color=input('select color: ')
    if color.lower() in C:
        print('')
        print(f'your selection is: ', [color.lower()])
        select = random.randint(1,10)
        if select==1:
            print('Bad Luck! You just lost all your money. Pay to play.')
            money=money-500
            print(f'number is : {select} \t\t | Color : {color.lower()} \t\t|\t\t Balance = 0 \n\n')
            break

        elif select == 2:
            print('WOW You won 600. Play again to win more. ')
            money=money+600
            print(f'Number is : {select} \t\t | Color : {color.lower()} \t\t|\t\t Balance={money} \n\n')
            if money == 0:
                break

        elif select==3:
            print('Biggest luck of the century! YOu just won 1000. Play again to win more!')
            money=money+1000
            print(f'Number is : {select}\t\t | Color : {color.lower}\t\t|\t\t Balance = {money} \n\n')
            if money==0:
                break

        elif select==4:
            print('Amazing! You just won 800. Play again to win more!')
            money=money+800
            print(f'Number is : {select}\t\t | Color : {color.lower}\t\t|\t\t Balance = {money} \n\n')
            if money==0:
                break

        elif select==4:
            print('Amazing! You just won 700. Play again to win more!')
            money=money+700
            print(f'Number is : {select}\t\t | Color : {color.lower}\t\t|\t\t Balance = {money} \n\n')
            if money==0:
                break
        else: 
            print('you just lost 100 as you did not get any lucky number. play again to win more')
            money=money-100
            print(f'Number is : {select}\t\t | Color : {color.lower}\t\t|\t\t Balance = {money} \n\n')
            if money==0:
                break
    else:
        print('Selected color is not available.')

    i = i+1

if i==6:
    print('Game over! Your total is:', money)