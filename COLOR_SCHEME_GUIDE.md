# Color Scheme System - Developer Guide

## 🎨 Overview

This repository uses a unified color scheme system that allows you to **set colors once in code** and have them apply across all applets and pages. This is a **developer tool only** - users don't see any color scheme options.

## ✅ What's Been Done

All applets and pages have been migrated to use the color scheme system. The infrastructure is in place and working.

## 🚀 How to Use

### Quick Start: Change the Global Color Scheme

**Edit `/js/global-scheme-config.js`** and uncomment your preferred scheme inside the `applyGlobalScheme()` function:

```javascript
function applyGlobalScheme() {
    // Uncomment ONE line:
    
    // styleConfig.setScheme('default');                  // Classic 3Blue1Brown style
    styleConfig.setScheme('dark_muted_pastels');       // Modern soft pastels (ACTIVE)
    // styleConfig.setScheme('deep_jewel_tones');         // Sophisticated elegance
    // styleConfig.setScheme('contrasting_vibrancy');     // High energy, bold
    // styleConfig.setScheme('erau');                     // ERAU university branding
    // styleConfig.setScheme('dark');                     // Contemporary dark theme
    // styleConfig.setScheme('high_contrast');            // Maximum accessibility
    // styleConfig.setScheme('warm_sunset');              // Cozy, inviting
    // styleConfig.setScheme('cool_ocean');               // Calm, professional
    // styleConfig.setScheme('forest_earth');             // Natural, grounded
}
```

That's it! Refresh your browser (Ctrl+F5 or Cmd+Shift+R) and all pages and applets will use that scheme.

### Override for a Specific Page

In that page's HTML, add after the global-scheme-config.js script:

```html
<script src="../js/global-scheme-config.js"></script>
<script>
    // Override just for this page
    styleConfig.setScheme('erau');
</script>
```

### Override for a Specific Applet

Same approach - add a script tag with `styleConfig.setScheme('scheme_name');`

## 📋 Available Color Schemes

1. **default** - Classic black background with vibrant colors (3Blue1Brown style)
2. **dark_muted_pastels** ⭐ - Soft pastels on dark gray (recommended default)
3. **deep_jewel_tones** - Rich, saturated jewel colors
4. **contrasting_vibrancy** - Bright, bold, maximum energy
5. **erau** - ERAU university branding colors
6. **dark** - Modern sophisticated dark theme
7. **high_contrast** - Maximum contrast for accessibility
8. **warm_sunset** - Warm oranges and browns
9. **cool_ocean** - Blues and cyans
10. **forest_earth** - Greens and earth tones

Each scheme provides these semantic colors:
- `background`, `text`, `text_background`, `text_surrounding`
- `highlight`, `accent`, `time`, `displacement`, `dot`
- `contrast_1`, `contrast_2`

## 🎯 Common Tasks

### Change Theme for Everything
1. Edit `/js/global-scheme-config.js`
2. Uncomment your preferred scheme
3. Done!

### Use Different Schemes for Different Sections
Edit `/js/global-scheme-config.js` and uncomment the advanced section:

```javascript
(function() {
    const path = window.location.pathname;
    
    if (path.includes('/applets/')) {
        styleConfig.setScheme('dark_muted_pastels');
    } else if (path.includes('/pages/')) {
        styleConfig.setScheme('default');
    } else if (path.includes('index.html')) {
        styleConfig.setScheme('cool_ocean');
    }
})();
```

### Get Colors in JavaScript (for Canvas Drawing)

In your applet code:

```javascript
function draw() {
    // Get colors from current scheme
    const bgColor = styleConfig.getColor('background');
    const highlightColor = styleConfig.getColor('highlight');
    const textColor = styleConfig.getColor('text');
    
    // Use them
    ctx.fillStyle = bgColor;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = highlightColor;
    // ... etc
}

// Redraw when scheme changes
window.addEventListener('colorSchemeChanged', () => {
    draw();
});
```

### Use Colors in CSS (Automatic)

CSS variables are automatically set based on the active scheme:

```css
.my-element {
    background: var(--background);
    color: var(--text);
    border-color: var(--highlight);
}
```

