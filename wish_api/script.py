import os
import subprocess

def run_ogrinfo(file_path):
    ogrinfo_command = ['ogrinfo', '-so', file_path, 'gis_osm_places_a_free_1']

    try:
        result = subprocess.run(ogrinfo_command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running ogrinfo: {e.stderr}"

def save_results_to_txt(file_path, results):
    with open(file_path, 'a') as file:
        file.write(results)
        file.write("\n" + "=" * 50 + "\n")

def main():
    directory_path = 'wish/data/portugal-latest-free.shp'
    output_file_path = 'ogrinfo_results.txt'

    shapefiles = [file for file in os.listdir(directory_path) if file.endswith('.shp')]

    for shapefile in shapefiles:
        shapefile_path = os.path.join(directory_path, shapefile)

        results = run_ogrinfo(shapefile_path)

        # Print results to console
        print(f"Results for {shapefile}:")
        print(results)
        print("=" * 50)

        # Save results to text file
        save_results_to_txt(output_file_path, f"Results for {shapefile}:\n")
        save_results_to_txt(output_file_path, results)

if __name__ == "__main__":
    main()
