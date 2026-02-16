@echo off
REM Batch script to start the frontend application

REM Navigate to the frontend directory
cd /d "%~dp0apps\frontend"

REM Install dependencies (retry on failure)
echo Installing dependencies...
npm install --legacy-peer-deps
if %errorlevel% neq 0 (
    echo First install attempt failed, trying with cache clean...
    npm cache clean --force
    npm install --legacy-peer-deps
)

REM Check if installation was successful
if %errorlevel% equ 0 (
    echo Dependencies installed successfully!
    
    REM Run the development server
    echo Starting the development server...
    npm run dev
) else (
    echo Failed to install dependencies. Please check your network connection.
    pause
    exit /b 1
)