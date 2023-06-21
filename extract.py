"""Extract data on near-Earth objects."""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file."""
    if neo_csv_path:
        neo_csv_path
    else:
        neo_csv_path = 'data/neos.csv'

    data_neos = []
    with open(neo_csv_path) as file_csx:
        reader = csv.reader(file_csx)
        next(reader)
        for colum in reader:
            diameter = float(colum[15]) if colum[15] else float('nan')
            hazardous = False
            if (colum[7] == 'Y'):
                hazardous = True

            data_neos.append(NearEarthObject(
                colum[3], colum[4], diameter, hazardous
                ))

    return data_neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file."""
    if cad_json_path:
        cad_json_path
    else:
        cad_json_path = 'data/cad.json'

    data_approaches = []

    with open(cad_json_path) as file_json:
        data = json.load(file_json)
        for value in data["data"]:
            data_approaches.append(
                CloseApproach(value[0],
                              value[3],
                              float(value[4]),
                              float(value[7])))

    return data_approaches
