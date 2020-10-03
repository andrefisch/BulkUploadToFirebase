import csv 
import json 
import os

def convert_csv_to_json(csvFilePath, memberString):
    temp = csvFilePath.split('.')
    jsonFilePath = temp[0] + ".json"
    # create a dictionary 
    data = {} 
    # Open a csv reader called DictReader 
    with open(csvFilePath, encoding='utf-8') as csvf: 
        rowNum = 0
        csvReader = csv.DictReader(csvf) 
        # Convert each row into a dictionary 
        # and add it to data 
        for rows in csvReader: 
            # Assuming a column named 'memberString' to 
            # be the primary key 
            key = rows[memberString]
            data[key] = rows

    # Open a json writer, and use the json.dumps() 
    # function to dump data 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonf.write(json.dumps(data, indent=4)) 

def murder_end_comma(csvFilePath):
    fin = open(csvFilePath, "rt")
    #output file to write the result to
    fout = open('new' + csvFilePath, "wt")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        temp = line
        fout.write(temp[:-2] + temp[-1:])
    #close input and output files
    fin.close()
    fout.close()

# This will work for the members
print('Now converting members.csv')
# convert_csv_to_json('members.csv', 'Member #')
# This will work for the referees
# Get all files starting with the word 'referee' in this directory
files = [x for x in os.listdir() if x.startswith("referee")]
for eachfile in files:
    print("Now converting", eachfile)
    murder_end_comma(eachfile)
files = [x for x in os.listdir() if x.startswith("newreferee")]
for eachfile in files:
    print("Now converting", eachfile)
    convert_csv_to_json(eachfile, 'Member Number')

# download link for members
memberDL = 'https://usfaexports.s3.amazonaws.com/TodaysMemberList-2020-10-02.csv?response-content-disposition=attachment%3B%20filename%3Dmembers.csv&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAI4AKSIFI2VZZ4GVQ%2F20201002%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201002T152441Z&X-Amz-SignedHeaders=host&X-Amz-Expires=600&X-Amz-Signature=9df6ea58f485f6335b13887348db337e2f27f017c1de369a7e809e5a624f6f45'

referee1DL = 'https://member.usafencing.org/referees/search?name_member_id_search=1000&division_search=&rating_type=highestUsaEarnedRating&rating_is=%3D&rating_val=any&show%5B%5D=usa&sort=name&format=csv'

referee2DL = 'https://member.usafencing.org/referees/search?name_member_id_search=1001&division_search=&rating_type=highestUsaEarnedRating&rating_is=%3D&rating_val=any&show%5B%5D=usa&sort=name&format=csv'

referee3DL = 'https://member.usafencing.org/referees/search?name_member_id_search=1002&division_search=&rating_type=highestUsaEarnedRating&rating_is=%3D&rating_val=any&show%5B%5D=usa&sort=name&format=csv'
