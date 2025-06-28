user_name = input('Enter your name: ')
user_age = input('Enter your age: ')

def age_is_right(user_age)-> int:
    try:
        user_age = int(user_age)
        return user_age
    except ValueError:
        print('Invalid age')
        return None


validated_age = age_is_right(user_age)

def true_age(validated_age):
    if 11 <= validated_age <= 14:
        print (f" Агент {user_name} тебе {validated_age} лет")
    elif validated_age % 10 == 1 and validated_age % 100 != 11:
        print (f" Агент {user_name} тебе {validated_age} год")
    elif validated_age % 10 in (2, 3, 4) and not 12 <= validated_age % 100 <= 14:
        print (f" Агент {user_name} тебе {validated_age} года")
    else:
        print (f" Агент {user_name} тебе {validated_age} лет")


print(true_age(validated_age))
