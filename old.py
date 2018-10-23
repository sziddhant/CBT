def get_message_old1(inp):
    a, e = '', ''
    for y1 in hello:
        if inp.lower() == y1:
            a = "Hello! :) \nTry Rock paper scisors \nAsk the date or time\nSay toss to flip a coin"
            break
    for y2 in bye:
        if inp.lower() == y2:
            a = "Bye"
            break
    for y3 in HAU:
        if inp.lower() == y3:
            a = "I'm fine, What about you?"
            break
    for y4 in time:
        if inp.lower() == y4:
            k = str(datetime.time(datetime.now()))
            a = "The time is " + k
            break
    for y5 in date:
        if inp.lower() == y5:
            k = str(datetime.date(datetime.now()))
            a = "The date is " + k
            break
    for y6 in RPS:
        if inp.lower() == y6:
            bm = random.choice(RPS)
            a = bm
            if (((inp.lower() == 'rock') and bm == 'scissor') or (inp.lower() == 'paper' and bm == 'rock') or (
                    inp.lower() == 'scissor' and bm == 'paper')):
                a = bm + ',' + "You win"
            elif inp.lower() == bm:
                a = bm + ',' + "It's a tie!"
            else:
                a = bm + ',' + "I win"
            break

    for y6 in toss:
        if inp.lower() == y6:
            bm = random.choice(TOSS)
            a = bm
            break
        for y in info:
            if inp.lower() == y:
                a = "Chat Bot Test is an expertimental chat bot deployed on Facebook Messenger by Siddhant Saoji \nThis bot is currently in devlpoment phase"
                break

    for d in menu_m:
        if inp.lower() == d:
            a = "(Breakfast)Poha Jalebi|| (Lunch)||Plain Rice, Arhar dal, Lauki Chana,Boondi Raita||(Dinner) Jeera Rice, Moong-Masoor Dal,Chhole Bhature"
            break
    for d in menu_t:
        if inp.lower() == d:
            a = "(Breakfast)Uttpam, Sambhar, Coconut Chutney|| (Lunch)||Plain Rice, Dal Tadka, Aloo Matar,Seasonal Fruit Papaya||(Dinner) Fried Rice, Dal Tadka,Manchurian Gravy"
            break
    for d in menu_w:
        if inp.lower() == d:
            a = "(Breakfast)Pyaaz and Azwain Paratha, Aloo Sabji|| (Lunch)||Plain Rice, Arhar dal, Lauki Chana,Boondi Raita,Chhachh||(Dinner) Plain Rice, Arhar Dal,Mix Veg"
            break
    for d in menu_th:
        if inp.lower() == d:
            a = "(Breakfast)Idli / Fried Idli, Sambhar, Coconut Chutney|| (Lunch)||Plain Rice, Yellow Arhar-Moong dal,Kadhi-Pakoda, Black Chana||(Dinner)Plain Rice, Arhar Dal, Red Pumpkin,Gulab Jamun/ Kala Jamun"
            break
    for d in menu_f:
        if inp.lower() == d:
            a = "(Breakfast)Poori Sabji|| (Lunch)||Lemon Rice, Chana Dal, Bhindi Aloo,Banana,Gauva||(Dinner) Plain Rice, Dal Tadka,Paneer / Egg Curry, Ice Cream Cup#"
            break
    for d in menu_s:
        if inp.lower() == d:
            a = "(Breakfast) Aloo Paratha, Dahi, Sauce, Pickle|| (Lunch) Fried Rice, Urad Dal,Veg Kolhapuri||(Dinner) Plain Rice, Dal Fry,Baingan Bharta, Boondi Laddu"
            break
    for d in menu_sun:
        if inp.lower() == d:
            a = "(Breakfast) Masala Dosa, Sambhar, Chutney|| (Lunch)Veg Biryani, Dal Fry, Paalak Aloo,||(Dinner) |Plain Rice, Dal Makhani,Cucumber Raita Paneer / Chicken, Rice Kheer"
            break

    if a == '':
        e = "Sorry this is not supported yet"
    ans = a + e
    print(ans)
    return ans