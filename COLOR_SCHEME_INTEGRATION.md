# Color Scheme Integration Guide

This guide explains how to use the unified color scheme system across all applets and pages in the Math Intuitions Applets repository.

## 📋 Overview

The color scheme system provides:
- **10 predefined color schemes** (from the New Styles folder)
- **Centralized color management** via JavaScript and CSS
- **Easy scheme switching** at the global or per-element level
- **Persistent preferences** stored in localStorage
- **Consistent styling** across all applets and pages

## 🎨 Available Color Schemes

1. **default** - Classic 3Blue1Brown style (black background, vibrant colors)
2. **dark_muted_pastels** - Soft pastels on dark gray (modern, easy on eyes)
3. **deep_jewel_tones** - Rich, saturated colors (professional, sophisticated)
4. **contrasting_vibrancy** - Bright, bold colors (maximum energy)
5. **erau** - ERAU university branding
6. **dark** - Contemporary dark theme
7. **high_contrast** - Maximum accessibility
8. **warm_sunset** - Warm oranges and browns (cozy, inviting)
9. **cool_ocean** - Blues and cyans (calm, flowing)
10. **forest_earth** - Greens and earth tones (natural, grounded)

Each scheme provides semantic color keys:
- `background` - Main background color
- `text` - Primary text color
- `text_background` - Background for text elements
- `text_surrounding` - Borders/surroundings for text
- `highlight` - Emphasis color
- `accent` - Secondary accent
- `time` - Time-related elements
- `displacement` - Position/movement
- `dot` - Points and markers
- `contrast_1`, `contrast_2` - Additional contrasting colors

## 🚀 Quick Start

### For HTML Pages

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Page</title>
    <!-- Include color schemes CSS -->
    <link rel="stylesheet" href="../css/color-schemes.css">
    <!-- Include your main styles -->
    <link rel="stylesheet" href="../css/styles.css">
    <!-- Include JavaScript files -->
    <script src="../js/color-schemes.js"></script>
    <script src="../js/style-config.js"></script>
</head>
<body>
    <!-- Your content here -->
    
    <script>
        // Optionally set a specific scheme
        styleConfig.setGlobalScheme('dark_muted_pastels');
        
        // Or add a scheme selector UI
        document.addEventListener('DOMContentLoaded', () => {
            const selector = styleConfig.createSchemeSelector({
                label: '🎨 Color Scheme:'
            });
            document.body.appendChild(selector);
        });
    </script>
</body>
</html>
```

### For Applets (Standalone HTML)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Applet</title>
    <link rel="stylesheet" href="../css/color-schemes.css">
    <link rel="stylesheet" href="../css/applet-styles.css">
</head>
<body>
    <canvas id="myCanvas"></canvas>
    
    <script src="../js/color-schemes.js"></script>
    <script src="../js/style-config.js"></script>
    <script>
        const canvas = document.getElementById('myCanvas');
        const ctx = canvas.getContext('2d');
        
        function draw() {
            // Get colors from current scheme
            const bgColor = styleConfig.getColor('background');
            const highlightColor = styleConfig.getColor('highlight');
            const textColor = styleConfig.getColor('text');
            
            // Use colors in your drawing code
            ctx.fillStyle = bgColor;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.strokeStyle = highlightColor;
            ctx.fillStyle = textColor;
            // ... your drawing code
        }
        
        // Redraw when scheme changes
        window.addEventListener('colorSchemeChanged', draw);
        
        draw();
    </script>
</body>
</html>
```

## 📚 API Reference

### JavaScript API (`styleConfig` object)

#### `styleConfig.setGlobalScheme(schemeName, persist = true)`
Sets the global color scheme for the entire page.
```javascript
styleConfig.setGlobalScheme('cool_ocean'); // Sets and saves to localStorage
styleConfig.setGlobalScheme('erau', false); // Sets without saving
```

