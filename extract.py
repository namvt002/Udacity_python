"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):

    if neo_csv_path:
        neo_csv_path
    else:
        neo_csv_path = 'data/neos.csv'

    data_neos = []
    with open(neo_csv_path ) as file_csx:
        reader = csv.reader(file_csx)
        next(reader)
        # data corresponding to column of csv 
        # diameter => diameter coloum 15
        # hazardous => pha colum 7
        # designation = pdes colum 3
        # name = name 4
        for colum in reader:
            diameter = float(colum[15]) if colum[15] else float('nan')
            hazardous = False
            if(colum[7] == 'Y'):
                hazardous = True

            data_neos.append(NearEarthObject(colum[3], colum[4], diameter, hazardous))

    return data_neos


def load_approaches(cad_json_path):
    if cad_json_path:
        cad_json_path
    else:
        cad_json_path = 'data/cad.json'

    data_approaches = []
    
    # data corresponding array data to file of json 
    # diameter => dist 4
    # time => cd 3
    # designation = des 0
    # velocity => v_rel 7

    with open(cad_json_path) as file_json:
        data = json.load(file_json)
        for value in data["data"]:
            data_approaches.append(CloseApproach(value[0], value[3], float(value[4]),float(value[7])))

    return data_approaches

