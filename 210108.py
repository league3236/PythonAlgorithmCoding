

def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city.lower()
        if city in cache:
            cache.pop(cities.index(city))
            cache.append(city)
            answer += 1
            pass
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                cache = cache[1:] + [city]
            answer += 5
    return answer

array = ['1', '2', '3']
print(array[1:])