#### `styleConfig.getColor(colorKey, schemeName = null)`
Gets a color value from the current (or specified) scheme.
```javascript
const highlight = styleConfig.getColor('highlight'); // From current scheme
const bg = styleConfig.getColor('background', 'dark'); // From specific scheme
```

#### `styleConfig.getColors(schemeName = null)`
Gets all colors from a scheme.
```javascript
const colors = styleConfig.getColors(); // All colors from current scheme
const erauColors = styleConfig.getColors('erau'); // All colors from ERAU scheme
```

#### `styleConfig.getCurrentScheme()`
Returns the name of the currently active scheme.
```javascript
const current = styleConfig.getCurrentScheme(); // e.g., 'dark_muted_pastels'
```

#### `styleConfig.getAvailableSchemes()`
Returns an array of all available scheme names.
```javascript
const schemes = styleConfig.getAvailableSchemes();
// ['default', 'dark_muted_pastels', 'deep_jewel_tones', ...]
```

#### `styleConfig.createSchemeSelector(options)`
Creates a pre-styled dropdown UI for scheme selection.
```javascript
const selector = styleConfig.createSchemeSelector({
    id: 'my-selector',
    label: '🎨 Choose Color Scheme:',
    containerClass: 'my-custom-class'
});
document.body.appendChild(selector);
```

#### `styleConfig.hexToRGB(hex)`
Converts hex color to RGB array (0-255).
```javascript
const rgb = styleConfig.hexToRGB('#FF6B6B'); // [255, 107, 107]
```

#### `styleConfig.hexToRGBNormalized(hex)`
Converts hex color to normalized RGB array (0-1, for canvas).
```javascript
const rgb = styleConfig.hexToRGBNormalized('#FF6B6B'); // [1.0, 0.42, 0.42]
```

### CSS Variables

Each scheme defines CSS custom properties that can be used in your stylesheets:

```css
/* These are automatically set based on the active scheme */
:root {
    --background: #1a1a2e;
    --text: #e8e8e8;
    --text-background: #16213e;
    --highlight: #00d9ff;
    --accent: #77e4c8;
    /* ... and all other color keys */
}

/* Use them in your styles */
.my-element {
    background: var(--background);
    color: var(--text);
    border-color: var(--highlight);
}
```

### Events

#### `colorSchemeChanged` Event
Fired when the color scheme changes globally.
```javascript
window.addEventListener('colorSchemeChanged', (event) => {
    console.log('New scheme:', event.detail.scheme);
    // Redraw canvas, update UI, etc.
});
```

## 🎯 Best Practices

### 1. Use Semantic Color Names
Instead of hardcoding colors, use the semantic names:
```javascript
// ❌ Bad
ctx.fillStyle = '#FF0000';

// ✅ Good
ctx.fillStyle = styleConfig.getColor('highlight');
```

### 2. Listen for Scheme Changes
For dynamic content (canvas, SVG), redraw when the scheme changes:
```javascript
window.addEventListener('colorSchemeChanged', () => {
    redrawCanvas();
});
```

### 3. Provide Color Scheme Selector
Give users control over their visual experience:
```javascript
// Add to pages
const selector = styleConfig.createSchemeSelector({
    label: '🎨 Color Scheme:'
});
document.querySelector('#controls').appendChild(selector);
```

### 4. Use CSS Variables in Stylesheets
Let CSS automatically update with scheme changes:
```css
body {
    background: var(--background);
    color: var(--text);
}

button {
    background: var(--highlight);
    color: var(--text);
}
```

### 5. Override Specific Elements
You can override the scheme for specific elements:
```javascript
const specialDiv = document.getElementById('special');
styleConfig.setScheme(specialDiv, 'erau');
```

## 📝 Migration Guide

### Migrating Existing Applets

1. **Add CSS/JS includes** to your HTML:
   ```html
   <link rel="stylesheet" href="../css/color-schemes.css">
   <script src="../js/color-schemes.js"></script>
   <script src="../js/style-config.js"></script>
   ```

