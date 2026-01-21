# 🔧 Git Installation & GitHub Push Guide
**Wine Cultivar Prediction System**  
**Student:** Toluwani Onipede (22CG031936)

---

## ⚠️ ISSUE DETECTED: Git Not Installed

Git is not currently installed on your system. You need to install Git before pushing to GitHub.

---

## 📥 STEP 1: INSTALL GIT FOR WINDOWS

### Option A: Download Git for Windows (Recommended)

1. **Download Git:**
   - Go to: https://git-scm.com/download/win
   - Click "Click here to download" (64-bit version)
   - File: `Git-2.43.0-64-bit.exe` (or latest version)

2. **Install Git:**
   - Run the downloaded installer
   - **IMPORTANT SETTINGS:**
     - ✅ Use default installation directory: `C:\Program Files\Git`
     - ✅ Select: "Git from the command line and also from 3rd-party software"
     - ✅ Select: "Use bundled OpenSSH"
     - ✅ Select: "Use the OpenSSL library"
     - ✅ Select: "Checkout Windows-style, commit Unix-style line endings"
     - ✅ Select: "Use MinTTY (the default terminal of MSYS2)"
     - ✅ Select: "Default (fast-forward or merge)"
     - ✅ Select: "Git Credential Manager"
     - ✅ Enable file system caching
   - Click "Install"
   - Click "Finish"

3. **Verify Installation:**
   - **CLOSE and REOPEN PowerShell** (important!)
   - Run: `git --version`
   - Expected output: `git version 2.43.0.windows.1` (or similar)

**Installation Time:** 5-10 minutes

---

### Option B: Install via Winget (Faster)

If you have Windows Package Manager:

```powershell
winget install --id Git.Git -e --source winget
```

Then **restart PowerShell**.

---

## 🔐 STEP 2: CONFIGURE GIT (FIRST TIME ONLY)

After installing Git, configure your identity:

```powershell
git config --global user.name "Toluwani Onipede"
git config --global user.email "your-email@example.com"
```

**Replace** `your-email@example.com` with the email you used for GitHub.

Verify configuration:
```powershell
git config --global --list
```

---

## 📤 STEP 3: PUSH PROJECT TO GITHUB

### 3.1 Navigate to Project Directory

```powershell
cd c:\Users\DELL\Desktop\Ass
```

### 3.2 Initialize Git Repository

```powershell
git init
```

Expected output: `Initialized empty Git repository in c:/Users/DELL/Desktop/Ass/.git/`

### 3.3 Add Remote Repository

```powershell
git remote add origin https://github.com/Tolz-ctrl/WineCultivar_Project_OnipedeToluwani_22CG031936.git
```

Verify remote:
```powershell
git remote -v
```

Expected output:
```
origin  https://github.com/Tolz-ctrl/WineCultivar_Project_OnipedeToluwani_22CG031936.git (fetch)
origin  https://github.com/Tolz-ctrl/WineCultivar_Project_OnipedeToluwani_22CG031936.git (push)
```

### 3.4 Stage All Files

```powershell
git add .
```

Check what will be committed:
```powershell
git status
```

### 3.5 Commit Files

```powershell
git commit -m "Complete Wine Cultivar Prediction System with deployment files"
```

Expected output: Shows number of files changed and insertions.

### 3.6 Push to GitHub

```powershell
git push -u origin main
```

**If you get an error about 'master' vs 'main':**
```powershell
git branch -M main
git push -u origin main
```

**First time push:** You'll be prompted to authenticate with GitHub:
- Enter your GitHub username
- Enter your GitHub password (or Personal Access Token)

---

## ✅ STEP 4: VERIFY MODEL FILES IN REPOSITORY

**CRITICAL:** Verify that model files are included:

```powershell
git ls-files | findstr "pkl"
```

**Expected output:**
```
model/scaler.pkl
model/wine_cultivar_model.pkl
```

If model files are NOT showing, they might be in .gitignore. Fix:

```powershell
# Force add model files
git add -f model/*.pkl
git commit -m "Add trained model files"
git push origin main
```

---

## 🔍 STEP 5: VERIFY DEPLOYMENT FILES

Verify all deployment files are committed:

```powershell
git ls-files | findstr "Procfile runtime.txt requirements.txt"
```

