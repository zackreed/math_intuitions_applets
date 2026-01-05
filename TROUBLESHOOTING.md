# Color Scheme System - Troubleshooting Guide

## 🔧 Common Issues & Solutions

### Issue 1: I changed the scheme but colors didn't update

**Symptoms:**
- Edited `global-scheme-config.js` but pages still show old colors
- Some elements changed but others didn't

**Solutions:**

1. **Hard refresh your browser**
   - Windows/Linux: `Ctrl + F5` or `Ctrl + Shift + R`
   - Mac: `Cmd + Shift + R`
   - This clears cached JavaScript files

2. **Check browser console for errors**
   - Open DevTools (F12)
   - Look for red error messages
   - Common error: "styleConfig is not defined" means scripts loaded in wrong order

3. **Verify script order in HTML**
   Scripts must be in this order at the END of `<body>`:
   ```html
   <script src="../js/color-schemes.js"></script>
   <script src="../js/style-config.js"></script>
   <script src="../js/global-scheme-config.js"></script>
   </body>
   ```

4. **Check that only ONE scheme is uncommented**
   In `global-scheme-config.js`, inside `applyGlobalScheme()`:
   ```javascript
   function applyGlobalScheme() {
       // All others should be commented out with //
       styleConfig.setScheme('dark_muted_pastels');  // Only ONE active
   }
   ```

---

### Issue 2: Some elements have the wrong colors

**Symptoms:**
- Most of the page uses the new scheme
- But buttons, links, or specific elements still have old colors
- Mixed color schemes on one page

**Solutions:**

1. **Check for hardcoded inline styles**
   Look for elements with `style="color: #..."` in HTML:
   ```html
   <!-- BAD - hardcoded color -->
   <a href="..." style="color: #00d9ff;">Link</a>
   
   <!-- GOOD - uses CSS variable -->
   <a href="..." class="back-to-home">Link</a>
   ```

2. **Check for hardcoded colors in JavaScript**
   Canvas drawing code might have hardcoded hex colors:
   ```javascript
   // BAD - hardcoded
   ctx.strokeStyle = '#00d9ff';
   
   // GOOD - uses scheme
   ctx.strokeStyle = styleConfig.getColor('highlight');
   ```

3. **Verify CSS uses variables**
   CSS should reference `var(--variable-name)`:
   ```css
   /* BAD - hardcoded */
   .button {
       background: #00d9ff;
   }
   
   /* GOOD - uses variable */
   .button {
       background: var(--highlight);
   }
   ```

---

### Issue 3: Console shows "scheme not found"

**Symptoms:**
- Browser console shows: `Color scheme 'xyz' not found. Using 'default'.`

**Solutions:**

1. **Check scheme name spelling**
   Scheme names are case-sensitive and must match exactly:
   ```javascript
   // WRONG - typo
   styleConfig.setScheme('dark_muted_pastel');  // Missing 's'
   
   // RIGHT
   styleConfig.setScheme('dark_muted_pastels');
   ```

2. **Verify scheme exists**
   Check `/js/color-schemes.js` to see available schemes:
   ```javascript
   const COLOR_SCHEMES = {
       'default': { ... },
       'dark_muted_pastels': { ... },
       // etc
   };
   ```

---

### Issue 4: Canvas/applet colors don't update

**Symptoms:**
- Page colors changed but canvas graphics still use old colors
- Interactive applet doesn't reflect new scheme

**Solutions:**

1. **Check if applet listens for scheme changes**
   Add this to your applet's JavaScript:
   ```javascript
   // Redraw when scheme changes
   window.addEventListener('colorSchemeChanged', function() {
       draw();  // Call your draw function
   });
   ```

2. **Use styleConfig.getColor() in draw functions**
   ```javascript
   function draw() {
       // Get colors from current scheme
       ctx.fillStyle = styleConfig.getColor('background');
       ctx.strokeStyle = styleConfig.getColor('highlight');
       // ... rest of drawing code
   }
   ```

3. **Call draw function after loading**
   ```javascript
   // Wait for scheme to be applied
   window.addEventListener('colorSchemeChanged', draw);
   
   // Also draw on initial load
   window.addEventListener('load', draw);
   ```

---

### Issue 5: Different pages show different schemes (unintentionally)

**Symptoms:**
- Index page has one color scheme
- Applet pages have another
- Expected: all pages to match

**Solutions:**

