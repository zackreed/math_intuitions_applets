# Color Scheme System - File Structure & Flow

```
math_intuitions_applets/
│
├── 📁 New Styles/                    # Original source (Python)
│   ├── unified_color_schemes.py      # Python source
│   ├── color_schemes.css             # Generated CSS
│   ├── color_schemes.js              # Generated JS
│   ├── UNIFIED_STYLE_README.md       # Original docs
│   ├── QUICK_START.md
│   └── STYLE_GUIDE.md
│
├── 📁 css/                            # ✅ INTEGRATION FILES
│   ├── color-schemes.css             # ⭐ All color schemes (CSS variables)
│   ├── applet-styles.css             # ✅ Updated to use variables
│   └── styles.css                    # ✅ Updated to use variables
│
├── 📁 js/                             # ✅ INTEGRATION FILES  
│   ├── color-schemes.js              # ⭐ Color scheme data
│   ├── style-config.js               # ⭐ Central API & management
│   ├── global-scheme-config.js       # ⭐ Optional global config
│   ├── utils.js                      # Existing utilities
│   └── quiz.js                       # Existing quiz system
│
├── 📁 applets/                        # Your interactive applets
│   ├── geometric-series.html         # ✅ UPDATED - Example integration
│   ├── circle-series-viz.html        # TODO: Needs integration
│   ├── differential-viz-dynamic.html # TODO: Needs integration
│   ├── local-linearity-explorer.html # TODO: Needs integration
│   └── ... (other applets)           # TODO: Needs integration
│
├── 📁 pages/                          # Your walkthrough pages
│   ├── geometric-series-walkthrough.html  # ✅ UPDATED - Example
│   ├── circle-series-walkthrough.html     # TODO: Needs integration
│   ├── differential-walkthrough.html      # TODO: Needs integration
│   └── ... (other pages)                  # TODO: Needs integration
│
├── 📄 index.html                      # Main landing page
│   └── TODO: Add color scheme selector here
│
└── 📚 DOCUMENTATION                    # ✅ NEW DOCUMENTATION
    ├── COLOR_SCHEME_INTEGRATION.md    # ⭐ Complete guide (450+ lines)
    ├── COLOR_SCHEME_QUICK_REF.md      # ⭐ Quick reference
    └── IMPLEMENTATION_SUMMARY.md      # ⭐ This summary
```

## 🔄 Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│  New Styles Folder (Python Source)                          │
│  ├── unified_color_schemes.py                               │
│  └── Generates → color_schemes.css & color_schemes.js       │
└─────────────────────────────────────────────────────────────┘
                            │
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  Integration Files (Copied & Adapted)                       │
│  ├── css/color-schemes.css    (CSS custom properties)       │
│  └── js/color-schemes.js      (JavaScript data)             │
└─────────────────────────────────────────────────────────────┘
                            │
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  Style Configuration System                                  │
│  └── js/style-config.js    (API & Management)               │
│      ├── Load saved scheme from localStorage                │
│      ├── Apply data-color-scheme attribute to <html>        │
│      ├── Provide JavaScript API                             │
│      └── Emit 'colorSchemeChanged' events                   │
└─────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┴───────────────┐
            ↓                               ↓
┌─────────────────────────┐   ┌─────────────────────────┐
│  CSS (Automatic)        │   │  JavaScript (Manual)    │
│  ├── Reads CSS vars     │   │  ├── styleConfig API    │
│  ├── Updates colors     │   │  ├── Get colors         │
│  └── No code changes!   │   │  └── Redraw on change   │
└─────────────────────────┘   └─────────────────────────┘
            │                               │
            ↓                               ↓
┌─────────────────────────┐   ┌─────────────────────────┐
│  Pages (HTML/CSS)       │   │  Applets (Canvas/JS)    │
│  ├── Inherit vars       │   │  ├── Use API            │
│  └── Auto-update        │   │  └── Redraw on events   │
└─────────────────────────┘   └─────────────────────────┘
```

## 🎨 Color Scheme Selection Flow

```
User Action                    System Response
─────────────────────────────────────────────────────────
                              
1. Page loads                 → Check localStorage
   │                          → Apply saved scheme
   │                          → Or use default
   ↓
   
