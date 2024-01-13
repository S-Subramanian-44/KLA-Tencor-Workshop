def calculate_die_coordinates(wafer_diameter, die_size, die_shift_vector, reference_die):
    die_width, die_height = die_size
    ref_die_x, ref_die_y = reference_die
    die_shift_x, die_shift_y = die_shift_vector

    # Calculate the number of dies in each direction
    num_dies_x = int(wafer_diameter / die_width)
    num_dies_y = int(wafer_diameter / die_height)

    die_coordinates = []
    llc_coordinates = []

    for i in range(-num_dies_x // 2, num_dies_x // 2 + 1):
        for j in range(-num_dies_y // 2, num_dies_y // 2 + 1):
            die_x = ref_die_x + i + die_shift_x
            die_y = ref_die_y + j + die_shift_y

            die_coordinates.append((i + 1, j + 1))
            llc_coordinates.append((die_x * die_width, die_y * die_height))

    return die_coordinates, llc_coordinates


def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    wafer_diameter = int(lines[0].split(":")[1].strip())
    die_size = tuple(map(int, lines[1].split(":")[1].strip().split("x")))
    die_shift_vector = tuple(map(int, lines[2].split(":")[1].strip()[1:-1].split(",")))
    reference_die = tuple(map(int, lines[3].split(":")[1].strip()[1:-1].split(",")))

    return wafer_diameter, die_size, die_shift_vector, reference_die


def write_output(file_path, die_coordinates, llc_coordinates):
    with open(file_path, 'w') as file:
        for die, llc in zip(die_coordinates, llc_coordinates):
            file.write(f"({die[0]},{die[1]}):({llc[0]},{llc[1]})\n")


if __name__ == "__main__":
    input_file_path = "Input\Testcase2.txt"
    output_file_path = "output.txt"

    wafer_diameter, die_size, die_shift_vector, reference_die = read_input(input_file_path)

    die_coordinates, llc_coordinates = calculate_die_coordinates(
        wafer_diameter, die_size, die_shift_vector, reference_die
    )

    write_output(output_file_path, die_coordinates, llc_coordinates)
