#welp here we go
import pygame

#var
money = 0
rock = 0
monkey = 0
gernade = 0
thomas = 0
cock = 0
russian = 0
fat = 0
money_per_click = 1
frag = False
clock = pygame.time.Clock()
fps = 60

#enter click code
print('\nPress enter to start')
input()
frag2 = 0.0167

#store
while True:
    responce = input('enter clicker:')
    if responce == 'shop':
        print('welcome to the shop if you want to leave just press enter')
        print('to buy somthing just type the firs word of the product')
        print('rock 10$ 1 per click')
        print('monkey 35$ 2 per click')
        print('gernade 157$ 5 per click')
        print('thomas the thermo nucler bomb $420 10 per click')
        print('cock plane $69,000 50 per click')
        print('russian fighter jet $30,000 20 per click')
        print('fat @$$ bomb $74,000 25 per click')
        print('frag granade 1 clicks per sec $20000')
    if responce == 'rock':
        if money > 9:
            money = money-10
            rock = rock + 1
            money_per_click = money_per_click + 1
    if responce == 'monkey':
        if money > 34:
            money = money-35
            monkey = monkey + 1
            money_per_click = money_per_click + 2
    if responce == 'gernade':
        if money > 156:
            money = money-157
            gernade = gernade + 1
            money_per_click = money_per_click + 5
            if responce == 'thomas':
                if money > 419:
                    money = money-420
                    money_per_click = money_per_click + 10
            thomas = thomas + 1
            if responce == 'cock':
                if money > 68999:
                    money = money-69000
                    money_per_click = money_per_click + 50
            cock = cock + 1
            if responce == 'russian':
                if money > 29999:
                 money = money-30000
            russian = russian +1
            money_per_click = money_per_click + 20
            if responce == 'fat':
             if money > 73999:
                money = money-74000
            fat = fat +1
            money_per_click = money_per_click + 25
            if responce == 'frag':
                if money > 19999:
                    money = money -20000
                frag =+ True
    money = money + money_per_click
    clock.tick(fps)
    money = money + frag2

    #rounding out
    round(money)
    
   #printing numbers
    print('money')
    print(round(money))
    print('rock')
    print(rock)
    print('monkey')
    print(monkey)
    print('gernade')
    print(gernade)
    print('cock')
    print(cock)
    print('thomas')
    print(thomas)
    print('russian')
    print(russian)
    print('fat')
    print(fat)
    print('frag')
    print(frag)

#quit code
    if responce == 'quit':
        break