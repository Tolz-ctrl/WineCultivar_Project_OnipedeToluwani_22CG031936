# 🚀 Complete Deployment Guide: Render.com
**Wine Cultivar Prediction System**  
**Student:** Toluwani Onipede (22CG031936)  
**Estimated Time:** 30-45 minutes

---

## ✅ PRE-DEPLOYMENT CHECKLIST

Before starting, verify you have:

- [x] GitHub account created
- [x] GitHub repository: `https://github.com/Tolz-ctrl/WineCultivar_Project_OnipedeToluwani_22CG031936.git`
- [x] Model files trained and ready:
  - `model/wine_cultivar_model.pkl` (1039 bytes)
  - `model/scaler.pkl` (1047 bytes)
- [x] All code files in repository
- [x] Deployment files created:
  - `Procfile` ✅
  - `runtime.txt` ✅
  - `requirements.txt` (updated with gunicorn) ✅

---

## 📦 STEP 1: PREPARE YOUR GITHUB REPOSITORY

### 1.1 Commit All Required Files

Open terminal in your project directory and run:

```bash
cd c:\Users\DELL\Desktop\Ass

# Check git status
git status

# Add all files (if not already committed)
git add .

# Commit with message
git commit -m "Add deployment files for Render"

# Push to GitHub
git push origin main
```

### 1.2 Verify Model Files Are in Repository

**CRITICAL:** Model files MUST be in your Git repository!

```bash
# Check if model files exist in repo
git ls-files | findstr /i "pkl"
```

Expected output:
```
model/scaler.pkl
model/wine_cultivar_model.pkl
```

If model files are NOT showing:
```bash
# Remove from .gitignore if present
# Then add and commit
git add model/*.pkl
git commit -m "Add trained model files"
git push origin main
```

---

## 🌐 STEP 2: CREATE RENDER ACCOUNT

### 2.1 Sign Up
1. Go to https://render.com
2. Click **"Get Started for Free"**
3. Sign up with GitHub (recommended) or email
4. Verify your email address
5. Complete profile setup

**No credit card required for free tier!**

---

## 🔧 STEP 3: CREATE NEW WEB SERVICE

### 3.1 Connect GitHub Repository

1. From Render Dashboard, click **"New +"** → **"Web Service"**
2. Click **"Connect GitHub"** (if first time)
3. Authorize Render to access your GitHub
4. Select repository: `WineCultivar_Project_OnipedeToluwani_22CG031936`
5. Click **"Connect"**

### 3.2 Configure Web Service

Fill in the following settings:

| Setting | Value |
|---------|-------|
| **Name** | `wine-cultivar-prediction-toluwani` |
| **Region** | Choose closest to Nigeria (e.g., Frankfurt or Singapore) |
| **Branch** | `main` |
| **Root Directory** | (leave blank) |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |

### 3.3 Select Free Plan

1. Scroll down to **"Instance Type"**
2. Select **"Free"** plan
   - 512 MB RAM
   - Shared CPU
   - 750 hours/month

3. Click **"Create Web Service"**

---

## ⏳ STEP 4: MONITOR DEPLOYMENT

### 4.1 Watch Build Logs

Render will now:
1. Clone your repository
2. Install Python 3.11.7
3. Install dependencies (this takes 3-5 minutes for scikit-learn)
4. Start gunicorn server

**Expected build log output:**
```
==> Cloning from https://github.com/Tolz-ctrl/WineCultivar_Project...
==> Downloading Python 3.11.7
==> Running 'pip install -r requirements.txt'
    Collecting Flask==3.1.0
    Collecting scikit-learn==1.5.2
    ...
    Successfully installed Flask-3.1.0 scikit-learn-1.5.2 ...
==> Running 'gunicorn app:app'
    [INFO] Starting gunicorn 21.2.0
    [INFO] Listening at: http://0.0.0.0:10000
    ✓ Model and scaler loaded successfully!
==> Build successful!
==> Your service is live 🎉
```

