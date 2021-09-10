function getIP {
    (Get-NetIPAddress).IPv4Address | Select-String "192*"
}

$IP = getIP
write-host("This machine's IP is $IP")
