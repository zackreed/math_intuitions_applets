# Color Scheme System - Quick Reference

## 🎯 What Was Created

A complete color scheme integration system that allows you to:
1. **Select from 10 predefined color schemes** (from New Styles folder)
2. **Apply schemes globally** across all pages and applets
3. **Switch schemes dynamically** with UI controls
4. **Persist user preferences** in localStorage
5. **Override schemes per-element** when needed

## 📁 New Files Created

1. **`/js/color-schemes.js`** - Color scheme data (JavaScript)
2. **`/js/style-config.js`** - Central configuration system
3. **`/css/color-schemes.css`** - CSS variables for all schemes
4. **`/COLOR_SCHEME_INTEGRATION.md`** - Complete documentation

## 📝 Files Updated

1. **`/css/applet-styles.css`** - Now uses CSS variables from color schemes
2. **`/css/styles.css`** - Updated to use color scheme variables
3. **`/applets/geometric-series.html`** - Example applet integration
4. **`/pages/geometric-series-walkthrough.html`** - Example page integration

## 🚀 Quick Usage

### For a New Applet

```html
<head>
    <link rel="stylesheet" href="../css/color-schemes.css">
    <link rel="stylesheet" href="../css/applet-styles.css">
</head>
<body>
    <canvas id="canvas"></canvas>
    
    <script src="../js/color-schemes.js"></script>
    <script src="../js/style-config.js"></script>
    <script>
        // Use colors
        const bgColor = styleConfig.getColor('background');
        const highlightColor = styleConfig.getColor('highlight');
        
        // Redraw when scheme changes
        window.addEventListener('colorSchemeChanged', () => {
            draw();
        });
    </script>
</body>
```

### For a New Page

```html
<head>
    <link rel="stylesheet" href="../css/color-schemes.css">
    <link rel="stylesheet" href="../css/styles.css">
    <script src="../js/color-schemes.js"></script>
    <script src="../js/style-config.js"></script>
</head>
<body>
    <script>
        // Add scheme selector
        const selector = styleConfig.createSchemeSelector({
            label: '🎨 Color Scheme:'
        });
        document.body.appendChild(selector);
    </script>
</body>
```

## 🎨 Available Color Schemes

1. `default` - Classic 3Blue1Brown
2. `dark_muted_pastels` - Modern, soft
3. `deep_jewel_tones` - Sophisticated
4. `contrasting_vibrancy` - High energy
5. `erau` - University branding
6. `dark` - Contemporary
7. `high_contrast` - Accessibility
8. `warm_sunset` - Cozy
9. `cool_ocean` - Calm
10. `forest_earth` - Natural

## 🔧 Key Functions

```javascript
// Set global scheme
styleConfig.setGlobalScheme('dark_muted_pastels');

// Get a color
const color = styleConfig.getColor('highlight');

// Get all colors
const colors = styleConfig.getColors();

// Create UI selector
const selector = styleConfig.createSchemeSelector();
```

## 📌 CSS Variables

All schemes provide these CSS custom properties:
- `--background`
- `--text`
- `--text-background`
- `--highlight`
- `--accent`
- `--time`
- `--displacement`
- `--dot`
- `--contrast-1`
- `--contrast-2`

Use in CSS:
```css
body {
    background: var(--background);
    color: var(--text);
}
```

## ✅ Next Steps

1. **Test the system** - Open `geometric-series.html` or `geometric-series-walkthrough.html`
2. **Migrate other applets** - Follow patterns in updated files
3. **Customize** - Set default scheme or add new schemes
4. **Read full docs** - See `COLOR_SCHEME_INTEGRATION.md` for complete guide

## 🎯 Where to Apply

### Top Level (Global)
Set once in a configuration file or index page:
```javascript
styleConfig.setGlobalScheme('dark_muted_pastels');
```

### Per-Page Override
In specific page's script:
```javascript
styleConfig.setGlobalScheme('erau', false); // Don't persist
```

### Per-Applet
Each applet can use the global scheme or override:
```javascript
styleConfig.setScheme(document.body, 'cool_ocean');
```

### User Control
Add a selector for users to choose:
```javascript
const selector = styleConfig.createSchemeSelector();
document.getElementById('controls').appendChild(selector);
```

## 🔍 Examples

**Working Examples:**
- `applets/geometric-series.html` - Full applet integration with canvas
- `pages/geometric-series-walkthrough.html` - Full page integration

**Key Features Demonstrated:**
- ✅ Dynamic color loading from schemes
- ✅ Canvas redrawing on scheme change
- ✅ UI scheme selector
- ✅ localStorage persistence
- ✅ CSS variable integration

---

For complete documentation, see **COLOR_SCHEME_INTEGRATION.md**
