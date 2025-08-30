"""
This Scripts ingests python files with metadata headers and outputs
a corresponding problem file
"""

import argparse

def extract_meta_data(input_file,output_file):
    meta_data = []
    with open(input_file,"r") as f:
        next(f)
        next(f)
        for line in f:
            if(line.strip() == "END DATA"):
                break 
            meta_data.append(line.strip())
            
    
    with open(output_file,"w") as p:
        p.write("\n".join(meta_data))
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract metadata from all files")
    parser.add_argument("input_file", help="Input file for the problem")
    parser.add_argument("output_file", help="Output file with metadata")
    args = parser.parse_args()

    extract_meta_data(args.input_file, args.output_file)
