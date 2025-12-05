# Enable error handling
$ErrorActionPreference = "Stop"

# Relaunch as admin if not elevated
if (-not ([Security.Principal.WindowsPrincipal] `
    [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(`
    [Security.Principal.WindowsBuiltInRole] "Administrator"))
{
    Start-Process powershell "-File `"$PSCommandPath`"" -Verb RunAs
    exit
}

$ccPython = "C:\Program Files\CloudCompare\plugins\Python\python.exe"

Write-Host "Installing cloud_compare_python_plugin..." -ForegroundColor Cyan

try {
	& $ccPython -m pip install $PSScriptRoot/. --break-system-packages
}
catch {
    Write-Host "ERROR OCCURRED:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Press Enter to close..."
    Read-Host
    exit 1
}

Write-Host "Installation complete."
Write-Host ""
Write-Host "Press Enter to close..." -ForegroundColor Cyan
Read-Host