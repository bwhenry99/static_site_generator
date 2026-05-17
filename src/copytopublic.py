import os
import shutil

def copy_files_to_dir(source, target):
    absSource = os.path.abspath(source)
    if not os.path.exists(absSource):
        ValueError("Source directory does not exist")

    absTarget = os.path.abspath(target)

    if os.path.exists(absTarget):
        shutil.rmtree(absTarget)
    os.mkdir(absTarget)

    for item in os.listdir(source):
        filepath  = os.path.join(absSource, item)
        if os.path.isfile(filepath):
            shutil.copy(filepath, absTarget)
        else:
            os.mkdir(os.path.join(absTarget, item))
            copy_files_to_dir(filepath, os.path.join(absTarget, item))