1. **Check for page-specific overrides**
   Look for this in individual HTML files:
   ```html
   <script src="../js/global-scheme-config.js"></script>
   <script>
       // This overrides the global setting!
       styleConfig.setScheme('different_scheme');
   </script>
   ```
   Remove the override if you want all pages to match.

2. **Check for path-based logic**
   In `global-scheme-config.js`, look for the "Advanced" section:
   ```javascript
   (function() {
       const path = window.location.pathname;
       if (path.includes('/applets/')) {
           styleConfig.setScheme('dark_muted_pastels');
       } else if (path.includes('/pages/')) {
           styleConfig.setScheme('default');  // Different scheme!
       }
   })();
   ```
   Comment this out if you don't want different schemes per section.

---

### Issue 6: Scripts load but nothing happens

**Symptoms:**
- No errors in console
- Scripts are loaded
- But scheme doesn't apply

**Solutions:**

1. **Check script execution timing**
   Scripts must run AFTER DOM is ready. Verify they're at the end of `<body>`:
   ```html
   <body>
       <!-- All your content -->
       <div>...</div>
       
       <!-- Scripts at the END -->
       <script src="../js/color-schemes.js"></script>
       <script src="../js/style-config.js"></script>
       <script src="../js/global-scheme-config.js"></script>
   </body>
   ```

2. **Check file paths**
   For pages in `/pages/` folder, paths need `../`:
   ```html
   <!-- WRONG (for files in /pages/) -->
   <script src="js/style-config.js"></script>
   
   <!-- RIGHT -->
   <script src="../js/style-config.js"></script>
   ```
   
   For files in root (like index.html), no `../`:
   ```html
   <!-- RIGHT (for index.html) -->
   <script src="js/style-config.js"></script>
   ```

---

## 🧪 Testing Your Setup

### Test 1: Verify Scripts Load

1. Open any page in your browser
2. Open DevTools Console (F12)
3. Type: `styleConfig.getAvailableSchemes()`
4. Should see array of scheme names

If error "styleConfig is not defined":
- Scripts didn't load or loaded in wrong order

### Test 2: Verify Scheme Applied

1. Open DevTools Console
2. Type: `styleConfig.getCurrentScheme()`
3. Should show your active scheme name (e.g., "dark_muted_pastels")

If shows "default" but you set something else:
- Check for typos
- Check scheme exists in color-schemes.js

### Test 3: Verify DOM Attributes Set

1. Open DevTools Elements tab
2. Inspect the `<html>` element
3. Should see: `<html lang="en" data-color-scheme="dark_muted_pastels">`

If attribute missing:
- Scripts loaded before DOM was ready
- Move scripts to end of `<body>`

### Test 4: Verify CSS Variables Available

1. Open DevTools Console
2. Type: `getComputedStyle(document.documentElement).getPropertyValue('--highlight')`
3. Should show a color value (e.g., "#ABDADC")

If empty or wrong value:
- CSS file not loaded
- Check `<link rel="stylesheet" href="css/color-schemes.css">`

---

## 📊 Diagnostic Checklist

Run through this checklist to diagnose issues:

- [ ] Scripts in correct order: color-schemes.js → style-config.js → global-scheme-config.js
- [ ] Scripts at END of `<body>` (not in `<head>`)
- [ ] color-schemes.css linked in `<head>`
- [ ] Only ONE scheme uncommented in global-scheme-config.js
- [ ] Hard refresh browser (Ctrl+F5 / Cmd+Shift+R)
- [ ] No errors in browser console
- [ ] `styleConfig.getCurrentScheme()` returns expected scheme
- [ ] `<html>` element has `data-color-scheme` attribute
- [ ] CSS variables available (test with getComputedStyle)
- [ ] No inline `style="color: #..."` overriding colors

---

## 🆘 Still Having Issues?

1. **Check browser console** - Always start here
2. **View page source** - Verify script tags are present and correct
3. **Compare with working example** - Look at `applets/geometric-series.html`
4. **Test in incognito mode** - Rules out extension interference
5. **Try a different browser** - Rules out browser-specific issues

---

## 💡 Tips for Success

### DO:
✅ Keep scripts at end of `<body>`
✅ Use CSS variables (`var(--highlight)`)
✅ Use `styleConfig.getColor('highlight')` in JavaScript
✅ Hard refresh after changes
✅ Check console for errors

### DON'T:
❌ Put scripts in `<head>` (DOM won't be ready)
❌ Use inline styles with hardcoded colors
❌ Uncomment multiple schemes at once
❌ Modify `style-config.js` or `color-schemes.js` (unless adding features)
❌ Forget to refresh browser after changes
