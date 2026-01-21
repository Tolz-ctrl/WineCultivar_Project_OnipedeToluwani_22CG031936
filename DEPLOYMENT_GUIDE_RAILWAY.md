# 🚂 Complete Deployment Guide: Railway.app
**Wine Cultivar Prediction System - Backup Deployment**  
**Student:** Toluwani Onipede (22CG031936)  
**Estimated Time:** 20-30 minutes

---

## 🎯 WHY RAILWAY AS BACKUP?

Railway is the **fastest deployment option** with:
- ✅ Auto-detection of Flask apps (minimal configuration)
- ✅ No cold starts (better performance than Render free tier)
- ✅ $5 free credit monthly (sufficient for academic project)
- ✅ Simpler setup process
- ✅ Faster builds

**Use Railway if:**
- Render deployment fails or is slow
- You need faster response times
- You want simpler configuration

---

## ✅ PRE-DEPLOYMENT CHECKLIST

Same as Render:
- [x] GitHub repository ready
- [x] Model files committed (*.pkl)
- [x] `Procfile` created
- [x] `requirements.txt` updated with gunicorn
- [x] All code files pushed to GitHub

---

## 🌐 STEP 1: CREATE RAILWAY ACCOUNT

### 1.1 Sign Up
1. Go to https://railway.app
2. Click **"Login"** → **"Login with GitHub"**
3. Authorize Railway to access your GitHub
4. Complete profile setup

**Note:** Railway requires GitHub authentication (no email signup).

### 1.2 Verify Free Credit
- Check dashboard for **$5.00 free credit**
- This is enough for ~1 month of continuous running
- No credit card required initially

---

## 🚀 STEP 2: DEPLOY FROM GITHUB

### 2.1 Create New Project

1. From Railway Dashboard, click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose repository: `WineCultivar_Project_OnipedeToluwani_22CG031936`
4. Click **"Deploy Now"**

**That's it!** Railway auto-detects Flask and starts deployment.

### 2.2 Railway Auto-Configuration

Railway automatically:
- ✅ Detects Python project
- ✅ Finds `requirements.txt`
- ✅ Reads `Procfile` for start command
- ✅ Sets up environment
- ✅ Installs dependencies
- ✅ Starts your app

**No manual configuration needed!**

---

## ⏳ STEP 3: MONITOR DEPLOYMENT

### 3.1 Watch Build Logs

Click on your deployment to see logs:

```
==> Building...
==> Installing Python 3.11
==> Installing dependencies from requirements.txt
    Collecting Flask==3.1.0
    Collecting scikit-learn==1.5.2
    ...
    Successfully installed all packages
==> Starting application
    [INFO] Starting gunicorn
    ✓ Model and scaler loaded successfully!
==> Deployment successful!
```

**Build time:** 2-4 minutes (faster than Render)

### 3.2 Check Deployment Status

Look for:
- ✅ Green "Active" status
- ✅ "Model and scaler loaded successfully!" in logs
- ✅ No error messages

---

## 🌍 STEP 4: GET YOUR PUBLIC URL

### 4.1 Generate Public Domain

1. Click on your deployment
2. Go to **"Settings"** tab
3. Scroll to **"Networking"** section
4. Click **"Generate Domain"**

Railway provides a URL like:
```
https://winecultivar-project-onipedetoluwani-22cg031936-production.up.railway.app
```

### 4.2 Custom Domain (Optional)

You can add a custom domain if you have one:
1. Click **"Custom Domain"**
2. Enter your domain
3. Update DNS settings as instructed

**For academic submission, the Railway domain is fine!**

---

## 🧪 STEP 5: TEST YOUR DEPLOYMENT

### 5.1 Open Your URL

Click the generated URL or copy-paste into browser.

### 5.2 Verify Application

1. **Check form loads** with 6 input fields
2. **Test with sample data:**
   ```
   Alcohol: 14.23
   Malic Acid: 1.71
   Ash: 2.43
   Alcalinity of Ash: 15.6
   Magnesium: 127
   Flavanoids: 3.06
   ```
