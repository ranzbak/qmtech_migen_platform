#!/usr/bin/env python3

import sys
import os
import re
import argparse

def main():
    # Argument parser
    parser = argparse.ArgumentParser()

    # Add arguments to parser
    parser.add_argument("-i", "--input", type=str, required=True, help="Input file")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output file")
    args = parser.parse_args()

    # Debug
    print("Parsed args: {}", args)
    print(args.input)
    print(args.output)

    # Sanity checks
    if args.input == args.output:
        raise Exception("input and output should be different file")

    finput = ''
    foutput = ''
    # Open files
    try:
        finput = open(args.input, "r")
        foutput = open(args.output, "w")

    except IOError:
        print("Check input and output arguments")

    # Do something with the content
    with finput as file:
        input_string = file.read()

    # Translate the pins
    for key in PORT_TO_PIN_35T:
        p = re.compile("\\b" + key + "\\b")
        print("\\b" + key + "\\b")
        if p.match(input_string):
            print("Match")
        input_string = p.sub(PORT_TO_PIN_35T[key], input_string)

    # Write the result
    foutput.write(input_string)




# Translation from the 35T ports to the QMTECH pins
PORT_TO_PIN_35T = {
    # U2
    "B7": "CON_U2:7",
    "A7": "CON_U2:8",
    "B6": "CON_U2:9",
    "B5": "CON_U2:10",
    "E6": "CON_U2:11",
    "K5": "CON_U2:12",
    "J5": "CON_U2:13",
    "J4": "CON_U2:14",
    "G5": "CON_U2:15",
    "G4": "CON_U2:16",
    "C7": "CON_U2:17",
    "C6": "CON_U2:18",
    "D6": "CON_U2:19",
    "D5": "CON_U2:20",
    "A5": "CON_U2:21",
    "A4": "CON_U2:22",
    "B4": "CON_U2:23",
    "A3": "CON_U2:24",
    "D4": "CON_U2:25",
    "C4": "CON_U2:26",
    "C3": "CON_U2:27",
    "C2": "CON_U2:28",
    "B2": "CON_U2:29",
    "A2": "CON_U2:30",
    "C1": "CON_U2:31",
    "B1": "CON_U2:32",
    "E2": "CON_U2:33",
    "D1": "CON_U2:34",
    "E3": "CON_U2:35",
    "D3": "CON_U2:36",
    "F5": "CON_U2:37",
    "E5": "CON_U2:38",
    "F2": "CON_U2:39",
    "E1": "CON_U2:40",
    "F4": "CON_U2:41",
    "F3": "CON_U2:42",
    "G2": "CON_U2:43",
    "G1": "CON_U2:44",
    "H2": "CON_U2:45",
    "H1": "CON_U2:46",
    "K1": "CON_U2:47",
    "J1": "CON_U2:48",
    "L3": "CON_U2:49",
    "L2": "CON_U2:50",
    "H5": "CON_U2:51",
    "H4": "CON_U2:52",
    "J3": "CON_U2:53",
    "H3": "CON_U2:54",
    "K3": "CON_U2:55",
    "K2": "CON_U2:56",
    "L4": "CON_U2:57",
    "M4": "CON_U2:58",
    "N3": "CON_U2:59",
    "N2": "CON_U2:60",

    # U4
    "M12": "CON_U4:07",
    "N13": "CON_U4:08",
    "N14": "CON_U4:09",
    "N16": "CON_U4:10",
    "P15": "CON_U4:11",
    "P16": "CON_U4:12",
    "R15": "CON_U4:13",
    "R16": "CON_U4:14",
    "T14": "CON_U4:15",
    "T15": "CON_U4:16",
    "P13": "CON_U4:17",
    "P14": "CON_U4:18",
    "T13": "CON_U4:19",
    "R13": "CON_U4:20",
    "T12": "CON_U4:21",
    "R12": "CON_U4:22",
    "L13": "CON_U4:23",
    "N12": "CON_U4:24",
    "K12": "CON_U4:25",
    "K13": "CON_U4:26",
    "P10": "CON_U4:27",
    "P11": "CON_U4:28",
    "N9": "CON_U4:29",
    "P9": "CON_U4:30",
    "T10": "CON_U4:31",
    "R11": "CON_U4:32",
    "T9": "CON_U4:33",
    "R10": "CON_U4:34",
    "T8": "CON_U4:35",
    "R8": "CON_U4:36",
    "T7": "CON_U4:37",
    "R7": "CON_U4:38",
    "T5": "CON_U4:39",
    "R6": "CON_U4:40",
    "P6": "CON_U4:41",
    "R5": "CON_U4:42",
    "N6": "CON_U4:43",
    "M6": "CON_U4:44",
    "L5": "CON_U4:45",
    "P5": "CON_U4:46",
    "T4": "CON_U4:47",
    "T3": "CON_U4:48",
    "R3": "CON_U4:49",
    "T2": "CON_U4:50",
    "R2": "CON_U4:51",
    "R1": "CON_U4:52",
    "M5": "CON_U4:53",
    "N4": "CON_U4:54",
    "P4": "CON_U4:55",
    "P3": "CON_U4:56",
    "N1": "CON_U4:57",
    "P1": "CON_U4:58",
    "M2": "CON_U4:59",
    "M1": "CON_U4:60",
}

# Only when main -> main
if __name__ == '__main__':
    main()
