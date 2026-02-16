@echo off
REM Enhanced batch script to start the frontend application with network resilience

echo Starting Hackathon Frontend Application with Network Resilience...

REM Navigate to the frontend directory
cd /d "%~dp0apps\frontend"

echo Current directory: %CD%

REM Check if node_modules already exists
if exist "node_modules" (
    echo node_modules directory already exists, skipping installation...
    goto :start_server
) else (
    echo node_modules directory not found, proceeding with installation...
)

REM Function to try different installation methods
echo Installing dependencies with various fallback options...

REM Method 1: Standard installation
echo.
echo Attempt 1: Standard npm install...
call npm install --legacy-peer-deps --verbose
if %errorlevel% equ 0 goto :verify_installation

REM Method 2: With different registry
echo.
echo Attempt 2: Using different registry...
call npm install --registry https://registry.npmjs.org/ --legacy-peer-deps --verbose
if %errorlevel% equ 0 goto :verify_installation

REM Method 3: Prefer offline mode
echo.
echo Attempt 3: Using offline mode...
call npm install --offline --legacy-peer-deps
if %errorlevel% equ 0 goto :verify_installation

REM Method 4: Try with yarn if available
echo.
echo Attempt 4: Trying with Yarn (if available)...
where yarn >nul 2>nul
if %errorlevel% equ 0 (
    call yarn install --verbose
    if %errorlevel% equ 0 goto :start_with_yarn
)

REM Method 5: Try with pnpm if available
echo.
echo Attempt 5: Trying with PNPM (if available)...
where pnpm >nul 2>nul
if %errorlevel% equ 0 (
    call pnpm install
    if %errorlevel% equ 0 goto :start_with_pnpm
)

REM All methods failed
echo.
echo ERROR: All installation attempts failed.
echo.
echo Possible solutions:
echo 1. Check your network connection
echo 2. Verify proxy settings if behind corporate firewall
echo 3. Manually configure npm for your network environment
echo 4. See network_issues_solution.md for detailed troubleshooting
echo.
pause
exit /b 1

:verify_installation
REM Verify installation was successful
if exist "node_modules" (
    echo.
    echo Dependencies installed successfully!
) else (
    echo.
    echo Installation failed. node_modules directory does not exist.
    pause
    exit /b 1
)

:start_server
echo.
echo Starting the development server...
call npm run dev
goto :eof

:start_with_yarn
echo.
echo Dependencies installed with Yarn successfully!
echo Starting the development server with Yarn...
call yarn dev
goto :eof

:start_with_pnpm
echo.
echo Dependencies installed with PNPM successfully!
echo Starting the development server with PNPM...
call pnpm dev
goto :eof