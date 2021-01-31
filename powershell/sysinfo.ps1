function getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
    }

write-host(getIP)
$IP = getIP
$Date = Get-Date
$Body = "This machine's IP is $IP. User is $env:username. Hostname is $. PowerShell Version. Todays date is $DATE"

write-host($Body)

#Send-MailMessage -To "jscott017@outlook.com" -From "jsmail027@gmail.com" -Subject "IT3038C Windows Sysinfo" -Body $Body -SmtpServer smtp.google.com -port 587 -UseSSL -Credential (Get-Credential)