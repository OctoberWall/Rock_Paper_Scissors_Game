import utils
import random

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')

while True:
    print("何を出しますか？")
    print("0: グー")
    print("1: チョキ")
    print("2: パー")
    user_input = input("数字を入力してください（qで終了）：")

    if user_input == "q":
        print("ゲームを終了します")
        break

    try:
        player_hand = int(user_input)  # 数字に変換
    except ValueError:
        print("数字を入力してください")
        continue

    if utils.validate(player_hand):
        computer_hand = random.randint(0, 2)

        # プレイヤーの手を表示
        if player_name == '':
            utils.print_hand(player_hand)
        else:
            utils.print_hand(player_hand, player_name)

        # コンピュータの手を表示
        utils.print_hand(computer_hand, 'コンピューター')

        # 勝敗判定
        result = utils.judge(player_hand, computer_hand)
        print('結果は' + result + 'でした')
        print("-" * 20)  # 区切り線
    else:
        print("正しい数値を入力してください")
