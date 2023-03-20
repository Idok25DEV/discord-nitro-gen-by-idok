def gen():
    import random
    import string

    upper_letter = string.ascii_uppercase
    lower_letter = string.ascii_lowercase
    digits = string.digits

    numbertogen = input("How Many Do I Generate? ")
    upper, lower, nums = True, True, True
    all = ""

    if upper:
        all += upper_letter
    if lower:
        all += lower_letter
    if nums:
        all += digits

    length = 23
    amount = numbertogen

    for x in range(int(numbertogen)):
        nitro = ''.join(random.sample(all, length))
        print('discord.gift/' + nitro)

# Hello


gen()


