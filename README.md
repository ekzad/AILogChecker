## Simple AI Cybersecurity app (in Django) ##
``ATTENTION!!!!!`` **The HTML file is completely vibe coded (i did some coding, but i ran it through AI to make sure it's at least readable)**

## So:
This is an app that you can take inspiration from for building an actual AI app for website security.
It gets a logs.txt, BTW IF YOU DONT HAVE LOGS, YOU CAN GENERATE IT WITH > Log_Generator.py <. It generates fake log info in the right format; the format that the program can read.

Anyway: So, it gets a logs.txt, runs it through an AI model through an API call with the prompt written in the code, then takes the answer and feeds it to our views.py, (after parsing it into actual results), then it is fed to our website front end, and that's when the HTML logic comes in.

Simple but it works, and you can take some inspiration. I know, it's not some huge project, but im just having fun man.

I got a couple stuff coming up, im gonna put up some goodies here on github!!!

## FYI: ``Just to be sure, i did wipe out the django secret, you can get one with the following code:``

*
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
*
thank u !!!
