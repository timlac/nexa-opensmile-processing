import os.path
import opensmile
import warnings
import glob
from pathlib import Path
from config import ROOT_DIR


def get_filename(filepath):
    """
    :param filepath: some file path
    :return: filename without path or extension
    """
    return Path(filepath).stem


smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)

# all .wav files in this dir will be processed
input_dir = os.path.join(ROOT_DIR, '/home/tim/Downloads/klippta_ljudfiler/**/*.wav')

# all the output .csv files will be put in this directory, under the same name
output_dir = os.path.join(ROOT_DIR, 'files/out/')

file_paths = glob.glob(input_dir, recursive=True)

for idx, file_path in enumerate(file_paths):
    print("processing file {}, number {} out of {}".format(file_path, idx, len(file_paths)))

    filename = get_filename(file_path)
    df = smile.process_file(file_path)

    output_path = os.path.join(output_dir, filename + ".csv")
    # save csv
    df.to_csv(output_path, index=False)
