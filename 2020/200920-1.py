def solution(cacheSize, cities):
    answer = 0
    cache = []
    for citi in cities:
        citi = citi.lower()
        if citi in cache:
            cache.pop(cache.index(citi))
            cache.append(citi)
            answer += 1
        else:
            if len(cache) < cacheSize:
                cache.append(citi)
            else:
                cache = cache[1:] + [citi]
            answer += 5
    return answer

# solution(3,["Jeju","Pangyo","Seoul","NewYork","LA"])

citi = ["j", "a", "e"]

print(citi[1:])