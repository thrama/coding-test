# Script: PortScanner.ps1
# Author: Lorenzo Lombardi
# Date: 01/16/2023
#
# Description: This script scans a range of ports on the same remote server.

$startPort = 1
$endPort = 100
$hostName = "localhost"

Write-Host "Testing the range port [$startPort-$endPort] on the host [$hostName]..."

# Loop through the range of ports
for ($i = $startPort; $i -le $endPort; $i++) {
    # Test connection to the current port
    $connection = New-Object System.Net.Sockets.TcpClient
    try {
        $connection.Connect($hostName, $i)
        Write-Host "Port $i is open"
    } catch {
        Write-Host "Port $i is closed"
    } finally {
        $connection.Close()
    }
}
