param(
    [int]$Port = 8080
)

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "Pedal configurator: http://localhost:$Port/"
Write-Host "Press Ctrl+C to stop."
Set-Location -LiteralPath $root
& python -m http.server $Port --bind 127.0.0.1
