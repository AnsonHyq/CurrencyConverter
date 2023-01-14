import requests

cache_rate = dict()
currency_rate = dict()

own_code = input().lower()
url = f'http://www.floatrates.com/daily/{own_code.lower()}.json'
currency_rate = requests.get(url).json()

if own_code != 'usd':
    cache_rate['usd'] = currency_rate['usd']['rate']
if own_code != 'eur':
    cache_rate['eur'] = currency_rate['eur']['rate']

while target_code := input().lower():
    qty = float(input())
    print('Checking the cache...')

    if target_code in cache_rate:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache_rate[target_code] = currency_rate[target_code]['rate']

    print(f'You received {qty * cache_rate[target_code]:.2f} {target_code.upper()}.')