3. **Click "Predict Cultivar"**
4. **Verify result:** "Cultivar 0" with high confidence

### 5.3 Performance Check

Railway free tier performance:
- **First load:** < 1 second (no cold start!)
- **Predictions:** < 100ms
- **Uptime:** 99.9%

---

## 💰 STEP 6: MONITOR USAGE

### 6.1 Check Credit Usage

1. Go to **"Usage"** tab in dashboard
2. Monitor your $5 credit
3. Typical usage for this project: **$0.50-$1.00/month**

### 6.2 Set Up Alerts (Optional)

1. Go to **"Settings"**
2. Enable usage alerts
3. Get notified at 50%, 75%, 90% credit usage

---

## 🔄 STEP 7: AUTO-DEPLOYMENT

Railway automatically redeploys on Git push:

```bash
# Make changes
git add .
git commit -m "Update model"
git push origin main

# Railway automatically rebuilds (takes 1-2 minutes)
```

---

## 🐛 TROUBLESHOOTING

### Issue: "Application Failed to Respond"
**Solution:**
1. Check logs for errors
2. Verify `Procfile` exists: `web: gunicorn app:app`
3. Ensure app.py has `if __name__ == '__main__'` block

### Issue: "Module Not Found" Errors
**Solution:**
1. Verify all dependencies in `requirements.txt`
2. Check for typos in package names
3. Redeploy from Railway dashboard

### Issue: "Model Files Not Found"
**Solution:**
1. Verify model files are in Git repository
2. Check file paths in app.py match actual structure
3. Ensure files are in `model/` directory

### Issue: Running Out of Free Credit
**Solution:**
1. Railway charges ~$0.02/hour for active service
2. For academic project, $5 lasts 250 hours (10+ days)
3. If needed, pause service when not testing
4. Or add $5 credit card backup

---

## ⚙️ ADVANCED CONFIGURATION (OPTIONAL)

### Environment Variables

If you need to add environment variables:

1. Go to **"Variables"** tab
2. Click **"New Variable"**
3. Add key-value pairs (e.g., `FLASK_ENV=production`)

### Custom Start Command

If Procfile doesn't work:

1. Go to **"Settings"** → **"Deploy"**
2. Set custom start command: `gunicorn app:app --bind 0.0.0.0:$PORT`

---

## 📊 RAILWAY VS RENDER COMPARISON

| Feature | Railway | Render |
|---------|---------|--------|
| **Setup Time** | 20 min | 30 min |
| **Build Speed** | 2-4 min | 3-5 min |
| **Cold Starts** | None | 2-3 sec |
| **Free Tier** | $5 credit | 750 hrs |
| **Performance** | Better | Good |
| **Documentation** | Good | Excellent |
| **Reliability** | High | Very High |

**Recommendation:** Use Railway if you need speed, Render if you need stability.

---

## ✅ DEPLOYMENT SUCCESS CHECKLIST

- [ ] Project deployed successfully
- [ ] Public URL generated
- [ ] Application loads without errors
- [ ] Form displays all 6 fields
- [ ] Test prediction works correctly
- [ ] Confidence score shows
- [ ] No errors in Railway logs
- [ ] Usage is within free credit

---

## 🎯 FINAL STEPS

1. ✅ Copy your Railway URL
2. ✅ Test thoroughly
3. ✅ Update `WineCultivar_hosted_webGUI_link.txt`
4. ✅ Monitor credit usage
5. ✅ Keep as backup if using Render

**Your Railway deployment is complete! 🚂**

---

## 💡 PRO TIPS

1. **Keep both deployments:** Deploy to both Render and Railway, submit the more reliable URL
2. **Monitor uptime:** Check both URLs before final submission
3. **Test on mobile:** Ensure responsive design works
4. **Screenshot results:** Save evidence of working deployment
5. **Backup URL:** Include both URLs in your documentation

**Railway is your fast, reliable backup deployment! 🎉**

