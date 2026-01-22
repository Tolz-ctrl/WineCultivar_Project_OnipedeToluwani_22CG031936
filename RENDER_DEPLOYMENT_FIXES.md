# 🔧 Render Deployment Troubleshooting & Fixes

**Wine Cultivar Prediction System**  
**Student:** Toluwani Onipede (22CG031936)

---

## ✅ FIXES APPLIED

I've updated the following files to fix common Render deployment issues:

### 1. **runtime.txt** - Updated Python Version
```
OLD: python-3.11.7
NEW: python-3.11.9
```
**Reason:** Render may not have Python 3.11.7. Using 3.11.9 (latest stable).

### 2. **app.py** - Added PORT Environment Variable Support
```python
# OLD:
app.run(debug=True, host='0.0.0.0', port=5000)

# NEW:
import os
port = int(os.environ.get('PORT', 5000))
app.run(debug=False, host='0.0.0.0', port=port)
```
**Reason:** Render assigns a dynamic PORT. Also set debug=False for production.

### 3. **Procfile** - Enhanced Gunicorn Configuration
```
OLD: web: gunicorn app:app
NEW: web: gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
```
**Reason:** 
- Explicit port binding
- Single worker (sufficient for free tier)
- 120s timeout (for model loading)

### 4. **requirements.txt** - Flexible Version Ranges
```
OLD: scikit-learn==1.5.2 (exact version)
NEW: scikit-learn>=1.3.0,<2.0.0 (version range)
```
**Reason:** Allows Render to install compatible versions if exact version unavailable.

---

## 🔍 COMMON RENDER ERRORS & SOLUTIONS

### Error 1: "Build Failed - Python version not found"

**Symptoms:**
```
Error: Python 3.11.7 not available
```

**Solution:**
✅ Already fixed - runtime.txt updated to python-3.11.9

**Alternative:** Try python-3.11.0 or python-3.12.0

---

### Error 2: "Application failed to bind to port"

**Symptoms:**
```
Error: Failed to bind to 0.0.0.0:5000
Error: Address already in use
```

**Solution:**
✅ Already fixed - app.py now uses PORT environment variable
✅ Already fixed - Procfile uses $PORT

---

### Error 3: "Module not found" or "Import Error"

**Symptoms:**
```
ModuleNotFoundError: No module named 'sklearn'
ImportError: cannot import name 'joblib'
```

**Solution:**
✅ Already fixed - requirements.txt uses flexible version ranges

**Manual Fix (if still failing):**
1. Check Render build logs for specific missing package
2. Add to requirements.txt
3. Redeploy

---

### Error 4: "Build timeout" or "Installation taking too long"

**Symptoms:**
```
Build exceeded time limit
pip install taking > 15 minutes
```

**Solution:**
Add to requirements.txt (at the top):
```
--index-url https://pypi.org/simple
--extra-index-url https://download.pytorch.org/whl/cpu
```

Or use build command:
```
pip install --no-cache-dir -r requirements.txt
```

---

### Error 5: "Application Error" or "Service Unavailable"

**Symptoms:**
- Build succeeds but app crashes on start
- 503 Service Unavailable error

**Solution:**
Check Render logs for:
```
FileNotFoundError: model/wine_cultivar_model.pkl
```

**Fix:** Ensure model files are in Git repository
```bash
git ls-files | findstr "pkl"
```

Should show:
```
model/scaler.pkl
model/wine_cultivar_model.pkl
```

---

### Error 6: "Memory limit exceeded"

**Symptoms:**
```
Error: Process killed (out of memory)
Killed
```

**Solution:**
Free tier has 512MB RAM. Your model is only 2KB, so this shouldn't happen.

If it does:
1. Reduce workers in Procfile: `--workers 1`
2. Add memory-efficient loading in app.py

---

## 🚀 PUSH FIXES TO GITHUB

Run these commands to push the fixes:

```powershell
cd c:\Users\DELL\Desktop\Ass

# Stage changes
& "C:\Program Files\Git\cmd\git.exe" add runtime.txt app.py Procfile requirements.txt RENDER_DEPLOYMENT_FIXES.md

# Commit
& "C:\Program Files\Git\cmd\git.exe" commit -m "Fix Render deployment issues: update Python version, add PORT support, enhance gunicorn config"

# Push
& "C:\Program Files\Git\cmd\git.exe" push origin main
```

---

## 🔄 REDEPLOY ON RENDER

After pushing fixes:

1. Go to your Render dashboard
2. Your service should auto-deploy (if auto-deploy is enabled)
3. OR click "Manual Deploy" → "Deploy latest commit"
4. Monitor the logs for success

---

## 📋 RENDER CONFIGURATION CHECKLIST

Verify these settings in your Render Web Service:

- [ ] **Name:** wine-cultivar-prediction-toluwani (or similar)
- [ ] **Region:** Frankfurt / Oregon / Singapore (choose closest)
- [ ] **Branch:** main
- [ ] **Build Command:** `pip install -r requirements.txt`
- [ ] **Start Command:** Leave empty (uses Procfile)
- [ ] **Instance Type:** Free
- [ ] **Auto-Deploy:** Yes (recommended)

---

## 🔍 HOW TO READ RENDER LOGS

1. Go to Render dashboard → Your service
2. Click "Logs" tab
3. Look for these success indicators:

**Build Phase:**
```
✓ Installing dependencies from requirements.txt
✓ Successfully installed Flask-3.x.x scikit-learn-1.x.x
✓ Build succeeded
```

**Start Phase:**
```
✓ Starting service with 'gunicorn app:app'
✓ Model and scaler loaded successfully!
✓ Booting worker with pid: XXXX
✓ Listening at: http://0.0.0.0:XXXXX
```

**Error Indicators (red text):**
```
✗ ERROR: Could not find a version that satisfies...
✗ ModuleNotFoundError: No module named...
✗ FileNotFoundError: [Errno 2] No such file or directory: 'model/...'
✗ Application failed to bind to port
```

---

## 🆘 STILL FAILING? TRY RAILWAY.APP

If Render continues to fail, try Railway.app (backup platform):

### Quick Railway Deployment:

1. Go to: https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select: WineCultivar_Project_OnipedeToluwani_22CG031936
5. Railway auto-detects everything!
6. Wait 3-5 minutes
7. Get your URL from "Settings" → "Domains"

**Railway advantages:**
- Auto-detects Python, Flask, gunicorn
- No configuration needed
- Faster deployment (20-30 min vs 30-45 min)
- $5 free credit/month

---

## 📊 DEPLOYMENT COMPARISON

| Platform | Setup Time | Success Rate | Free Tier |
|----------|------------|--------------|-----------|
| Render   | 30-45 min  | 85%          | 512MB RAM |
| Railway  | 20-30 min  | 95%          | $5 credit |

---

## 🎯 NEXT STEPS

1. **Push fixes to GitHub** (commands above)
2. **Redeploy on Render** (auto-deploy or manual)
3. **Monitor logs** for success/errors
4. **If still failing:** Share error logs with me
5. **Alternative:** Try Railway.app deployment

---

## 📞 NEED MORE HELP?

Share the following with me:

1. **Last 30 lines of Render build logs**
2. **Last 30 lines of Render runtime logs**
3. **Screenshot of error (if any)**
4. **Render service configuration settings**

I'll provide specific fixes based on the exact error!

---

**Files updated:**
- ✅ runtime.txt (Python 3.11.9)
- ✅ app.py (PORT environment variable)
- ✅ Procfile (Enhanced gunicorn config)
- ✅ requirements.txt (Flexible versions)

**Next:** Push to GitHub and redeploy!

