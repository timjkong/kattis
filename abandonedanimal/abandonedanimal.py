if __name__ == '__main__':
    n = int(input())
    k = int(input())
    item_stores = {}
    for _ in range(k):
        store, item = input().split()
        store = int(store)
        if item not in item_stores:
            item_stores[item] = set()
        item_stores[item].add(store)
        
    m = int(input())
    sister_items = [input() for _ in range(m)]

    lower_bound = 0
    for i in range(m):
        item_stores[sister_items[i]] = [s for s in item_stores[sister_items[i]] if s >= lower_bound]
        if len(item_stores[sister_items[i]]) > 0:
            lower_bound = max(lower_bound, min(item_stores[sister_items[i]]))

    upper_bound = 10**9
    for i in range(m - 1, -1, -1):
        item_stores[sister_items[i]] = [s for s in item_stores[sister_items[i]] if s <= upper_bound]
        if len(item_stores[sister_items[i]]) > 0:
            upper_bound = min(upper_bound, max(item_stores[sister_items[i]]))
    
    ans = 'unique'
    for i in range(m):
        s = item_stores[sister_items[i]]
        if len(s) < 1:
            ans = 'impossible'
            break
        elif len(s) > 1:
            ans = 'ambiguous'

    print(ans)
    
