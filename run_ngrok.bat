@echo off
echo Configuring and starting ngrok...

REM Configure authtoken
.\ngrok.exe config add-authtoken 2u0WCZXgkZPbwou3gNvJ4shD6xA_2zSB7QnZ5tMjbxeSqwbm6

REM Start ngrok in a persistent window
start cmd /k ".\ngrok.exe http 8000"

echo.
echo Ngrok started! Copy the HTTPS URL from the new window
echo Use that URL + /webhook/ in your Twilio console
echo.
echo Press any key to continue...
timeout /t 5
type ngrok.log | findstr "url=https://"
pause > nul