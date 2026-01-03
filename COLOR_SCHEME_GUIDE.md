# Color Scheme Configuration Guide

## Overview

This project now supports multiple color schemes that can be applied globally across all pages and walkthroughs. The color schemes are defined in the `New Styles` folder and integrated into the framework through CSS custom properties (CSS variables).

## Quick Start: Changing the Global Color Scheme

To change the color scheme for the entire site:

1. Open the file: `js/global-style-config.js`
2. Find the line that says:
   ```javascript
   const GLOBAL_COLOR_SCHEME = 'dark_muted_pastels';
   ```
3. Change `'dark_muted_pastels'` to any of the available color schemes (see list below)
4. Save the file
5. Refresh any open pages in your browser

That's it! All pages and walkthroughs will automatically use the new color scheme.

## Available Color Schemes

Choose from these 10 carefully crafted color schemes:

1. **`default`** - Classic black background with vibrant colors
   - Best for: Traditional educational math videos
   - Style: High contrast, clear visibility

2. **`dark_muted_pastels`** - Soft pastels on dark gray background *(Current default)*
   - Best for: Gentle, modern aesthetic
   - Style: Low contrast, easy on eyes

3. **`deep_jewel_tones`** - Rich, saturated colors on very dark background
   - Best for: Professional, sophisticated look
   - Style: Medium contrast, elegant

4. **`contrasting_vibrancy`** - Bright, bold colors with maximum energy
   - Best for: Attention-grabbing content
   - Style: Very high contrast, energetic

5. **`erau`** - ERAU university branding colors
   - Best for: ERAU-specific content
   - Style: University brand compliance

6. **`dark`** - Modern sophisticated dark theme
   - Best for: Contemporary presentations
   - Style: Balanced contrast

7. **`high_contrast`** - Maximum contrast for accessibility
   - Best for: Visibility in all conditions
   - Style: Stark, clear

8. **`warm_sunset`** - Warm oranges and browns
   - Best for: Organic, warm feeling
   - Style: Cozy, inviting

9. **`cool_ocean`** - Blues and cyans for oceanic feel
   - Best for: Calm, flowing content
   - Style: Cool, tranquil

10. **`forest_earth`** - Greens and earth tones
    - Best for: Natural, grounded aesthetic
    - Style: Organic, stable

## How It Works

### Architecture

The color scheme system is built on three components:

1. **`New Styles/color_schemes.css`** - Contains CSS custom properties for all color schemes
2. **`js/color-schemes.js`** - JavaScript constants for accessing colors programmatically
3. **`js/global-style-config.js`** - Global configuration that applies the selected scheme

### Color Variables

Each color scheme provides these semantic color variables:

- `--background` - Main background color
- `--text` - Primary text color
- `--text-background` - Background for text elements
- `--text-surrounding` - Text borders/surroundings
- `--highlight` - Emphasis color
- `--accent` - Secondary accent
- `--time` - Time-related elements
- `--displacement` - Position/movement
- `--dot` - Points and markers
- `--contrast-1` - First contrasting color
- `--contrast-2` - Second contrasting color

### CSS Usage

All styles in `css/styles.css` now use these CSS variables instead of hardcoded colors:

```css
body {
    background: var(--background);
    color: var(--text);
}

h1 {
    color: var(--highlight);
}

.section {
    background: var(--text-background);
    border-bottom: 2px solid var(--text-surrounding);
}
```

This means when you change the `GLOBAL_COLOR_SCHEME`, all these elements automatically adapt to the new colors.

### JavaScript Usage

If you need to access colors in JavaScript (for canvas drawing, etc.):

```javascript
// Get a color from the active scheme
const highlightColor = getSchemeColor('highlight');

// Get the active scheme name
const currentScheme = getActiveColorScheme();

// Access the COLOR_SCHEMES object directly
const allSchemes = COLOR_SCHEMES;
const specificScheme = COLOR_SCHEMES['dark_muted_pastels'];
```

## Testing Different Schemes

To preview different schemes quickly:

1. Keep a browser window open with your page
2. Edit `js/global-style-config.js` and change the `GLOBAL_COLOR_SCHEME` value
3. Save the file
4. Refresh the browser
5. Repeat to try different schemes

## What's Covered

The global color scheme currently applies to:

- ✅ Main index page (`index.html`)
- ✅ All walkthrough pages in the `pages/` folder
- ✅ Quiz components and feedback
- ✅ Sections, headers, and text
- ✅ Buttons, inputs, and controls
- ✅ Code blocks and hints
- ⚠️ **Applets are NOT affected** (as requested - applets maintain their own styling)

## Future Enhancements

Potential improvements for later:

- Add a UI toggle to switch schemes without editing code
- Create custom schemes for specific topics
- Apply schemes to applets (when desired)
- Add animation timing function support (already available in New Styles)

## Troubleshooting

**Problem: Colors don't change after updating the config**
- Solution: Make sure you saved `js/global-style-config.js` and did a hard refresh (Ctrl+Shift+R or Cmd+Shift+R)

**Problem: Some elements still show old colors**
- Solution: Check if those elements are in an applet (which maintains separate styling) or if they use inline styles

**Problem: JavaScript errors in console**
- Solution: Ensure `js/color-schemes.js` is loaded before `js/global-style-config.js` in your HTML

## Additional Resources

For more information about the color schemes and their design:

- See `New Styles/UNIFIED_STYLE_README.md` - Complete style library documentation
- See `New Styles/STYLE_GUIDE.md` - Detailed color scheme descriptions
- See `New Styles/QUICK_START.md` - Quick reference for the style system

---

**Last Updated:** January 2026  
**Author:** Zackery Reed
