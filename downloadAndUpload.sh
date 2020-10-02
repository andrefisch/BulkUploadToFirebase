curl 'https://member.usafencing.org/referees/search?name_member_id_search=1000&division_search=&rating_type=highestUsaEarnedRating&rating_is=%3D&rating_val=any&show%5B%5D=usa&sort=name&format=csv' --output referee1.csv
# Websites don't like if you do things too often so wait for 2 minutes between each curl
sleep 2m
curl 'https://member.usafencing.org/referees/search?name_member_id_search=1001&division_search=&rating_type=highestUsaEarnedRating&rating_is=%3D&rating_val=any&show%5B%5D=usa&sort=name&format=csv' --output referee2.csv
sleep 2m
curl 'https://member.usafencing.org/referees/search?name_member_id_search=1002&division_search=&rating_type=highestUsaEarnedRating&rating_is=%3D&rating_val=any&show%5B%5D=usa&sort=name&format=csv' --output referee3.csv
python csvtojson.py
node `pwd`
# Uncomment these lines to delete all csv and or json files if you want
# rm *csv
# rm *json
