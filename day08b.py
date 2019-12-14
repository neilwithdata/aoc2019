with open('day08_input.txt') as file:
    data = file.read().strip()

num_layers = int(len(data) / 150)
layer_data = []
for i in range(num_layers):
    curr_indx = i * 150
    layer_data.append(data[curr_indx:curr_indx + 150])

img_data = []
for pixel_layer in zip(*layer_data):
    # Find the first non-transparent pixel
    for p in pixel_layer:
        if p != '2':
            img_data.append(' ' if p == '0' else '*')
            break

# we now have the final image data
for i in range(6):
    print(''.join(img_data[25 * i: 25 * (i + 1)]))
