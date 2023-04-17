@echo off

rem Check if the command line argument exists
if "%1" == "" (
  echo Usage: %0 [-c|-d <file>]
  exit /b 1
)

rem Check if the argument is '-c' or '-d'
if "%1" == "-c" (
  rem Check if the next argument exists
  if "%2" == "" (
    echo Error: Missing file name after -c option.
    exit /b 1
  ) else (
    rem Call the comp.py Python script with the file name as an argument
    python comp.py "%2"
    exit /b 0
  )
) else if "%1" == "-d" (
  rem Check if the next argument exists
  if "%2" == "" (
    echo Error: Missing file name after -d option.
    exit /b 1
  ) else (
    rem Call the decomp.py Python script with the file name as an argument
    python decomp.py "%2"
    exit /b 0
  )
)

rem If no valid options are provided, display an error message
echo Error: Invalid option. Use -c or -d to specify an operation.
exit /b 1
