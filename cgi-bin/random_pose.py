#!/usr/bin/env python

import random

index_file_path = "index.txt"


if __name__ == "__main__":
    filenames = [line.rstrip('\n') for line in open(index_file_path)]

    ## DEBUG
    #print "Content-type: text/plain\n"
    #for f in filenames:
    #    print f
    
    filename = "/" + random.choice(filenames)

    print "Content-type: text/html\n"
    print '<html>'
    print '<head>'
    print '<title>Random pose generator</title>'
    print '<link rel="stylesheet" type="text/css" href="/mystyle.css">'
    print '<script src="/js/myscript.js" type="text/javascript"></script>'
    print '</head>'

    print '<body>'
    print '<img src="%s">' % filename

    print '<div id="timerLinks">'
    print '<a href="?time=30" class="timer-link">30 sec pose</a>'
    print '<a href="?time=120" class="timer-link">2min pose</a>'
    print '</div>'

    print '<div id="timeText" />'
    print '<script>startCountdown()</script>'

    print '</body>'
    print '</html>'

