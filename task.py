import heapq

def min_connection_cost(cables):
    heapq.heapify(cables)  # Перетворюємо список у мін-купу
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)  # Витягуємо найкоротший кабель
        second = heapq.heappop(cables)  # Витягуємо наступний найкоротший
        cost = first + second  # Витрати на їх об'єднання
        total_cost += cost  # Додаємо до загальних витрат
        heapq.heappush(cables, cost)  # Додаємо новий кабель назад у купу
    
    return total_cost

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

def find_min_coins(amount):
    coins = [1, 2, 5, 10, 25, 50]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

def analyze_efficiency():
    import time
    amount = 10000
    
    start = time.time()
    find_coins_greedy(amount)
    greedy_time = time.time() - start
    
    start = time.time()
    find_min_coins(amount)
    dp_time = time.time() - start
    
    print(f"Greedy algorithm time: {greedy_time:.6f} seconds")
    print(f"Dynamic programming time: {dp_time:.6f} seconds")
    
    if greedy_time < dp_time:
        print("Greedy algorithm is faster but may not provide the optimal solution in all cases.")
    else:
        print("Dynamic programming guarantees the optimal solution but takes more time.")

# Приклад використання
cables = [4, 3, 2, 6]
print(min_connection_cost(cables))  # Очікуваний результат: 29

amount = 113
print(find_coins_greedy(amount))  # Очікуваний результат: {50: 2, 10: 1, 2: 1, 1: 1}
print(find_min_coins(amount))  # Очікуваний результат: {50: 2, 10: 1, 2: 1, 1: 1}

# Аналіз ефективності
analyze_efficiency()