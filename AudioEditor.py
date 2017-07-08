import os


def normalize(folder_path):
    # redirect to the folder that contains all of the wav files
    os.chdir(folder_path)

    for file in os.listdir(folder_path):
        # iterate over all of the wav files in the folder
        if ".wav" not in file:
            continue

        # use ffmpeg-normalize to normalize the audio sample
        os.system(
            "ffmpeg-normalize -v -f --level=-1.0 -m " + file)


normalize('/Users/robingranberry/Documents/CaSTSelectedWords')