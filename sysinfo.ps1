function getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

$IP = getIP
write-host("This machine's IP is $IP. User is $User. Hostname is $HostN. Powershell Version $Version. Today's Date is $Date, $Month.")

function getUser {
    (Get-LocalUser) | Select-String "Admin*"
    }
$User = getUser

function getHostName {
    (hostname) | Select-String "wilsoncz*"
    }
$HostN = getHostName

function getVersion {
    (Get-Host).Version.Major
    }
$Version = getVersion

function getToday {
    (Get-Date -Format dddd)
    }
$Date = getToday

function getDate {
    (Get-Date -Format MM/dd/yyyy)
    }
$Month = getDate 

Send-MailMessage -To $To -From $From -Cc $Cc -Subject $Subject -Body $BODY -SmtpServer $SMTPServer -port $SMTPPort -UseSSL -Credential (Get-Credential) 

$From = "wilsonchloe64@gmail.com"
$To = "botheaj@ucmail.uc.edu"

$Cc = "wilsoncz@mail.uc.edu"

$Attachment = "C:\temp\Some random file.txt"
$Subject = "IT3038C Windows SysInfo"
$Body = "This machine's IP is $IP. User is $User. Hostname is $HostN. Powershell Version $Version. Today's Date is $Date, $Month."

$SMTPServer = "smtp.gmail.com"
$SMTPPort = "587"
