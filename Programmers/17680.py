def solution(cacheSize, cities):
    cache = []
    time = 0
    for city in cities:
        city = city.lower() # 대/소문자 구분 x
        if cacheSize:
            if not city in cache: # 캐시에 도시가 없다면
                if len(cache) == cacheSize: # 캐시 사이즈가 다 찼다면
                    cache.pop(0) # 참조가 오래된 도시부터 pop
                cache.append(city)
                time += 5
            else: # 캐시에 동일한 도시가 있다면 그 도시의 index를 찾아 도시를 pop
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
        else: # 예외처리: cachesize가 0일 경우 miss만 발생하므로 +5
            time += 5
    return time