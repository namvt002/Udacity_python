
import csv
import json

def write_to_csv(results, filename):

    title = [
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous']

    with open(filename, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(title)

        for close_approach in results:
            neo = close_approach.neo
            row = [ close_approach.time_str,
                    close_approach.distance,
                    close_approach.velocity,
                    close_approach.neo.designation,
                    close_approach.neo.name or '',
                    close_approach.neo.diameter or '',
                    str(neo.hazardous) ]
            writer.writerow(row)



def write_to_json(results, filename):

    rows = []

    for close_approach in results:
        neo = close_approach.neo
        row = {
            'datetime_utc': close_approach.time_str,
            'distance_au': close_approach.distance,
            'velocity_km_s': close_approach.velocity,
            'neo': {
                'designation': neo.designation,
                'name': neo.name or '',
                'diameter_km': neo.diameter or float('nan'),
                'potentially_hazardous': neo.hazardous
            }
        }
        rows.append(row)

    with open(filename, 'w') as outfile:
        json.dump(rows, outfile, indent=2)
