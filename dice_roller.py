import random

dice_rolls = 2


def main():
    dice_sum = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1, 6)
        # print(f'You rolled a {roll}')
        if roll == 1:
          print(f'You rolled a {roll}, that''s not bad :)')
        elif roll == 6:
          print(f'You rolled a {roll}, you''ll be able to do better next time ;)')
        else:
          print(f'You rolled a {roll}')
        dice_sum += roll  # This means "dice_sum = dice_sum + roll"
    print(f'You have rolled a total of {dice_sum}')


if __name__ == "__main__":
    main()
