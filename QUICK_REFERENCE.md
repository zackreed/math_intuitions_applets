# Color Scheme System - Quick Reference

## 🎨 Change Global Colors (Most Common)

**File:** `/js/global-scheme-config.js`  
**Line:** ~31 (inside `applyGlobalScheme()` function)

```javascript
function applyGlobalScheme() {
    styleConfig.setScheme('dark_muted_pastels');  // ← Edit this line
}
```

**Available Schemes:**
- `default` - Classic 3Blue1Brown
- `dark_muted_pastels` - Modern soft pastels ⭐ CURRENT
- `deep_jewel_tones` - Sophisticated
- `contrasting_vibrancy` - Bold & vibrant
- `erau` - University branding
- `dark` - Contemporary dark
- `high_contrast` - Accessibility focused
- `warm_sunset` - Cozy orange/pink
- `cool_ocean` - Calm blue/teal
- `forest_earth` - Natural green/brown

**After editing:** Hard refresh browser (Ctrl+F5 / Cmd+Shift+R)

---

## 📁 File Structure

```
css/
  ├─ color-schemes.css ......... CSS variables for all schemes
  └─ styles.css ................. Main stylesheet (uses variables)

js/
  ├─ color-schemes.js ........... Color data for all schemes
  ├─ style-config.js ............ API for getting/setting schemes
  └─ global-scheme-config.js .... YOUR CONFIG FILE (edit this!)
```

---

## 🔧 API Reference

### JavaScript

```javascript
// Set scheme (use in global-scheme-config.js)
styleConfig.setScheme('cool_ocean');

// Get a color value
const highlightColor = styleConfig.getColor('highlight');  // Returns "#ABDADC"

// Get all colors from current scheme
const colors = styleConfig.getColors();

// Get current scheme name
const currentScheme = styleConfig.getCurrentScheme();  // Returns "dark_muted_pastels"

// Get list of available schemes
const schemes = styleConfig.getAvailableSchemes();  // Returns array

// Listen for scheme changes (for canvas redraws)
window.addEventListener('colorSchemeChanged', function(e) {
    console.log('Scheme changed to:', e.detail.scheme);
    redrawCanvas();
});
```

### CSS

```css
/* Use CSS variables in your stylesheets */
.my-element {
    color: var(--text);
    background: var(--background);
    border-color: var(--highlight);
}
```

**Available CSS Variables:**
- `--background` - Main background
- `--text` - Main text color
- `--text-background` - Secondary background
- `--highlight` - Primary highlight
- `--accent` - Secondary accent
- `--accent-primary` - Primary accent
- `--accent-secondary` - Secondary accent
- `--dot` - Dot/point color
- `--time` - Time-based color
- `--displacement` - Displacement color
- `--equation` - Equation color
- `--border-color` - Border color

---

## ✅ Checklist: Adding Color Scheme to New Page

### HTML (in `<head>`):
```html
<link rel="stylesheet" href="../css/color-schemes.css">
<link rel="stylesheet" href="../css/styles.css">
```

### HTML (before `</body>`):
```html
<script src="../js/color-schemes.js"></script>
<script src="../js/style-config.js"></script>
<script src="../js/global-scheme-config.js"></script>
</body>
```

### CSS:
- Use `var(--variable-name)` for colors
- Don't hardcode hex values

### JavaScript (for canvas):
- Use `styleConfig.getColor('highlight')` instead of `'#00d9ff'`
- Add listener: `window.addEventListener('colorSchemeChanged', redraw);`

---

## 🐛 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| Colors don't change | Hard refresh browser (Ctrl+F5) |
| Some elements wrong color | Check for inline `style="color:#..."` |
| Console error: "not defined" | Check script order and paths |
| Canvas doesn't update | Add `colorSchemeChanged` listener |
| Different colors per page | Check for page overrides after global-scheme-config.js |

**Full troubleshooting:** See `TROUBLESHOOTING.md`

---

## 📝 Common Tasks

### Task: Test a different scheme quickly
1. Edit `/js/global-scheme-config.js`
2. Change line 33 to different scheme
3. Save, hard refresh browser

### Task: Override scheme for one page
```html
<!-- After global-scheme-config.js in that page -->
<script src="../js/global-scheme-config.js"></script>
<script>
    styleConfig.setScheme('erau');  // This page only
</script>
```

### Task: Use scheme colors in canvas
```javascript
function draw() {
    ctx.fillStyle = styleConfig.getColor('background');
    ctx.strokeStyle = styleConfig.getColor('highlight');
    // ... drawing code
}

// Redraw when scheme changes
window.addEventListener('colorSchemeChanged', draw);
```

### Task: Create a new color scheme
1. Edit `/js/color-schemes.js` - Add new scheme object
2. Edit `/css/color-schemes.css` - Add new `[data-color-scheme='name']` section
3. Edit `/js/global-scheme-config.js` - Add comment line with new scheme name

---

## 📚 Full Documentation

- **Quick Start:** This file
- **Complete Guide:** `COLOR_SCHEME_GUIDE.md`
- **Troubleshooting:** `TROUBLESHOOTING.md`
- **Recent Fixes:** `BUG_FIXES.md`
- **Implementation:** `FINAL_IMPLEMENTATION.md`

---

## 💡 Pro Tips

1. **Always hard refresh** after editing config (Ctrl+F5 / Cmd+Shift+R)
2. **Check browser console** for errors (F12)
3. **Use CSS variables** in stylesheets, not hardcoded colors
4. **Use `styleConfig.getColor()`** in JavaScript, not hex codes
5. **Scripts go at end of `<body>`**, not in `<head>`
6. **Only uncomment ONE scheme** in global-scheme-config.js

---

**Current Active Scheme:** `dark_muted_pastels`  
**Last Updated:** January 2, 2026
