import math


def generate_points(diameter, num_points, angle):
    radius = diameter / 2.0
    angle_rad = math.radians(angle)

    points = []
    for i in range(num_points):
        x = radius * math.cos(angle_rad)
        y = radius * math.sin(angle_rad)
        points.append((round(x, 4), round(y, 4)))
        angle_rad += 2 * math.pi / num_points

    return points


def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    wafer_diameter = float(data[0].split(":")[1].strip())
    num_points = int(data[1].split(":")[1].strip())
    given_angle = float(data[2].split(":")[1].strip())

    return wafer_diameter, num_points, given_angle


def write_output(file_path, points):
    with open(file_path, 'w') as file:
        for point in points:
            file.write(f'({point[0]},{point[1]})\n')


# Example usage
input_file_path = 'Testcase1.txt'
output_file_path = 'output.txt'

wafer_diameter, num_points, given_angle = read_input(input_file_path)
result = generate_points(wafer_diameter, num_points, given_angle)
write_output(output_file_path, result)
