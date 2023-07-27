i_num_list = range(1, 11)
s_num_list = list(map(lambda i: str(i) + "番", i_num_list))
print("文字列リスト:", s_num_list)

i_num_llist = range(1, 11)
s_num_list = list(map(lambda i: 2 * i, i_num_list))
print("文字列リスト:", s_num_list)

for e in filter(lambda i: i % 2 == 0, range(1, 11)):
    print(e, end="")

pairs = [
    (2, "down"),
    (1, "up"),
    (4, "charm"),
    (3, "strange"),
    (6, "top"),
    (5, "bottom"),
]

pairs.sort(key=lambda x: x[1])
print(pairs)