2. User selects scheme        → styleConfig.setGlobalScheme()
   (via dropdown)             │
   │                          ↓
   │                          → Set data-color-scheme on <html>
   │                          → Save to localStorage
   │                          → Emit 'colorSchemeChanged' event
   │                          ↓
   ↓                          
                              → CSS automatically updates
3. Page reflects change       → Canvas redraws (if listening)
   instantly!                 → All colors change
```

## 🔌 Integration Points

### For HTML Pages (Walkthroughs)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- 1. Include color schemes CSS -->
    <link rel="stylesheet" href="../css/color-schemes.css">
    
    <!-- 2. Include your main styles -->
    <link rel="stylesheet" href="../css/styles.css">
    
    <!-- 3. Include JavaScript -->
    <script src="../js/color-schemes.js"></script>
    <script src="../js/style-config.js"></script>
</head>
<body>
    <!-- Your content uses CSS variables automatically! -->
    
    <script>
        // 4. Optional: Add scheme selector
        const selector = styleConfig.createSchemeSelector();
        document.body.appendChild(selector);
    </script>
</body>
</html>
```

### For Canvas Applets

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- 1. Include color schemes CSS -->
    <link rel="stylesheet" href="../css/color-schemes.css">
    <link rel="stylesheet" href="../css/applet-styles.css">
</head>
<body>
    <canvas id="canvas"></canvas>
    
    <!-- 2. Include JavaScript -->
    <script src="../js/color-schemes.js"></script>
    <script src="../js/style-config.js"></script>
    
    <script>
        // 3. Use colors in your draw function
        function draw() {
            const bg = styleConfig.getColor('background');
            const highlight = styleConfig.getColor('highlight');
            // ... use colors ...
        }
        
        // 4. Redraw when scheme changes
        window.addEventListener('colorSchemeChanged', draw);
        
        draw();
    </script>
</body>
</html>
```

## 📋 Migration Checklist

### Per Applet:
- [ ] Add CSS includes (`color-schemes.css`, `applet-styles.css`)
- [ ] Add JS includes (`color-schemes.js`, `style-config.js`)
- [ ] Replace hardcoded colors with `styleConfig.getColor()`
- [ ] Add `colorSchemeChanged` event listener
- [ ] Test with multiple schemes

### Per Page:
- [ ] Add CSS includes (`color-schemes.css`, `styles.css`)
- [ ] Add JS includes (`color-schemes.js`, `style-config.js`)
- [ ] Optionally add scheme selector UI
- [ ] Test that CSS updates automatically

### Global Setup (One Time):
- [ ] Choose default scheme in `global-scheme-config.js`
- [ ] Or add scheme selector to `index.html`
- [ ] Update README with color scheme info

## 🎯 Priority Order

1. **Done ✅**
   - Core system files created
   - Documentation written
   - Example applet updated (geometric-series.html)
   - Example page updated (geometric-series-walkthrough.html)

2. **Next: Index Page**
   - Add scheme selector to main index.html
   - Sets default for entire site

3. **Then: Other Applets**
   - Migrate using geometric-series.html as template
   - Each applet is independent

4. **Finally: Other Pages**
   - Migrate using geometric-series-walkthrough.html as template
   - Much easier than applets (mostly CSS)

## 💡 Pro Tips

1. **Start Simple**: Just include the files, colors work automatically via CSS
2. **Test Often**: Switch schemes frequently while developing
3. **Use Examples**: Copy patterns from geometric-series files
4. **Read Comments**: style-config.js is heavily documented
5. **Check Console**: Errors will appear if files are missing

## 🔗 Related Files

- **Core System**: `js/style-config.js` (265 lines, well-commented)
- **Color Data**: `js/color-schemes.js` (all 10 schemes)
- **CSS Variables**: `css/color-schemes.css` (one [data-color-scheme] per scheme)
- **Full Docs**: `COLOR_SCHEME_INTEGRATION.md` (complete API reference)
- **Quick Ref**: `COLOR_SCHEME_QUICK_REF.md` (common patterns)

---

**Ready to use!** Start by viewing the examples or begin migration following the patterns shown above.
