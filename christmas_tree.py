from termcolor import colored
from random import choice

colors = ['yellow', 'red', 'blue', 'grey', 'magenta', 'cyan', 'white']
color = choice(colors)


def air_block():
    return colored(choice('\u2744    '), 'white', attrs=['blink'])


def leaf():
    return colored('*', 'green')


def ornament():
    return colored(choice(['\u06E9', '@']), choice(colors))


def light():
    return colored('\u06F5', choice(colors), attrs=['blink'])


def body_block():
    body_options = [leaf] * 3 + [light] * 2 + [ornament]
    return choice(body_options)()


def christmas_tree(h):
    s = h - 1
    w = 1
    print('𝐻𝒶𝓅𝓅𝓎 𝐻𝑜𝓁𝒾𝒹𝒶𝓎𝓈'.center(2 * h))
    print(colored(' ' * (h - 1) + colored('\u2735'), 'yellow'))
    print(colored(' ' * (h - 1) + colored('^'), 'green'))
    for i in range(h):
        print(colored(''.join(air_block() for _ in range(s)) + ''.join(
            body_block() for _ in range(w)) + ''.join(air_block(
            ) for _ in range(s)), choice(colors)))
        w += 2
        s -= 1
    return ' ' * (h - 2) + '| |'


if __name__ == '__main__':
    height = int(input('How tall? '))
    print(christmas_tree(height))
