with open('day08_input.txt') as file:
    data = file.read().strip()

num_layers = int(len(data) / 150)
min_zeros = 151
for i in range(num_layers):
    curr_indx = i * 150
    layer_data = data[curr_indx:curr_indx + 150]
    zero_count = layer_data.count('0')

    if zero_count < min_zeros:
        res = layer_data.count('1') * layer_data.count('2')
        min_zeros = zero_count

print(res)
