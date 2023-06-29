import os

input_directory = os.getcwd()  # Use the current working directory as the input directory
output_file = 'urls.txt'

result = []

# Iterate over files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):  # Check if the file has a .txt extension
        file_path = os.path.join(input_directory, filename)
        with open(file_path, 'r') as file:
            for line in file:
                if 'www.sciencedirect.com' in line:
                    content = line.replace('(', '').replace(')', '').strip()
                    result.append(content)

with open(output_file, 'w') as file:
    for line in result:
        file.write(line + '\n')

print("URLs saved to urls.txt file.")
