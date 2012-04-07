from string import *

def generate(page_list):
    rec_output = ""
    for record in page_list:
        backlink = record[0]
        ancortext = record[1]
        rec_output += backlink+" "+ancortext+"\n"
    content = "we would like to remove links to our website in your website in following pages:\n" \
            + rec_output
    print content

fp = open('list.csv')

first_line = fp.readline()
first_record = split(first_line, ';')
prev_ip = first_record[3]

page_list = list()

page_list.append(first_record)

lines = fp.readlines()

for line in lines:
    record = split(line, ';')
    ip = record[3]
    if(ip == prev_ip):
        page_list.append(record)
    else:
        generate(page_list)
        prev_ip = ip
        page_list = []
        page_list.append(record)

fp.close()


