#validating indian mobile number
import re
data=['hello','+11-2998734570','+91-6734610984','+91-5987347021','6987230159']
mp='[+]91-[6-9]\d{9}'
for i in data:
    if re.match(mp,i):
        print(i)


#validating email id
import re
data=['kanha@gmail.com','56kanha@gmail.com','sahoo.kanha@gmail.com']
mp='[a-zA-Z0-9]\w*[.]?\w+@gmail[.]com'
for i in data:
    if re.match(mp,i):
        print(i)