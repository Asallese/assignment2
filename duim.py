#!/usr/bin/env python3

import subprocess, sys
import argparse



'''
OPS445 Assignment 2
Program: duim.py 
Author: Asallese2 ( Anthony Sallese )
The python code in this file (duim.py) is original work written by
"Student Name". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: 
'''

def parse_command_args():
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="DU Improved -- See Disk Usage Report with bar charts",epilog="Copyright 2023")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    # check the docs for an argparse option to store this as a boolean.
    # add argument for "target". set number of args to 1.
    args = parser.parse_args()
    return args


def percent_to_graph(percent: int, total_chars: int) -> str:

# Check percent
    if not (0 <= percent <= 100):
        raise ValueError("Percent must be between 0 and 100.")
# calculate the filled characters for the bar.    
    filled_chars = round((percent / 100) * total_chars)

# Bar graph symbol
    graph = '#' * filled_chars + ' ' * (total_chars - filled_chars)

# return the graph
    return graph

def call_du_sub(location: str) -> list:
    command = ['du', '-d', '1', location]
# the above argument is going to be ran with subprocess and has been made a method to do so. 
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout.strip().split('\n')
   # "use subprocess to call `du -d 1 + location`, rtrn raw list"
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return []

def create_dir_dict(raw_dat: list) -> dict:
    "get list from du_sub, return dict {'directory': 0} where 0 is size"
    pass

def bytes_to_human_r(kibibytes: int, decimal_places: int=2) -> str:
    "turn 1,024 into 1 MiB, for example"
    suffixes = ['KiB', 'MiB', 'GiB', 'TiB', 'PiB']  # iB indicates 1024
    suf_count = 0
    result = kibibytes 
    while result > 1024 and suf_count < len(suffixes):
        result /= 1024
        suf_count += 1
    str_result = f'{result:.{decimal_places}f} '
    str_result += suffixes[suf_count]
    return str_result

if __name__ == "__main__":
    args = parse_command_args()
    pass

