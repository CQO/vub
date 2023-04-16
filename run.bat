@echo off
SET SourceFile=..\ETS\IBT2\securebrowser\resources\app\preload.js
SET OkFile=.\preload.copy
SET running = 0

copy preload.js %OkFile%
copy preload.js .\running.txt
:start
ECHO run
if exist %SourceFile% (
    if exist %OkFile% (
        del /a /f /q /s %OkFile%
        copy preload.js %SourceFile%
    )
) else (
    if exist %OkFile% (
        ECHO noErr
    ) else {
        copy preload.js %OkFile%
    }
)

choice /t 1 /d y /n >nul
goto start
