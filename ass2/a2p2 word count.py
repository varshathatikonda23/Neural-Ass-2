from collections import Counter

def calculate_word_counts_per_line(input_filepath, output_filepath):
    """Calculates word counts for each line in an input file and writes them, along with the original lines, to an output file."""

    try:
        with open(input_filepath, 'r') as input_file:
            input_lines = input_file.readlines()

        word_counts_per_line = [(line.strip(), len(line.split())) for line in input_lines]

        with open(output_filepath, 'w') as output_file:
            for line, word_count in word_counts_per_line:
                output_file.write(f"{line}\nWord_Count:\n")
                for word, count in Counter(line.split()).items():
                    output_file.write(f"{word}: {count}\n")
                output_file.write(f"Total_Words: {word_count}\n\n")

        print(f"Word counts along with the original lines written to '{output_filepath}' successfully.")

    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' not found.")
    except IOError as e:
        print(f"Error: An error occurred while reading or writing files: {e}")

if __name__ == "__main__":
    input_filepath = "input.txt"
    output_filepath = "output.txt"
    calculate_word_counts_per_line(input_filepath, output_filepath)
