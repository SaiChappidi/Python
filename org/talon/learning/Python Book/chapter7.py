import sys


def moon_weight(weight, interval):
    for year in range(1, 16):
        weight = weight + interval
        moon_weight = weight * .165
        print('Year %s Weight is %s' % (year, moon_weight))


moon_weight(30, .25)


def moon_weight(weight, interval, years):
    years = years + 1
    for year in range(1, 6):
        weight = weight + interval
        moon_weight = weight * .165
        print('Year %s Weight is %s' % (year, moon_weight))


moon_weight(90, .25, 5)


def moon_weight():
    print('Please enter your current Earth weight')
    weight = int(sys.stdin.readline())
    print('Please enter the amount your weight might increase each year')
    interval = int(sys.stdin.readline())
    print('Please enter the number of years')
    years = int(sys.stdin.readline())
    years = years + 1
    for year in range(1, years):
        weight = weight + interval
        moon_weight = weight * .165
        print('Year %s Weight is %s' % (year, moon_weight))


moon_weight()