Most of your CSS will already work because the shared stylesheets use these variables.

## 📂 Files You Might Edit

- **`/js/global-scheme-config.js`** - Set the default scheme here (most common)
- **Individual page/applet HTML** - Override scheme for specific pages
- **`/js/style-config.js`** - Core system (rarely need to edit)
- **`/css/color-schemes.css`** - CSS variables for all schemes (rarely need to edit)

## 🔧 Technical Details

### How It Works

1. `color-schemes.css` defines CSS custom properties for each scheme
2. `color-schemes.js` provides the color data in JavaScript
3. `style-config.js` is the API that sets the `data-color-scheme` attribute on `<html>`
4. `global-scheme-config.js` calls `styleConfig.setScheme()` to set the default
5. CSS automatically picks up colors via `var(--color-name)`
6. JavaScript can get colors via `styleConfig.getColor('color-name')`

### API Reference

```javascript
// Set global scheme
styleConfig.setScheme('dark_muted_pastels');

// Get a color
const color = styleConfig.getColor('highlight');  // Returns hex string like '#ABDADC'

// Get all colors
const colors = styleConfig.getColors();  // Returns object with all colors

// Get current scheme name
const current = styleConfig.getCurrentScheme();  // e.g., 'dark_muted_pastels'

// Get available schemes
const schemes = styleConfig.getAvailableSchemes();  // Array of scheme names

// Color conversion helpers
const rgb = styleConfig.hexToRGB('#FF6B6B');  // [255, 107, 107]
const normalized = styleConfig.hexToRGBNormalized('#FF6B6B');  // [1.0, 0.42, 0.42]
```

## 📝 Example: Creating a New Applet

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My New Applet</title>
    <link rel="stylesheet" href="../css/color-schemes.css">
    <link rel="stylesheet" href="../css/applet-styles.css">
</head>
<body>
    <canvas id="canvas" width="800" height="600"></canvas>
    
    <script src="../js/color-schemes.js"></script>
    <script src="../js/style-config.js"></script>
    <script src="../js/global-scheme-config.js"></script>
    
    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        
        function draw() {
            // Use color scheme
            ctx.fillStyle = styleConfig.getColor('background');
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.strokeStyle = styleConfig.getColor('highlight');
            ctx.fillStyle = styleConfig.getColor('text');
            // ... your drawing code
        }
        
        // Redraw on scheme change
        window.addEventListener('colorSchemeChanged', draw);
        
        draw();
    </script>
</body>
</html>
```

## 🎨 Customizing Colors

### Adding a New Scheme

1. Edit `/js/color-schemes.js` and add your scheme to the `COLOR_SCHEMES` object
2. Edit `/css/color-schemes.css` and add a new `[data-color-scheme='your_scheme']` section
3. Use it: `styleConfig.setScheme('your_scheme');`

### Tweaking an Existing Scheme

Edit the color values in `/js/color-schemes.js` and `/css/color-schemes.css`

## 💡 Tips

- **Start simple**: Just edit `global-scheme-config.js` to change the scheme
- **Test different schemes**: Try them all to see what looks best
- **Use semantic names**: Instead of hardcoding `'#FF0000'`, use `styleConfig.getColor('highlight')`
- **Canvas redraws**: Remember to add the `colorSchemeChanged` event listener
- **Check examples**: See `applets/geometric-series.html` for a complete working example

## 🐛 Troubleshooting

**Colors not showing?**
- Check that all three scripts are included (color-schemes.js, style-config.js, global-scheme-config.js)
- Make sure they're in the correct order
- Check browser console for errors

**Scheme not changing?**
- Make sure you uncommented only ONE scheme in global-scheme-config.js
- Hard refresh the page (Ctrl+F5 or Cmd+Shift+R)
- Check that the scheme name is spelled correctly

**Canvas not updating?**
- Did you add the `colorSchemeChanged` event listener?
- Is your draw function using `styleConfig.getColor()` instead of hardcoded colors?

---

**That's it!** Edit one line in `global-scheme-config.js` to change your entire site's color scheme.
