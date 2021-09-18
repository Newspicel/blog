import os

filespath = []

for filename in os.listdir('pages'):
    filespath += ["pages/" + filename + "/index.md"]

# iterate filespath and create index.md with links to all files
with open("index.md", "w", encoding="utf-8") as index:
    for file in filespath:
        index.write("* [" + file.split("/")[-2] + "](" + file + ")\n")
    index.write("\n")
    print("index.md created")
    index.close()

