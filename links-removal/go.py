import os

links_to_be_removed = "";

for root, dirs, files in os.walk("./files/"):
    for filename in files:
        path = "./files/"+filename
        fp = open(path, 'w')
        raw_content = fp.read()
        new_content = replace(raw_content, link_to_be_removed, '')
        fp.flush()
        fp.write(new_content)
        fp.close()

    # for test only, should be disabled
    # TEST CODE BEGIN
    for filename in files:
        path = "./files/"+filename
        fp = open(path)
        print fp.readline()
        fp.close()
    #TEST CODE END
