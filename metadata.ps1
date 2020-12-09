# Python Executable Definition
$Python = "python.exe"


# Python Scrip that I wish to execute
#Write your path down where the py file is in
$Script = "C:\Users\user32\Desktop\piac\pyExif.py"

#Write down the path where your file images is
$files = Get-ChildItem C:\Users\user32\Desktop\images\*.jpg
$jpegList = $files | Select-Object FullName | Format-Table -HideTableHeaders

$jpegList | & $Python $Script
