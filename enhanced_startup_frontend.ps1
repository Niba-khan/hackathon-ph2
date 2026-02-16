# PowerShell script to start the frontend application with network resilience

Write-Host "Starting Hackathon Frontend Application with Network Resilience..." -ForegroundColor Green

# Navigate to the frontend directory
Set-Location -Path "$PSScriptRoot\apps\frontend"
Write-Host "Current directory: $(Get-Location)" -ForegroundColor Cyan

# Check if node_modules already exists
if (Test-Path "node_modules") {
    Write-Host "node_modules directory already exists, skipping installation..." -ForegroundColor Yellow
    Start-Server
} else {
    Write-Host "node_modules directory not found, proceeding with installation..." -ForegroundColor Yellow
}

# Function to try different installation methods
function Install-Deps {
    Write-Host "`nInstalling dependencies with various fallback options..." -ForegroundColor Cyan

    # Method 1: Standard installation
    Write-Host "`nAttempt 1: Standard npm install..." -ForegroundColor White
    $result = npm install --legacy-peer-deps --verbose
    if ($LASTEXITCODE -eq 0) { 
        Verify-Installation
        return
    }

    # Method 2: With different registry
    Write-Host "`nAttempt 2: Using different registry..." -ForegroundColor White
    $result = npm install --registry https://registry.npmjs.org/ --legacy-peer-deps --verbose
    if ($LASTEXITCODE -eq 0) { 
        Verify-Installation
        return
    }

    # Method 3: Prefer offline mode
    Write-Host "`nAttempt 3: Using offline mode..." -ForegroundColor White
    $result = npm install --offline --legacy-peer-deps
    if ($LASTEXITCODE -eq 0) { 
        Verify-Installation
        return
    }

    # Method 4: Try with yarn if available
    Write-Host "`nAttempt 4: Trying with Yarn (if available)..." -ForegroundColor White
    if (Get-Command yarn -ErrorAction SilentlyContinue) {
        $result = yarn install --verbose
        if ($LASTEXITCODE -eq 0) { 
            Start-WithYarn
            return
        }
    }

    # Method 5: Try with pnpm if available
    Write-Host "`nAttempt 5: Trying with PNPM (if available)..." -ForegroundColor White
    if (Get-Command pnpm -ErrorAction SilentlyContinue) {
        $result = pnpm install
        if ($LASTEXITCODE -eq 0) { 
            Start-WithPnpm
            return
        }
    }

    # All methods failed
    Write-Host "`nERROR: All installation attempts failed." -ForegroundColor Red
    Write-Host ""
    Write-Host "Possible solutions:" -ForegroundColor Yellow
    Write-Host "1. Check your network connection"
    Write-Host "2. Verify proxy settings if behind corporate firewall"
    Write-Host "3. Manually configure npm for your network environment"
    Write-Host "4. See network_issues_solution.md for detailed troubleshooting"
    Read-Host "Press Enter to exit"
    exit 1
}

function Verify-Installation {
    if (Test-Path "node_modules") {
        Write-Host "`nDependencies installed successfully!" -ForegroundColor Green
    } else {
        Write-Host "`nInstallation failed. node_modules directory does not exist." -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

function Start-Server {
    Write-Host "`nStarting the development server..." -ForegroundColor Cyan
    npm run dev
}

function Start-WithYarn {
    Write-Host "`nDependencies installed with Yarn successfully!" -ForegroundColor Green
    Write-Host "Starting the development server with Yarn..." -ForegroundColor Cyan
    yarn dev
}

function Start-WithPnpm {
    Write-Host "`nDependencies installed with PNPM successfully!" -ForegroundColor Green
    Write-Host "Starting the development server with PNPM..." -ForegroundColor Cyan
    pnpm dev
}

# Start the installation process
Install-Deps