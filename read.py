from chat_downloader import ChatDownloader
import csv
import sys
import os

with open('ytcomments.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Do not do anything')
            line_count += 1
        else:
            print(f'Starting... {row[0]}-{row[1]}-{row[2]}.')
            sessionfilename=row[0]+row[2]
            # cmd="chat_downloader "+row[1]+" --output "+sessionfilename+".json"
            # os.system(cmd)
            chat = ChatDownloader().get_chat(row[1], output='comments/'+sessionfilename+'.json')      # create a generator
            for message in chat:                        # iterate over messages
                chat.print_formatted(message)           # print the formatted message

            print(f'Completed... {row[0]}-{row[1]}-{row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')