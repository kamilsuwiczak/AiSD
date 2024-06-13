def backpack(volumes, values, capacity, n):
    cost_matrix = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if volumes[i - 1] <= j:
                cost_matrix[i][j] = max(values[i - 1] + cost_matrix[i - 1][j - volumes[i - 1]], cost_matrix[i - 1][j])
            else:
                cost_matrix[i][j] = cost_matrix[i - 1][j]

    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if cost_matrix[i][j] != cost_matrix[i - 1][j]:
            selected_items.append(i - 1)
            j -= volumes[i - 1]
        i -= 1

    return cost_matrix[n][capacity], selected_items[::-1]

def backpack_bruteforce(volumes, values, capacity, n):
    def bruteforce(i, c, selected_items):
        if i == n:
            return 0, selected_items
        if volumes[i] > c:
            return bruteforce(i + 1, c, selected_items)
        else:
            value1, selected_items1 = bruteforce(i + 1, c - volumes[i], selected_items + [i])
            value1 += values[i]
            value2, selected_items2 = bruteforce(i + 1, c, selected_items)
            if value1 > value2:
                return value1, selected_items1
            else:
                return value2, selected_items2
    
    return bruteforce(0, capacity, [])

def main():
    with open("data.txt") as f:
        C = int(f.readline())
        n = int(f.readline())
        volumes = []
        values = []
        for line in f:
            v, c = map(int, line.split())
            volumes.append(v)
            values.append(c)

    max_value, selected_items = backpack(volumes, values, C, n)
    print("Pojemność plecaka:", C)
    print("Liczba przedmiotów:", n)
    print("Maksymalna wartość:", max_value)
    print("Spakowane przedmioty:", selected_items) #indexy przedmiotów (od 0)

    print(backpack_bruteforce(volumes, values, C, n) == (max_value, selected_items)) #True :)

if __name__ == "__main__":
    main()