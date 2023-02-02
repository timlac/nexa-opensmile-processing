import os.path
import opensmile
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
    feature_set=opensmile.FeatureSet.ComParE_2016,
    feature_level=opensmile.FeatureLevel.LowLevelDescriptors_Deltas,
)

# all .wav files in this dir will be processed
input_dir = os.path.join(ROOT_DIR, 'files/example_audio/**/*.wav')

# all the output .csv files will be put in this directory, under the same name
output_dir = os.path.join(ROOT_DIR, 'files/out/')

for file in glob.glob(input_dir, recursive=True):
    filename = get_filename(file)

    # process sound file
    df = smile.process_file(file)

    output_path = os.path.join(output_dir, filename + ".csv")
    # save csv
    df.to_csv(output_path, index=False)
