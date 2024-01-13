import re

def generate_coordinates(input_file, output_file):
    # Read input from the file
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Parse input parameters
    wafer_diameter = int(lines[0].split(':')[1])
    die_size = [int(x) for x in lines[1].split(':')[1].split('x')]
    die_shift_vector = tuple(map(int, re.findall(r'\d+', lines[2])))
    reference_die = tuple(map(int, re.findall(r'\d+', lines[3])))
    die_street_width_height = tuple(map(int, re.findall(r'\d+', lines[4])))
    reticle_street_width_height = tuple(map(int, re.findall(r'\d+', lines[5])))
    dies_per_reticle = [int(x) for x in lines[6].split(':')[1].split('x')]

    # Calculate die index and LLC for each die
    output_data = []
    for i in range(dies_per_reticle[0]):
        for j in range(dies_per_reticle[1]):
            die_index = (i + 1, j + 1)
            llc = (
                reference_die[0] + i * (die_size[0] + reticle_street_width_height[0]) + die_shift_vector[0],
                reference_die[1] + j * (die_size[1] + reticle_street_width_height[1]) + die_shift_vector[1]
            )
            output_data.append((die_index, llc))

    # Write output to the file
    with open(output_file, 'w') as f:
        for entry in output_data:
            f.write(f"{entry[0]}:{entry[1]}\n")

# Example usage
generate_coordinates("Input\Testcase2.txt", "output.txt")
