@echo off
REM Batch command to easily invoke the pip install/ uninstall function.
REM User can quickly install the required python module by just entering the module name
REM Runs on Windows

cd /
cd Users/%USERNAME%/
pip install selenium
pip install pyautogui

pause
exit
