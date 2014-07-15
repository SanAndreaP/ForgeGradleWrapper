@echo off
del ForgeGradleWrapper.exe
set /p pypath=Geben Sie den Ordner des Python Paths an:
call 7z.exe a ForgeGradleWrapper.exe -mmt -mx5 -sfx fGradleH.py
call 7z.exe a ForgeGradleWrapper.exe -mmt -mx5 -sfx run.bat
call 7z.exe a ForgeGradleWrapper.exe -mmt -mx5 -sfx colorama
call 7z.exe a ForgeGradleWrapper.exe -mmt -mx5 -sfx fgw_src
call 7z.exe a ForgeGradleWrapper.exe -mmt -mx5 -sfx %pypath%