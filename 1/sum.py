import sys


def calc_fuel(mass: int) -> int:
    return mass//3 - 2


def main():
    if len(sys.argv) != 2:
        print('sum.py <input file>')
        sys.exit(1)

    fuel = 0
    fuel_plus = 0
    extra: int
    raw: str

    with open(sys.argv[1]) as f:
        raw = f.read().strip()

    for line in raw.split('\n'):
        temp = calc_fuel(int(line, 10))
        fuel += temp

        extra = calc_fuel(temp)
        while extra > 0:
            temp += extra
            extra = calc_fuel(extra)
        fuel_plus += temp

    print('Fuel before extra: {}'.format(fuel))
    print('Fuel after extra: {}'.format(fuel_plus))


if __name__ == '__main__':
    main()
