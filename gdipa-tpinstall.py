import os
import shutil

# ask for input
ipa = input('What is the path of your Geometry Dash IPA: ')
tp = input('What is the path of your Texture Pack: ')
os.rename(ipa, 'gd.zip')
shutil.unpack_archive('gd.zip', 'temp')
# check if files exist and replace them
folder_1 = 'temp\Payload\GeometryJump.app'
files_in_folder_1 = os.listdir(folder_1)
for file in files_in_folder_1:
    file_path_1 = os.path.join(folder_1, file)
    file_path_2 = os.path.join(tp, file)
    if os.path.exists(file_path_2):
        shutil.copy(file_path_2, folder_1)

# create the zip file and add the files to it
shutil.make_archive('gdtp', 'zip', 'temp')
os.rename('gdtp.zip', 'gd.ipa')
shutil.rmtree('temp')
os.remove('gd.zip')
print("IPA saved as gd.ipa, click any key to exit")
input()


