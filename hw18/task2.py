import osa

RUB = 'RUB'


def get_cost(line):
    params = line.strip().split()
    return {'sum': float(params[1]), 'currency': params[2]}


def get_costs():
    costs = []
    with open('currencies.txt') as f:
        for line in f:
            costs.append(get_cost(line))
    return costs


def get_exchange_rate(currency):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    return client.service.RateNum('', currency, RUB, False)


def get_sum_rub(sum_currency, currency):
    if currency == RUB:
        return sum_currency
    else:
        return sum_currency * get_exchange_rate(currency)


def main():
    costs = get_costs()
    sum_rub = 0
    for cost in costs:
        sum_rub += get_sum_rub(cost['sum'], cost['currency'])
    print('Общая стоимость путешествия в рублях:', round(sum_rub))


main()
