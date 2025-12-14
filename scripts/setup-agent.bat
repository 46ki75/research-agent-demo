@echo off
REM Navigate to the agent directory
cd /d "%~dp0\..\apps\agent" || exit /b 1

REM Install dependencies using uv
uv sync 