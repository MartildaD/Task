for tries in range (3):
    guess = input(f"Guess the favorite color {tries}: ")
    favourite_color = 'blue'

    if favourite_color == 'blue':
        print('correct')
        break
    elif color == 'green':
            print('close')
    else:
        print('wrong')
