Goal is to bypass login with SQLi

1. Try some common passwords
2. Try SQL commands in input
3. Internal server error => Potential vulnerabilities 

Possible SQL syntax

SELECT user FROM users where username='' and password=''

SELECT user FROM users where username='admin'--' and password='' ❌
SELECT user FROM users where username='administrator'--' and password='' ❌

### Code automation
FoxyProxy extension in browser
Analyse using burpsuite
CSRF token https://youtu.be/fMPvCyD2v4w?t=1588
Write code to get csrf token first