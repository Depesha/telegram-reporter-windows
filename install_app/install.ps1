Set-ExecutionPolicy Bypass -Scope Process -Force;
Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'));

Invoke-WebRequest -Uri 'https://bootstrap.pypa.io/get-pip.py' -OutFile get_pip.py
choco feature enable -n=allowGlobalConfirmation
choco upgrade python

$env:Path += ';C:\Python310'

python .\get_pip.py

$env:Path += ';C:\Python310\Scripts'

Set-Location -Path ..\

pip install -r .\py_app\requirements.txt
python .\py_app\telegram_reporter.py