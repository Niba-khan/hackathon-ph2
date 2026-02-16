@echo off
REM Diagnostic script to troubleshoot network issues for npm

echo Running diagnostics for npm network issues...
echo.

echo 1. Checking Node.js and npm versions:
node --version
npm --version
echo.

echo 2. Checking npm configuration:
npm config list
echo.

echo 3. Testing connectivity to npm registry:
ping -n 3 registry.npmjs.org
echo.

echo 4. Checking if node_modules exists:
if exist "..\apps\frontend\node_modules" (
    echo node_modules directory exists
) else (
    echo node_modules directory does not exist
)
echo.

echo 5. Checking package.json existence:
if exist "..\apps\frontend\package.json" (
    echo package.json exists
) else (
    echo ERROR: package.json does not exist
)
echo.

echo 6. Testing basic npm functionality:
npm ping
echo.

echo Diagnostics complete. Check the output above for potential issues.
pause