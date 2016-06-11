#Third revision for testing with Git - no code changes

import datetime
import requests

r = requests.get('http://realtimerpi.com/college_Women_basketball_rpi_Full.html')
text = r.text

iu = 'Indiana</a>'

offset = text.find(iu)

result_text = text[offset - 52: offset - 49]

if result_text[0] == '>':
	rank = int(result_text[1:3])
else:
	rank = int(result_text)
	
print(rank)
today = datetime.datetime.now()
today = today.strftime('%m / %d / %Y: ')



with open('iuwbb_rpi.txt', 'r') as f:
        line_list = f.readlines()

last_line = line_list[len(line_list) - 1]
last_date = last_line[0:16]
print(rank)

if today != last_date:
    with open('iuwbb_rpi.txt', 'a') as f:
        rank = str(rank)
        line = today + '#IUWBB RPI rank is ' + rank + '\n'
        f.write(line)
