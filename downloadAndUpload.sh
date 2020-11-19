# AWS requires a signature that is less than 5 minutes old so we must cURL the page to find the new DL URL
# Get the URL for the list of members
curl https://member.usafencing.org/search/members --output members.txt
# Find the DL URL in the html output
python scrapeCSVURL.py
# cURL the URL we found
xargs < urls.txt curl --output members.csv
# Clean up
rm members.txt
rm urls.txt
sleep .1m
# Download referee stuff
curl 'https://member.usafencing.org/referees/search?name_member_id_search=1000&division_search=&rating_type=highestUsaEarnedRating&rating_is=%3D&rating_val=any&show%5B%5D=usa&sort=name&format=csv' --output referee1.csv
# Websites don't like if you do things too often so wait for 2 minutes between each cURL
sleep .1m
curl 'https://member.usafencing.org/referees/search?name_member_id_search=1001&division_search=&rating_type=highestUsaEarnedRating&rating_is=%3D&rating_val=any&show%5B%5D=usa&sort=name&format=csv' --output referee2.csv
sleep .1m
curl 'https://member.usafencing.org/referees/search?name_member_id_search=1002&division_search=&rating_type=highestUsaEarnedRating&rating_is=%3D&rating_val=any&show%5B%5D=usa&sort=name&format=csv' --output referee3.csv
python csvtojson.py
# node `pwd`
# Uncomment these lines to delete all csv and or json files if you want
# mkdir old
# Clean out old folder
rm old/*
# Move all csv files to old folder
mv m*csv old
mv newr*csv old
# Delete all csv and json that remain
rm *csv
# rm m*json
# rm n*json

# We sleep for one minute between each cURL so we don't annoy the website
