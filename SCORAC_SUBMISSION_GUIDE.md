# 📤 Final Submission Guide: Scorac.com Upload
**Wine Cultivar Prediction System**  
**Student:** Toluwani Onipede (22CG031936)  
**Deadline:** January 21, 2026

---

## 🎯 DUAL SUBMISSION REQUIREMENT

Your project requires **TWO submissions:**

1. **Live Deployment** → Cloud hosting (Render/Railway)
2. **File Upload** → Scorac.com platform

Both are required for complete submission!

---

## ✅ PRE-SUBMISSION CHECKLIST

### Before Uploading to Scorac.com:

- [ ] **Model trained successfully**
  - Test accuracy: 94.44% ✅
  - Model files generated: wine_cultivar_model.pkl, scaler.pkl ✅

- [ ] **Application deployed to cloud**
  - Platform: Render.com or Railway.app
  - Live URL tested and working
  - All features functional

- [ ] **WineCultivar_hosted_webGUI_link.txt updated**
  - Student name and matric number filled
  - Live URL inserted
  - Deployment date added
  - All sections completed

- [ ] **Project folder properly named**
  - Exact name: `WineCultivar_Project_OnipedeToluwani_22CG031936`
  - No spaces, special characters, or variations

- [ ] **All required files present**
  - See file checklist below

---

## 📁 REQUIRED FILES CHECKLIST

### Core Application Files:
- [x] `app.py` - Flask web application (118 lines)
- [x] `requirements.txt` - Dependencies (18 lines, updated with gunicorn)
- [x] `Procfile` - Deployment configuration
- [x] `runtime.txt` - Python version specification

### Model Files:
- [x] `model/model_building.ipynb` - Training notebook
- [x] `model/train_model.py` - Training script
- [x] `model/wine_cultivar_model.pkl` - Trained model (1,039 bytes)
- [x] `model/scaler.pkl` - Fitted scaler (1,047 bytes)

### Frontend Files:
- [x] `templates/index.html` - Web interface (232 lines)
- [x] `static/style.css` - Optional styling

### Documentation Files:
- [x] `README.md` - Project documentation
- [x] `WineCultivar_hosted_webGUI_link.txt` - **CRITICAL** (Updated with your URL)
- [x] `DEPLOYMENT_ANALYSIS.md` - Platform comparison
- [x] `DEPLOYMENT_GUIDE_RENDER.md` - Render deployment guide
- [x] `DEPLOYMENT_GUIDE_RAILWAY.md` - Railway deployment guide
- [x] `SCORAC_SUBMISSION_GUIDE.md` - This file
- [x] `SETUP_GUIDE.md` - Setup instructions
- [x] `PROJECT_SUMMARY.md` - Technical summary
- [x] `CHECKLIST.md` - Pre-submission checklist

**Total Files:** 18+ files

---

## 📦 STEP 1: PREPARE PROJECT FOLDER

### 1.1 Rename Project Folder

**CRITICAL:** The folder name must be EXACTLY:
```
WineCultivar_Project_OnipedeToluwani_22CG031936
```

In Windows:
```powershell
# Navigate to parent directory
cd c:\Users\DELL\Desktop

# Rename folder (if not already named correctly)
Rename-Item -Path "Ass" -NewName "WineCultivar_Project_OnipedeToluwani_22CG031936"
```

### 1.2 Verify Folder Structure

```
WineCultivar_Project_OnipedeToluwani_22CG031936/
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── WineCultivar_hosted_webGUI_link.txt  ← MUST have your live URL!
├── model/
│   ├── model_building.ipynb
│   ├── train_model.py
│   ├── wine_cultivar_model.pkl  ← MUST be present!
│   └── scaler.pkl               ← MUST be present!
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── [All documentation files]
```

### 1.3 Final File Check

Run this command to verify all critical files:

```powershell
cd c:\Users\DELL\Desktop\WineCultivar_Project_OnipedeToluwani_22CG031936

# Check model files exist
dir model\*.pkl

# Check deployment files
dir Procfile, runtime.txt, requirements.txt

# Check updated submission file
type WineCultivar_hosted_webGUI_link.txt | findstr "http"
```

**Expected output:** Should show your live URL!

---

## 🗜️ STEP 2: CREATE ZIP ARCHIVE

### 2.1 Create ZIP File

**Option A: Using Windows Explorer**
1. Navigate to `c:\Users\DELL\Desktop`
2. Right-click on `WineCultivar_Project_OnipedeToluwani_22CG031936` folder
3. Select **"Send to"** → **"Compressed (zipped) folder"**
4. Rename to: `WineCultivar_Project_OnipedeToluwani_22CG031936.zip`

**Option B: Using PowerShell**
```powershell
cd c:\Users\DELL\Desktop

Compress-Archive -Path "WineCultivar_Project_OnipedeToluwani_22CG031936" -DestinationPath "WineCultivar_Project_OnipedeToluwani_22CG031936.zip"
```

### 2.2 Verify ZIP File

1. **Check file size:** Should be ~5-15 MB (includes model files)
2. **Test extraction:** Extract to a test folder and verify all files present
3. **Verify model files in ZIP:** Ensure *.pkl files are included

