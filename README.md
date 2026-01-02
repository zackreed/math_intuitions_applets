# Math Intuitions Applets

This repository contains interactive HTML5/JavaScript applets and walkthroughs for visualizing key mathematical concepts, designed for discovery-based learning. Each applet is paired with a conceptual walkthrough page featuring guided questions, interactive quizzes, and embedded symbolic computation.

## 🎨 Color Scheme System

The repository features a **unified color scheme system** for consistent styling:
- **10 professional color schemes** (from classic 3Blue1Brown to modern pastels)
- **Developer-controlled** - set once in code, applies everywhere
- **No user-facing controls** - users see your chosen theme
- **Easy to change** - edit one line to switch the entire site's colors

**To change the color scheme:** Edit `/js/global-scheme-config.js` and uncomment your preferred scheme.

**Documentation:** See `COLOR_SCHEME_GUIDE.md` for complete instructions.

## Structure

- `index.html` — Main navigation page
- `applets/` — Standalone HTML visualizations (canvas-based)
- `pages/` — Walkthrough pages with quizzes and explorations
- `css/` — Shared stylesheets
  - `color-schemes.css` — Color scheme CSS variables
  - `applet-styles.css` — Base applet styles
  - `styles.css` — Page styles
- `js/` — Shared JavaScript utilities
  - `color-schemes.js` — Color scheme data
  - `style-config.js` — Color management API
  - `global-scheme-config.js` — Default scheme configuration ⚙️
  - `canvas-utils.js`, `quiz.js`, `utils.js` — Utilities
- `New Styles/` — Original Python source for color schemes

## Applets & Walkthroughs
- Chain Rule Visualization
- Circle Series Visualization
- Geometric Series Visualization
- Local Linearity Explorer
- Population Density Visualization
- Tortoise-Hare Race
- Vector Projection

## Features
- **Unified color scheme system** with 10 professional themes
- Consistent theming via CSS variables
- Efficient, modular JavaScript for canvas interactions
- Discovery-based questions and quizzes
- Embedded SageMath/SymPy cells for symbolic computation
- KaTeX for math rendering

## Documentation

### Color Scheme System
- `COLOR_SCHEME_GUIDE.md` — **START HERE** - Complete guide for using color schemes
- `New Styles/UNIFIED_STYLE_README.md` — Original documentation for Python source

### Legacy Documentation (for reference)
- `COLOR_SCHEME_QUICK_REF.md`
- `COLOR_SCHEME_INTEGRATION.md`
- `FILE_STRUCTURE_GUIDE.md`
- `IMPLEMENTATION_SUMMARY.md`

## License
See LICENSE file for copyright and usage information.

---

© 2025 Zackery Reed. All rights reserved.

