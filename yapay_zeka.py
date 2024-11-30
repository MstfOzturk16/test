import heapq

def tahta_olusturma(tahta):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(tahta[i][j])
            else:
                print(str(tahta[i][j]) + " ", end="")

def gecerli_mi(tahta, satır, sütun, num):
    for x in range(9):
        if tahta[satır][x] == num:
            return False
    for x in range(9):
        if tahta[x][sütun] == num:
            return False
    start_satır, start_sütun = 3 * (satır // 3), 3 * (sütun // 3)
    for i in range(3):
        for j in range(3):
            if tahta[i + start_satır][j + start_sütun] == num:
                return False
    return True

def bos_yer_bulma(tahta):
    for i in range(9):
        for j in range(9):
            if tahta[i][j] == 0:
                return (i, j)
    return None

def heuristic(tahta):
    return sum(satır.count(0) for satır in tahta)

def a_star_sudoku(tahta):
    
    visited = set()
    open_list = []
    
    initial_heuristic = heuristic(tahta)
    heapq.heappush(open_list, (initial_heuristic, 0, tahta))

    sayac = 0

    while open_list:
        f, g, current_tahta = heapq.heappop(open_list)
        tahta_tuple = tuple(tuple(satır) for satır in current_tahta)
        if tahta_tuple in visited:
            continue
        visited.add(tahta_tuple)

        empty = bos_yer_bulma(current_tahta)

        if not empty:
            print(f"buradaki kod {sayac} adım .")
            return current_tahta

        satır, sütun = empty
        for num in range(1, 10):
            if gecerli_mi(current_tahta, satır, sütun, num):
                new_tahta = [satır[:] for satır in current_tahta]
                new_tahta[satır][sütun] = num
                new_g = g + 1
                new_f = new_g + heuristic(new_tahta)
                heapq.heappush(open_list, (new_f, new_g, new_tahta))
                sayac += 1

    print("Çözüm yok.")
    return None

def sudoku_oyun(tahta):
    while True:
        tahta_olusturma(tahta)
        choice = input("Sudoku yu çözümlemek için 'z' tuşlayın: ").lower()        
        if choice == 'z':
            solution = a_star_sudoku(tahta)
            if solution:
                print("Sudoku oyunu çözüldü:")
                tahta_olusturma(solution)
            else:
                print("Çözüm bulunamadı")
            break
        else:
            print("Geçersiz.Tekrar deneyin.")
tahta = [
        [0, 0, 9, 0, 0, 0, 0, 0, 2],
        [8, 7, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 3, 0, 9],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 5, 0, 7, 0, 9, 0],
        [1, 0, 0, 8, 0, 0, 5, 0, 0],
        [4, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 0, 4, 6],
        [0, 8, 0, 0, 1, 0, 0, 0, 0]
]
print("Oyun baslatılıyor")
sudoku_oyun(tahta)
