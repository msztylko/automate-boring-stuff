spam = ['apples', 'bananas', 'tofu', 'cats']

def transform(list):
    out = ''
    for i in range(len(list) - 1):
        print(list[i] + ', ', end='')
    print('and ' + list[-1])


transform(spam)