**Expected output:**
```
Procfile
requirements.txt
runtime.txt
```

---

## 🌐 STEP 6: VERIFY ON GITHUB.COM

1. Go to: https://github.com/Tolz-ctrl/WineCultivar_Project_OnipedeToluwani_22CG031936
2. Verify you see all files:
   - ✅ app.py
   - ✅ Procfile
   - ✅ runtime.txt
   - ✅ requirements.txt
   - ✅ model/ folder with .pkl files
   - ✅ templates/ folder
   - ✅ All documentation files

3. Click on `model/` folder
4. Verify both files are present:
   - ✅ wine_cultivar_model.pkl (1,039 bytes)
   - ✅ scaler.pkl (1,047 bytes)

---

## 🐛 TROUBLESHOOTING

### Issue: "Git is not recognized"
**Solution:** 
- Git not installed or not in PATH
- Install Git for Windows (see Step 1)
- **Restart PowerShell** after installation

### Issue: "Permission denied (publickey)"
**Solution:**
- Use HTTPS URL (not SSH): `https://github.com/Tolz-ctrl/...`
- Or set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### Issue: "Authentication failed"
**Solution:**
- GitHub no longer accepts password authentication
- Create Personal Access Token:
  1. Go to GitHub → Settings → Developer settings → Personal access tokens
  2. Generate new token (classic)
  3. Select scopes: `repo` (full control)
  4. Copy token and use as password

### Issue: "Repository not found"
**Solution:**
- Verify repository exists on GitHub
- Check repository URL is correct
- Ensure you have access to the repository

### Issue: "Model files not in repository"
**Solution:**
- Check if .gitignore excludes .pkl files
- Force add: `git add -f model/*.pkl`
- Commit and push again

### Issue: "Failed to push some refs"
**Solution:**
- Pull first: `git pull origin main --allow-unrelated-histories`
- Then push: `git push origin main`

---

## 📋 COMPLETE COMMAND SEQUENCE

Once Git is installed, run these commands in order:

```powershell
# Navigate to project
cd c:\Users\DELL\Desktop\Ass

# Initialize git
git init

# Configure git (first time only)
git config --global user.name "Toluwani Onipede"
git config --global user.email "your-email@example.com"

# Add remote
git remote add origin https://github.com/Tolz-ctrl/WineCultivar_Project_OnipedeToluwani_22CG031936.git

# Stage all files
git add .

# Commit
git commit -m "Complete Wine Cultivar Prediction System with deployment files"

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main

# Verify model files
git ls-files | findstr "pkl"

# Verify deployment files
git ls-files | findstr "Procfile runtime.txt requirements.txt"
```

---

## ✅ SUCCESS CHECKLIST

After pushing to GitHub:

- [ ] Git installed and configured
- [ ] Repository initialized
- [ ] Remote added
- [ ] All files committed
- [ ] Pushed to GitHub successfully
- [ ] Model files (.pkl) visible in repository
- [ ] Deployment files (Procfile, runtime.txt, requirements.txt) visible
- [ ] All documentation files present
- [ ] Repository accessible at GitHub URL

---

## 🎯 NEXT STEPS AFTER GITHUB PUSH

Once your code is on GitHub:

1. ✅ Verify repository on GitHub.com
2. ✅ Proceed with Render.com deployment (DEPLOYMENT_GUIDE_RENDER.md)
3. ✅ Or deploy to Railway.app (DEPLOYMENT_GUIDE_RAILWAY.md)

---

## 💡 ALTERNATIVE: GITHUB DESKTOP (GUI METHOD)

If you prefer a graphical interface:

1. **Download GitHub Desktop:**
   - Go to: https://desktop.github.com
   - Install GitHub Desktop

2. **Clone Repository:**
   - File → Clone Repository
   - Enter URL: https://github.com/Tolz-ctrl/WineCultivar_Project_OnipedeToluwani_22CG031936.git

3. **Copy Files:**
   - Copy all files from `c:\Users\DELL\Desktop\Ass` to cloned folder

4. **Commit and Push:**
   - GitHub Desktop will show all changes
   - Add commit message
   - Click "Commit to main"
   - Click "Push origin"

---

**After installing Git, return to this guide and execute the commands in Step 3!**

