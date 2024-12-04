#!/bin/bash
chmod +x prepare.sh
#creating dirty data file
python3 generate_dirty_data.py
#Part 2: Clean raw data file
#removing comments
grep -v "#" ./ms_data_dirty.csv > ms_no_comments.csv
#removing empty lines
sed -e '/^$/d' ./ms_no_comments.csv > ms_no_emptylines.csv
#extracting the 5 essential columns
cut -d ',' -f 1,2,4,5,6 ms_no_emptylines.csv > ms_5col.csv
#removing extra commas
sed -e 's/,,/,/g' ./ms_5col.csv > ms_data.csv
#Summary of processed data
row_count=$(wc -l < ms_data.csv)
echo $row_count
head -n 5 "ms_data.csv"

#creating insurance file
file_ins="insurance.lst"
#each label is added to the file on a new line
echo -e "Bronze\nSilver\nGold\nPlatinum" >> "$file_ins"
