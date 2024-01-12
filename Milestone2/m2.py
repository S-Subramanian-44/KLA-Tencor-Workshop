import numpy as np


def calculate_die__and_llc(wafer_diameter, die_size, die_shift_vector, distance_from_cow):
    num_dies_x = int(wafer_diameter / (die_size[0] + die_shift_vector[0])) + 1
    num_dies_y = int(wafer_diameter / (die_size[1] + die_shift_vector[1])) + 1

    die_index = []
    die_llc = []

    for i in range(num_dies_x):
        for j in range(num_dies_y):
            die_shift_x = i * die_shift_vector[0]
            die_shift_y = j * die_shift_vector[1]

            die_index.append((i, j))
            die_llc.append((distance_from_cow[0] + die_shift_x, distance_from_cow[1] + die_shift_y))

    return die_index, die_llc


with open('Input/Testcase2.txt', 'r') as f:
    d1 = [line.strip() for line in f]
    d = []
    for i in d1:
        s = i.split(':')
        d.append(s)
    wd = int(d[0][1])
    ds = np.array([int(x) for x in d[1][1].split('x')])
    dsv = np.array([int(x) for x in d[2][1].strip('()').split(',')])
    dfc = np.array([int(x) for x in d[3][1].strip('()').split(',')])

    die_index, die_llc = calculate_die__and_llc(wd, ds, dsv, dfc)

    print("Die Index: ", die_index)
    print("LLC of all valid dies: ", die_llc)

    output_str = ''
    for i, llc in zip(die_index, die_llc):
        output_str += f'({i[0]},{i[1]}):({llc[0]:.1f},{llc[1]:.2f})' + '\n'
    with open('out.txt', 'w') as w:
        output_str = output_str.strip()
        w.write(output_str)
