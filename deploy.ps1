$env:PATH = "C:\Users\Administrator\AppData\Local\Programs\Nodejs\node-v20.18.0-win-x64;" + $env:PATH
$env:SURGE_LOGIN = "phuquocbds4878@fldubai.com"
$env:SURGE_TOKEN = "2ba1fad35a72227eb6fe2dae2afdac00"
& "C:\Users\Administrator\AppData\Local\Programs\Nodejs\node-v20.18.0-win-x64\npx.cmd" surge "$PSScriptRoot" phuquocbds.surge.sh
