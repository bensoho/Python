# age = 10

# if age < 0:
#     print('This can hardly be true!')
# elif age == 1:
#     print("About 14 human years")
# elif age == 2:
#     print('About 22 human years')
# elif age > 2:
#     humanAge = 22 + (age - 2) * 5
#     print('Human years: ', humanAge)

number = 7
guess = -1
print('Guess the number!')
while guess != number:
    guess = int(input('Is it... '))
    if guess == number:
        print('Hooray! You guessed it right! ')
    elif guess < number:
        print('It is not so small... ')
    elif guess > number:
        print('It is bigger... ')
