#!/usr/bin/python

import os
import sys
import uuid

f1 = open('/tmp/rewrite.log', 'w', 0)


def rewrite_url(line):
    # line:  http://192.168.1.13/biedronka_logo.jpg 192.168.1.100/192.168.1.100 - GET myip=- myport=3128
    urls = line.split(' ')
    old_url = urls[0]
    new_url = '\n'

    if old_url.endswith('jpg') or old_url.endswith('.jpeg'):
        filename = str(uuid.uuid4()) + ".jpg"

        wget_cmd = "/usr/bin/wget -q -O /var/www/html/img/" + filename + " " + old_url
        log(wget_cmd)
        os.system(wget_cmd)

        mogrify_cmd = "/usr/bin/mogrify -flip /var/www/html/img/" + filename
        log(mogrify_cmd)
        os.system(mogrify_cmd)

        new_url = "http://127.0.0.1/img/" + filename + new_url
        log('line: ' + line + ' | new_url: ' + new_url)

    return new_url


def log(msg):
    f1.write(msg + '\n')


def inf_loop():
    while True:
        line = sys.stdin.readline().strip()
        new_url = rewrite_url(line)
        sys.stdout.write(new_url)
        sys.stdout.flush()


try:
    log('--- start infinitive loop ---')
    inf_loop()
finally:
    log('--- End of the log --- ')
    f1.close()
