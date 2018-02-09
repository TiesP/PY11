import osa


def get_distance_mi(line):
    params = line.strip().split()
    return float(params[1].replace(',', ''))


def get_distances_mi():
    distance_mi = []
    with open('travel.txt') as f:
        for line in f:
            distance_mi.append(get_distance_mi(line))
    return distance_mi


def get_distance_km(distance_mi):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    return client.service.ChangeLengthUnit(distance_mi, 'Miles', 'Kilometers')


def get_distances_km(distances_mi):
    distances_km = []
    for distance_mi in distances_mi:
        distances_km.append(get_distance_km(distance_mi))
    return distances_km


def main():
    distances_mi = get_distances_mi()
    distances_km = get_distances_km(distances_mi)
    print('суммарное расстояние в километрах :', round(sum(distances_km), 2))


main()
