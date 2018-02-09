import osa


def get_temp_f(line):
    params = line.strip().split()
    return int(params[0])


def get_temps_f():
    temps_f = []
    with open('temps.txt') as f:
        for line in f:
            temps_f.append(get_temp_f(line))
    return temps_f


def get_temp_c(temp_f):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    return client.service.ConvertTemp(temp_f, 'degreeFahrenheit', 'degreeCelsius')


def get_temps_c(temps_f):
    temps_c = []
    for temp_f in temps_f:
        temps_c.append(get_temp_c(temp_f))
    return temps_c


def main():
    temps_f = get_temps_f()
    temps_c = get_temps_c(temps_f)
    print('средняя тем-ра в градусах Цельсия:', round(sum(temps_c) / len(temps_c)))


main()
