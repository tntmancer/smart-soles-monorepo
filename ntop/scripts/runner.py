import os
import subprocess
import json

# Assuming this script, ntop file, and json files will be in the same folde
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
exe_path = os.path.join("C:", "Program Files", "nTopology", "nTopology", "nTopCL.exe")
ntop_file_path = os.path.join(current_directory, "RelDensity.ntop")
output_directory = os.path.join(current_directory, "RelDensity")
input_file_name = os.path.join(current_directory, "input{}.json")
output_file_name = os.path.join(output_directory, "out{}.json")


# Input variables in JSON structure
thickness_values = [round(x * 0.1, 1) for x in range(1, 21)] # List of thickness values from 0.1 to 2 with increments of 0.1
cellsize_values = [round(x * 0.5, 1) for x in range(1, 21)] # List of L values from 0.5 to 10 with increments of 0.5

# Iterate over each cell size value
for i, cellsize in enumerate(cellsize_values):
    input_json = {
    "description": "",
    "inputs": [
        {
            "description": "",
            "name": "Output directory",
            "type": "text",
            "value": output_directory
        },
        {
            "description": "",
            "name": "Unit cell",
            "type": "enum",
            "value": 0
        },
        {
            "description": "",
            "name": "L",
            "type": "real",
            "units": "mm",
            "value": 10.0
        },
        {
            "description": "",
            "name": "Unit Cell Size",
            "type": "real",
            "units": "mm",
            "value": cellsize
        },
        {
            "description": "",
            "name": "Thickness",
            "type": "real",
            "units": "mm",
            "values": thickness_values
        }
        ],
    "title": "Relative Density of Walled TPMS"
    }

    # Create input.json file
    input_file_name = input_file_name.format(i + 1)
    with open(input_file_name, 'w') as outfile:
        json.dump(input_json, outfile, indent=4)

    # nTopCL arguments in a list
    arguments = [exe_path] # nTopCL path
    arguments.append("-j") # json input argument
    arguments.append(input_file_name) # json path
    arguments.append("-o") # output argument
    output_file_name = output_file_name.format(i + 1)
    arguments.append(output_file_name) # output json path
    arguments.append(ntop_file_path) # .ntop notebook file path
    arguments.append("-v2")

# nTopCL call with arguments
print("Running nTopCL with input file: {}".format(input_file_name))
print(" ".join(arguments))
output, error = subprocess.Popen(arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

# Print the return messages
print(output.decode("utf-8"))