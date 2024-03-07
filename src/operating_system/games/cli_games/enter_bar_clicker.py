# Welp here we go.

# Var.
money = 0
rock = 0
monkey = 0
gernade = 0
thomas = 0
cock = 0
russian = 0
fat = 0
pc = 0
money_per_click = 1

# Intro message.
print('\n\nEnter Bar Clicker, coded by T. G. M.')
print('Type in "shop" to enter the shop. Type in "quit" to exit the game.')

print('\nPress enter to start')
input()

# Main loop.
while True:
    responce = input('\nEnter Clicker:')
    responce = responce.lower()

    # Store.
    if responce == 'shop':
        print('\n\nWelcome to the shop. If you want to leave just press enter.')
        print('To buy something, type in the full name of the product.')
        print('Rock - costs 10$ - 1$ per click')
        print('monkey - costs 35$ - 2$ per click')
        print('gernade - costs 157$ - 5$ per click')
        print('thomas - costs $420 - 10$ per click')
        print('cock plane - costs $6000 - 100$ per click')
        print('russian fighter jet - costs $15000 - 500$ per click')
        print('fat @$$ bomb - costs $50,000 - 2000$ per click')
        print('python console - costs $250,000 - 100,000$ per click')

    if responce == 'rock':
        if money >= 10:
            money = money - 10
            rock = rock + 1
            money_per_click = money_per_click + 1

    if responce == 'monkey':
        if money >= 35:
            money = money - 35
            monkey = monkey + 1
            money_per_click = money_per_click + 2

    if responce == 'gernade':
        if money >= 157:
            money = money - 157
            gernade = gernade + 1
            money_per_click = money_per_click + 5

    if responce == 'thomas':
        if money >= 420:
            money = money - 420
            money_per_click = money_per_click + 10
            thomas = thomas + 1

    if responce == 'cock plane':
        if money >= 6000:
            money = money - 6000
            money_per_click = money_per_click + 50
            cock = cock + 1
            
    if responce == 'russian fighter jet':
        if money >= 15000:
            money = money - 15000
            russian = russian +1
            money_per_click = money_per_click + 200

    if responce == 'fat @$$ bomb':
        if money >= 50000:
            money = money - 50000
            fat = fat + 1
            money_per_click = money_per_click + 1000

    if responce == 'python console':
        if money >= 250000:
            money = money - 250000
            money_per_click += 100000
            pc += 1

    money = money + money_per_click

    # Round out
    round(money)

    # Print numbers
    print('\n\nmoney')
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
    print('python console')
    print(pc)

# Quit code.
    if responce == 'quit':
        break