import os
import glob

def run(command):
	print(command)
	os.system(command)


notebook_files = [filename for filename in glob.iglob('./lab*/*.ipynb', recursive=True)]

notebook_files.sort(key=lambda x: os.path.basename(os.path.dirname(x)))

pdf_command = "jupyter nbconvert {} --to pdf"
html_command = "jupyter nbconvert {} --to html --template full"

for f in notebook_files:
    print(os.getcwd())
    folder = os.path.dirname(f)
    print(folder)
    os.chdir(folder)
    file_name = os.path.basename(f)
    run(pdf_command.format(file_name))
    run(html_command.format(file_name))
    print("file_name:", file_name)
    os.rename(os.path.splitext(file_name)[0] + ".html","index.html")
    os.chdir("..")
    print(os.getcwd())

