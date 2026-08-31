import os

model_path = r'C:\Users\saura\Desktop\Insect\archive.zip\insects.h5'
if os.path.exists(model_path):
    print("File exists")
else:
    print("File does not exist")
