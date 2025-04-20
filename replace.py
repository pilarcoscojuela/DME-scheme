import re

# Function to replace large exponents in variable names
# according to the mapping rules for the attack

def replace_exponents(line):
    # Replace Rt and St raised to 4096 with a 'b' suffix
    pattern_rs = r'([RS]t\d{1,2})\^4096'
    line = re.sub(pattern_rs, r'\1b', line)

    # Replace Rt and St raised to 1024 with an 'a' suffix
    pattern_rs = r'([RS]t\d{1,2})\^1024'
    line = re.sub(pattern_rs, r'\1a', line)

    # Replace Xt and Yt squared with a 'b' suffix
    pattern_xy = r'([XY]t\d{1,2})\^2'
    line = re.sub(pattern_xy, r'\1b', line)

    # Remove any exponent on H-variables (e.g., H12^n -> H12)
    pattern_h = r'(H\d{1,3})\^\d+'
    line = re.sub(pattern_h, r'\1', line)

    return line

# Function to process an input file and write the processed output

def process_file(input_file, output_file):
    try:
        # Read all lines from the input file
        with open(input_file, 'r') as f_in:
            lines = f_in.readlines()

        # Write processed lines to the output file
        with open(output_file, 'w') as f_out:
            for line in lines:
                processed = replace_exponents(line)
                f_out.write(processed)

        print(f"File has been processed and saved as {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == '__main__':
    process_file('result.txt', 'result_replaced.txt')