2. **Replace hardcoded colors** in JavaScript:
   ```javascript
   // Before
   const bgColor = '#1a1a2e';
   const textColor = '#eee';
   
   // After
   const bgColor = styleConfig.getColor('background');
   const textColor = styleConfig.getColor('text');
   ```

3. **Update CSS** to use variables:
   ```css
   /* Before */
   body {
       background: #1a1a2e;
       color: #eee;
   }
   
   /* After */
   body {
       background: var(--background);
       color: var(--text);
   }
   ```

4. **Add redraw listener** for canvas applets:
   ```javascript
   window.addEventListener('colorSchemeChanged', () => {
       draw(); // Your draw function
   });
   ```

### Migrating Walkthrough Pages

1. **Update HTML head** with new includes
2. **Add scheme selector** (optional but recommended):
   ```javascript
   document.addEventListener('DOMContentLoaded', () => {
       const wrapper = document.getElementById('scheme-selector-wrapper');
       const selector = styleConfig.createSchemeSelector({
           label: '🎨 Color Scheme:'
       });
       wrapper.appendChild(selector);
   });
   ```

## 🎨 Customizing Color Schemes

### Setting a Default Scheme for Your Project

Edit `/js/style-config.js` and change the default:
```javascript
this.DEFAULT_SCHEME = 'dark_muted_pastels'; // Change this line
```

### Per-Page Overrides

Set a specific scheme in your page's script:
```javascript
// This page always uses ERAU colors
styleConfig.setGlobalScheme('erau', false);
```

### Creating New Color Schemes

To add new schemes:

1. Edit `/js/color-schemes.js` and add your scheme to `COLOR_SCHEMES`:
   ```javascript
   my_custom_scheme: {
       text_background: '#...',
       text: '#...',
       background: '#...',
       highlight: '#...',
       // ... all required keys
   }
   ```

2. Edit `/css/color-schemes.css` and add CSS variables:
   ```css
   [data-color-scheme='my_custom_scheme'] {
       --text-background: #...;
       --text: #...;
       /* ... */
   }
   ```

Or regenerate from Python using the scripts in `New Styles/`.

## 🐛 Troubleshooting

### Colors Not Updating
- Check that you've included both `color-schemes.css` and `color-schemes.js`
- Verify that `style-config.js` is loaded after `color-schemes.js`
- Make sure you're using CSS variables or JavaScript API, not hardcoded colors

### Scheme Selector Not Appearing
- Ensure `styleConfig` is defined (check console for errors)
- Verify the selector is being appended to an existing element
- Check that scripts are loaded after the DOM is ready

### Canvas Not Redrawing
- Add a listener for `colorSchemeChanged` event
- Call your draw function when the event fires

## 📂 File Structure

```
math_intuitions_applets/
├── css/
│   ├── color-schemes.css      # CSS variables for all schemes
│   ├── applet-styles.css      # Base applet styles (uses variables)
│   └── styles.css             # Page styles (uses variables)
├── js/
│   ├── color-schemes.js       # Color scheme data
│   └── style-config.js        # Central configuration system
├── New Styles/                # Original Python source files
│   ├── color_schemes.css
│   ├── color_schemes.js
│   └── ...
└── applets/
    └── *.html                 # Your applets
```

## 🔗 Related Resources

- **New Styles/UNIFIED_STYLE_README.md** - Original documentation
- **New Styles/QUICK_START.md** - Quick reference
- **New Styles/STYLE_GUIDE.md** - Detailed style guide

## 💡 Example: Complete Applet Integration

See `applets/geometric-series.html` for a complete working example of:
- Including all necessary files
- Using colors dynamically in canvas drawing
- Adding a scheme selector
- Listening for scheme changes
- Redrawing on scheme change

See `pages/geometric-series-walkthrough.html` for a complete page example.

---

**Questions?** Check the examples or examine the implementation in `js/style-config.js`.
