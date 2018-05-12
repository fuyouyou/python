import random

poker_num = [str(i) for i in range(2,11)]
poke_str = ['A', 'j', 'Q', 'K']
poke_king =['大王', '小王']
print(poker_num)
poker_color =['红', '黑', '方', '花']
pokers =['%s%s' % (i, j) for i in poker_color for j in poker_num + poke_str] + poke_king
print(pokers)
print(len(pokers))
random.shuffle(pokers)
print(pokers)

#斗地主发牌
person_a = pokers[0:51:3]
person_b = pokers[1:51:3]
person_c = pokers2:51:3]
last_3 =pokers[-3:]
print('person_a:', person_a)
print('person_b:', person_b)
print('person_c:', person_c)
[
