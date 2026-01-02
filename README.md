# Math Intuitions Applets

This repository contains interactive HTML5/JavaScript applets and walkthroughs for visualizing key mathematical concepts, designed for discovery-based learning. Each applet is paired with a conceptual walkthrough page featuring guided questions, interactive quizzes, and embedded symbolic computation.

## 🎨 NEW: Color Scheme System

The repository now features a **unified color scheme system** that provides:
- **10 professional color schemes** (from classic 3Blue1Brown to modern pastels)
- **Dynamic scheme switching** with persistent user preferences
- **Centralized color management** across all applets and pages
- **Flexible configuration** - set globally or per-applet

**Quick Start:**
- See `COLOR_SCHEME_QUICK_REF.md` for quick reference
- See `COLOR_SCHEME_INTEGRATION.md` for complete documentation
- See `FILE_STRUCTURE_GUIDE.md` for file structure and migration guide

**Try it now:** Open `applets/geometric-series.html` and use the color scheme selector!

## Structure

- `index.html` — Main navigation page
- `applets/` — Standalone HTML visualizations (canvas-based)
- `pages/` — Walkthrough pages with quizzes and explorations
- `css/` — Shared stylesheets
  - `color-schemes.css` — Color scheme CSS variables ⭐
  - `applet-styles.css` — Base applet styles (uses color schemes)
  - `styles.css` — Page styles (uses color schemes)
- `js/` — Shared JavaScript utilities
  - `color-schemes.js` — Color scheme data ⭐
  - `style-config.js` — Central color management system ⭐
  - `global-scheme-config.js` — Optional global configuration ⭐
  - `canvas-utils.js`, `quiz.js`, `utils.js` — Existing utilities
- `New Styles/` — Original Python source for color schemes and animations

## Applets & Walkthroughs
- Chain Rule Visualization
- Circle Series Visualization
- Geometric Series Visualization ✅ (updated with color schemes)
- Local Linearity Explorer
- Population Density Visualization
- Tortoise-Hare Race
- Vector Projection

## Features
- **Unified color scheme system** with 10 professional themes ⭐
- Dynamic scheme switching with localStorage persistence ⭐
- Consistent theming via CSS variables
- Efficient, modular JavaScript for canvas interactions
- Discovery-based questions and quizzes
- Embedded SageMath/SymPy cells for symbolic computation
- KaTeX for math rendering

## Documentation

### Color Scheme System
- `COLOR_SCHEME_QUICK_REF.md` — Quick reference and common patterns
- `COLOR_SCHEME_INTEGRATION.md` — Complete guide with API reference
- `FILE_STRUCTURE_GUIDE.md` — File structure and migration guide
- `IMPLEMENTATION_SUMMARY.md` — System overview and implementation details

### New Styles (Source)
- `New Styles/UNIFIED_STYLE_README.md` — Original documentation
- `New Styles/QUICK_START.md` — Quick start for Python source
- `New Styles/STYLE_GUIDE.md` — Detailed style guide

## License
See LICENSE file for copyright and usage information.

---

© 2025 Zackery Reed. All rights reserved.

