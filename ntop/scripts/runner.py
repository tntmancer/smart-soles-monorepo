import os
import subprocess
import json

# Constants
EXE_PATH = os.path.join("C:", "Program Files", "nTopology", "nTopology", "nTopCL.exe")
NTOP_FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "RelDensity.ntop")
CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
OUTPUT_DIRECTORY = os.path.join(CURRENT_DIRECTORY, "RelDensity")
INPUT_FILE_TEMPLATE = os.path.join(CURRENT_DIRECTORY, "input{}.json")
OUTPUT_FILE_TEMPLATE = os.path.join(OUTPUT_DIRECTORY, "out{}.json")

# Input variables in JSON structure
THICKNESS_VALUES = [round(x * 0.1, 1) for x in range(1, 21)]  # List of thickness values from 0.1 to 2.0
CELLSIZE_VALUES = [round(x * 0.5, 1) for x in range(1, 21)]  # List of L values from 0.5 to 10.0

def create_input_json(cellsize, index):
    """Creates an input JSON file for nTopCL."""
    input_data = {
        "description": "",
        "inputs": [
            {"description": "", "name": "Output directory", "type": "text", "value": OUTPUT_DIRECTORY},
            {"description": "", "name": "Unit cell", "type": "enum", "value": 0},
            {"description": "", "name": "L", "type": "real", "units": "mm", "value": 10.0},
            {"description": "", "name": "Unit Cell Size", "type": "real", "units": "mm", "value": cellsize},
            {"description": "", "name": "Thickness", "type": "real", "units": "mm", "values": THICKNESS_VALUES}
        ],
        "title": "Relative Density of Walled TPMS"
    }
    input_file = INPUT_FILE_TEMPLATE.format(index + 1)
    with open(input_file, 'w', encoding='utf-8') as outfile:
        json.dump(input_data, outfile, indent=4)
    return input_file

def run_ntopcl(input_file, index):
    """Runs nTopCL with the given input file and generates an output file."""
    output_file = OUTPUT_FILE_TEMPLATE.format(index + 1)
    arguments = [
        EXE_PATH,
        "-j", input_file,
        "-o", output_file,
        NTOP_FILE_PATH,
        "-v2"
    ]
    
    print(f"Running nTopCL with input file: {input_file}")
    print(" ".join(arguments))
    
    # TODO (austin): Need to think about whether we want to use subprocess.Popen or just subprocess.run
    output, error = subprocess.Popen(arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    print(output.decode("utf-8"))

def main():
    """Main function to generate input JSON files and run nTopCL."""
    for i, cellsize in enumerate(CELLSIZE_VALUES):
        input_file = create_input_json(cellsize, i)
        run_ntopcl(input_file, i)

if __name__ == "__main__":
    main()