```powershell
# Check ZIP contents
Expand-Archive -Path "WineCultivar_Project_OnipedeToluwani_22CG031936.zip" -DestinationPath "test_extract" -Force

# Verify model files
dir test_extract\WineCultivar_Project_OnipedeToluwani_22CG031936\model\*.pkl
```

---

## 🌐 STEP 3: UPLOAD TO SCORAC.COM

### 3.1 Access Scorac.com

1. Go to **https://scorac.com** (or your institution's submission portal)
2. Log in with your student credentials:
   - Matric Number: **22CG031936**
   - Password: [Your password]

### 3.2 Navigate to Submission Page

1. Find **"Machine Learning"** or **"Data Science"** course
2. Click on **"Wine Cultivar Prediction Project"** assignment
3. Click **"Submit Assignment"** or **"Upload"**

### 3.3 Upload ZIP File

1. Click **"Choose File"** or **"Browse"**
2. Select: `WineCultivar_Project_OnipedeToluwani_22CG031936.zip`
3. **DO NOT** upload individual files - upload the ZIP!
4. Wait for upload to complete (may take 1-2 minutes)

### 3.4 Fill Submission Form

Complete any required fields:

| Field | Value |
|-------|-------|
| **Student Name** | Toluwani Onipede |
| **Matric Number** | 22CG031936 |
| **Project Title** | Wine Cultivar Origin Prediction System |
| **Live URL** | [Your Render/Railway URL] |
| **GitHub Repository** | https://github.com/Tolz-ctrl/WineCultivar_Project_OnipedeToluwani_22CG031936.git |
| **ML Algorithm** | Logistic Regression |
| **Test Accuracy** | 94.44% |
| **Comments** | Deployed on [Render/Railway], all features working |

### 3.5 Submit

1. Review all information
2. Click **"Submit"** or **"Upload Assignment"**
3. Wait for confirmation message
4. **SAVE** the submission confirmation (screenshot or PDF)

---

## ✅ STEP 4: VERIFY SUBMISSION

### 4.1 Confirmation Checks

After submission, verify:
- [ ] Confirmation email received
- [ ] Submission shows in your Scorac.com dashboard
- [ ] File size matches your ZIP file
- [ ] Submission timestamp is before deadline
- [ ] Status shows "Submitted" (not "Draft")

### 4.2 Test Your Live URL One More Time

```powershell
# Test URL is accessible
curl [YOUR_LIVE_URL]
```

Or open in browser and test prediction with sample data.

---

## 🚨 COMMON SUBMISSION ERRORS

### Error: "File too large"
**Solution:** 
- Check ZIP size (should be < 50MB)
- Remove unnecessary files (.git folder, __pycache__, etc.)
- Compress with maximum compression

### Error: "Invalid folder structure"
**Solution:**
- Ensure folder name is EXACTLY: `WineCultivar_Project_OnipedeToluwani_22CG031936`
- ZIP should contain the folder, not just files
- Extract and re-zip if needed

### Error: "Missing required files"
**Solution:**
- Verify `WineCultivar_hosted_webGUI_link.txt` is present and updated
- Ensure model/*.pkl files are included
- Check all files from checklist above

### Error: "Live URL not working"
**Solution:**
- Test URL before submission
- Ensure deployment is active (not paused)
- Check for typos in URL
- Verify HTTPS (not HTTP)

---

## 📋 FINAL SUBMISSION CHECKLIST

Before clicking "Submit":

- [ ] Project folder renamed correctly
- [ ] All 18+ files present
- [ ] Model files (*.pkl) included
- [ ] WineCultivar_hosted_webGUI_link.txt updated with live URL
- [ ] ZIP file created and tested
- [ ] Live URL tested and working
- [ ] Scorac.com login credentials ready
- [ ] Submission form filled correctly
- [ ] Deadline confirmed (January 21, 2026)
- [ ] Backup copy of ZIP file saved

---

## 🎯 SUBMISSION TIMELINE

**Recommended Schedule:**

| Time Before Deadline | Task |
|----------------------|------|
| **48 hours** | Deploy to Render/Railway |
| **24 hours** | Test deployment thoroughly |
| **12 hours** | Update WineCultivar_hosted_webGUI_link.txt |
| **6 hours** | Create ZIP and verify |
| **2 hours** | Upload to Scorac.com |
| **1 hour** | Final verification |
| **Deadline** | Relax! ✅ |

**DO NOT wait until the last minute!**

---

## 📞 EMERGENCY CONTACTS

If you encounter issues:

1. **Technical Issues:** Check deployment guides troubleshooting sections
2. **Scorac.com Issues:** Contact your course instructor
3. **Deployment Issues:** Use backup platform (Railway if Render fails)

---

## 🎉 POST-SUBMISSION

After successful submission:

1. ✅ Save confirmation email/screenshot
2. ✅ Keep ZIP file backup
3. ✅ Monitor live URL (keep deployment active)
4. ✅ Note submission timestamp
5. ✅ Prepare for presentation (if required)

**Congratulations on completing your Wine Cultivar Prediction System! 🍷**

---

**Your project is ready for submission! Good luck! 🎓**

