#Reformats the gbk files produced by pharokka (https://doi.org/10.1093/bioinformatics/btac776)
#and adds artemis colour codes (0-18)
#Please refer to artermis manual chapter 6 for exact colour codes
#Reformatted gbk files are suitable for parsing into EasyFig (http://mjsull.github.io/Easyfig/) for visualisation

#version 0.0.2
#==============================================================
import argparse 

#==============================================================
def write_colour(func):
    wf.write(f'                     /colour="{func}"\n{i}')
def write_normal():
    wf.write(f"{i}")
def parse_colours(file):
    colours = {}
    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                key, value = line.split('=')
                colours[key] = int(value)
    return colours
#==============================================================

parser = argparse.ArgumentParser(description="Reformat GBK files produced by Pharokka and add Artemis color codes for EasyFig Plotting.")
parser.add_argument("-fi", metavar="/PATH/TO/GBK", type=str, help="Pharokka Output Genebank (GBK) file.")
parser.add_argument("-c", metavar="/PATH/TO/COLOURS", type=str, help="Colour configuration file.")
args = parser.parse_args()
if args.fi:
    inputfile = args.fi
    if not inputfile.endswith(".gbk"):
        parser.error("Please provide a GeneBank (GBK) file.")
else:
    parser.error("Please provide the --fi argument with the input GBK file.")
    
if args.c:
    colours_file = args.c
    colours = parse_colours(colours_file)
else:
    parser.error("Please provide the --c argument with the colour configuration file.")




basename = inputfile.split(".gbk")[0]
outputfile = f"{basename}.formatted.gbk"

#Default colour codes
#func_DNA = 5
#func_hypo = 0
#func_head = 2
#func_connect = 10
#func_tail = 7
#func_trans = 3
#func_lysis = 11
#func_moron = 6
#func_other = 14
#func_int = 8
#print(colours)

with open(inputfile, 'r') as f, open(outputfile, "w") as wf:
    info = f.readlines()
    for i in info:
        if "/function" in i:
            function = i.split("=")[1].strip()
            if function.split('"')[1] in colours:
                function = function.split('"')[1]
                write_colour(colours[function])
            else:
                #print(f"Unknown function: {function}")
                write_normal()
                #print(" ")
        else:
            write_normal()
    