### 4.2 Check for Errors

**Common errors and fixes:**

**Error:** `ModuleNotFoundError: No module named 'sklearn'`
- **Fix:** Ensure `scikit-learn==1.5.2` is in requirements.txt

**Error:** `FileNotFoundError: model/wine_cultivar_model.pkl`
- **Fix:** Model files not in Git. Commit and push them!

**Error:** `No module named 'gunicorn'`
- **Fix:** Add `gunicorn==21.2.0` to requirements.txt

---

## 🎉 STEP 5: TEST YOUR DEPLOYMENT

### 5.1 Get Your URL

Once deployed, Render provides a URL like:
```
https://wine-cultivar-prediction-toluwani.onrender.com
```

### 5.2 Test the Application

1. **Open the URL in browser**
2. **Verify the form loads** with 6 input fields
3. **Test with sample data:**
   - Alcohol: `14.23`
   - Malic Acid: `1.71`
   - Ash: `2.43`
   - Alcalinity of Ash: `15.6`
   - Magnesium: `127`
   - Flavanoids: `3.06`

4. **Click "Predict Cultivar"**
5. **Expected result:** "Cultivar 0" with ~95-100% confidence

### 5.3 Verify Model Loading

Check the Render logs for:
```
✓ Model and scaler loaded successfully!
```

---

## 📝 STEP 6: UPDATE SUBMISSION FILES

### 6.1 Copy Your Deployment URL

Example: `https://wine-cultivar-prediction-toluwani.onrender.com`

### 6.2 Update WineCultivar_hosted_webGUI_link.txt

Replace the content with your actual URL (see template in next section).

---

## 🔄 STEP 7: AUTO-DEPLOYMENT (OPTIONAL)

Render automatically redeploys when you push to GitHub!

```bash
# Make any changes to your code
git add .
git commit -m "Update prediction logic"
git push origin main

# Render will automatically rebuild and deploy
```

---

## 🐛 TROUBLESHOOTING

### Issue: Build Fails with Memory Error
**Solution:** scikit-learn installation needs memory. Wait and retry, or use Railway instead.

### Issue: App Loads but "Model not loaded" Error
**Solution:** 
1. Check logs for file path errors
2. Verify model files are in `model/` directory in Git
3. Check file names match exactly: `wine_cultivar_model.pkl` and `scaler.pkl`

### Issue: Cold Start Delays
**Solution:** Free tier sleeps after 15 min inactivity. First request takes 2-3 seconds. This is normal.

### Issue: 502 Bad Gateway
**Solution:** 
1. Check if gunicorn is starting correctly in logs
2. Verify `Procfile` contains: `web: gunicorn app:app`
3. Ensure port binding is correct (Render uses PORT env variable automatically)

---

## ✅ DEPLOYMENT SUCCESS CHECKLIST

- [ ] Build completed without errors
- [ ] Service shows "Live" status (green dot)
- [ ] URL opens and shows the form
- [ ] All 6 input fields are visible
- [ ] Test prediction returns correct result
- [ ] Confidence score displays
- [ ] No console errors in browser (F12)
- [ ] Model loading message in Render logs

---

## 📊 EXPECTED PERFORMANCE

- **Build Time:** 3-5 minutes (first time)
- **Cold Start:** 2-3 seconds (after inactivity)
- **Warm Response:** < 1 second
- **Prediction Time:** < 100ms
- **Uptime:** 99.9% (free tier)

---

## 🎯 FINAL STEPS

1. ✅ Copy your live URL
2. ✅ Test thoroughly with multiple inputs
3. ✅ Update `WineCultivar_hosted_webGUI_link.txt`
4. ✅ Commit and push the updated file
5. ✅ Prepare for Scorac.com submission

**Your Render deployment is complete! 🎉**

Next: See `DEPLOYMENT_GUIDE_RAILWAY.md` for backup deployment option.

