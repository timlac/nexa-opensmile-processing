import opensmile
import os
import pandas as pd

from config import ROOT_DIR

# set opensmile parameters
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)

input_path = os.path.join(ROOT_DIR, 'files/example_audio/file_example_WAV_1MG.wav')
output_path = os.path.join(ROOT_DIR, 'files/out/file_example_WAV_1MG.csv')

# process sound file
df = smile.process_file(input_path)

# save csv
df.to_csv(output_path, index=False)

