import random
player_score = 0
comp_score = 0
for game_n in range(10):
    player = int(input("Сделайте ход: 1-Камень 2-Ножницы 3-Бумага "))
    if player == 1:
        print("Ваш ход - камень")
    elif player == 2:
        print("Ваш ход - ножницы")
    elif player == 3:
        print("Ваш ход - бумага")
    else:
        print("Вы выбрали не ту цифру или я вас не понял")
    comp = random.randint(1, 3)
    if comp == 1:
        print("Ход компьютера - камень")
    elif comp == 2:
        print("Ход компьютера - ножницы")
    elif comp == 3:
        print("Ход компьютера - бумага")
    if player == 1 and comp == 2 or player == 2 and comp == 3 or player == 3 and comp == 1:
        print("Вы победили!")
        player_score += 1
        print(f"Мои победы: {player_score}")
    elif player == comp:
        print("Ничья!")
        print(f"Мои победы: {player_score}")
    else:
        print("Вы проиграли")
        comp_score += 1
        print(f"Мои победы: {player_score}")

    if player_score == 3:
        print("Поздравляем вас с победой!")
        break
    elif comp_score == 3:
        print("Игра завершена. Выиграл компьютер")
        break
