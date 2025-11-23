import random
from collections import Counter
import time

all_card_type = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
joker_card_type = random.choice(all_card_type)
card_list = [card for card in all_card_type if card != joker_card_type] + all_card_type
random.shuffle(card_list)

your_card_list = card_list[:12]
emergy_card_list = card_list[12:]

def card_remove(card_list):
    card_num = Counter(card_list)
    new_card_list = [card for card in card_num.keys() if card_num[card] == 1]
    return new_card_list

your_card_list = card_remove(your_card_list)
emergy_card_list = card_remove(emergy_card_list)

while True:
    print(f"您率先抽卡！\n您的卡牌为：\n{your_card_list}\n对方的卡牌序号为：\n{[card_NO + 1 for card_NO in range(len(emergy_card_list))]}")
    time.sleep(1)
    choice_num = input("请输入您要抽取的对方卡牌序号：")
    choice_card = emergy_card_list[int(choice_num) - 1]
    time.sleep(1)
    print(f"您抽到的卡牌是：{choice_card}")
    time.sleep(1)
    if choice_card in your_card_list:
        your_card_list.remove(choice_card)
        print("恭喜您成功消除了一张卡牌")
    else:
        your_card_list.append(choice_card)
        print("很遗憾您未能消除卡牌")
    time.sleep(1)
    if len(your_card_list) == 0:
        print("您消除了所有的手牌，恭喜您获得了胜利！")
        break
    if len(emergy_card_list) == 0:
        print("对方消除了所有的手牌，对方获胜了")
        break

    print("现在轮到对方抽卡")
    time.sleep(1)
    choice_card = random.choice(your_card_list)
    your_card_list.remove(choice_card)
    print(f"对方抽走了您的{choice_card}卡")
    time.sleep(1)
    if choice_card in emergy_card_list:
        emergy_card_list.remove(choice_card)
        print("对方成功消除了一张卡牌")
    else:
        emergy_card_list.append(choice_card)
        print("对方未能消除卡牌")
    if len(your_card_list) == 0:
        print("您消除了所有的手牌，恭喜您获得了胜利！")
        break
    if len(emergy_card_list) == 0:
        print("对方消除了所有的手牌，对方获胜了")
        break

    random.shuffle(emergy_card_list)
    time.sleep(1)
    print("又轮到您的回合了！")

print(f"这局的鬼牌是{joker_card_type}")
