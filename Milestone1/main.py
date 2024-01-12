import math
import numpy as np


def read_input_file(filepath):
    with open(filepath, 'r') as f:
        d1 = [line.strip() for line in f]
    d = []
    for i in d1:
        s = i.split(':')
        d.append(s)
    wd = int(d[0][1])
    np = int(d[1][1])
    a = int(d[2][1])
    return wd, np, a


def distance_between(diameter, n):
    start_point = np.array([0, 0])
    end_point = np.array([diameter / 2, 0])
    step_vector = (end_point - start_point) / (n - 1)
    return step_vector


def find_coordinated(distance, angle):
    x = distance * math.cos(math.radians(angle))
    y = distance * math.sin(math.radians(angle))
    return x, y


def write_output_file(filepath, xy_pairs):
    with open(filepath, 'w') as w:
        for x, y in xy_pairs:
            w.write(f'({x},{y})\n')


def main(filepath):
    diameter, n, ang = read_input_file(filepath)
    dis = distance_between(diameter, n)
    xy_pairs = []
    for i in range(n):
        x, y = find_coordinated(dis[0], ang)
        xy_pairs.append((x, y))
        xy_pairs.append((-x, -y))
        dis = dis + distance_between(diameter, n)
    write_output_file("out.txt", xy_pairs)


if __name__ == "__main__":
    main('Input\Testcase1.txt')
