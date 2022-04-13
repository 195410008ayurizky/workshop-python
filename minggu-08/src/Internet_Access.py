from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
     for line in response:
         line = line.decode()             # Convert bytes to a str
         if line.startswith('datetime'):
             print(line.rstrip())         # Remove trailing newline
#output
datetime: 2022-04-12T11:46:35.689215+00:00

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
 """To: jcaesar@example.org
 From: soothsayer@example.org

 Beware the Ides of March.
 """)
server.quit()