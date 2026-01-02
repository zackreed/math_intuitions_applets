/**
 * Style Configuration System
 * ===========================
 * 
 * Central management for color schemes across all applets and pages.
 * 
 * Usage:
 * ------
 * 1. Include this file after color-schemes.js in your HTML
 * 2. Set a global color scheme: StyleConfig.setGlobalScheme('dark_muted_pastels')
 * 3. Override for specific elements: StyleConfig.setScheme(element, 'erau')
 * 4. Get colors in JavaScript: StyleConfig.getColor('highlight')
 * 
 * Features:
 * ---------
 * - Global scheme selection (applies to entire page)
 * - Per-element scheme overrides
 * - Local storage persistence
 * - Easy color access in JavaScript
 * - Fallback to default scheme
 */

class StyleConfig {
    constructor() {
        this.DEFAULT_SCHEME = 'default';
        this.STORAGE_KEY = 'math_applets_color_scheme';
        this.currentScheme = this.DEFAULT_SCHEME;
        
        // Load saved scheme from localStorage
        this.loadSavedScheme();
    }
    
    /**
     * Get list of all available color schemes
     */
    getAvailableSchemes() {
        return Object.keys(COLOR_SCHEMES);
    }
    
    /**
     * Get the currently active global scheme name
     */
    getCurrentScheme() {
        return this.currentScheme;
    }
    
    /**
     * Set global color scheme for the entire page/applet
     * @param {string} schemeName - Name of the color scheme to apply
     * @param {boolean} persist - Whether to save to localStorage (default: true)
     */
    setGlobalScheme(schemeName, persist = true) {
        if (!COLOR_SCHEMES[schemeName]) {
            console.warn(`Color scheme '${schemeName}' not found. Using '${this.DEFAULT_SCHEME}'.`);
            schemeName = this.DEFAULT_SCHEME;
        }
        
        this.currentScheme = schemeName;
        
        // Apply to document root
        document.documentElement.setAttribute('data-color-scheme', schemeName);
        
        // Also apply to body for backward compatibility
        document.body.setAttribute('data-color-scheme', schemeName);
        
        // Save to localStorage if requested
        if (persist) {
            this.saveScheme(schemeName);
        }
        
        // Dispatch custom event for listeners
        window.dispatchEvent(new CustomEvent('colorSchemeChanged', {
            detail: { scheme: schemeName }
        }));
        
        console.log(`Color scheme set to: ${schemeName}`);
    }
    
    /**
     * Set color scheme for a specific element
     * @param {HTMLElement} element - The element to apply the scheme to
     * @param {string} schemeName - Name of the color scheme
     */
    setScheme(element, schemeName) {
        if (!COLOR_SCHEMES[schemeName]) {
            console.warn(`Color scheme '${schemeName}' not found.`);
            return;
        }
        
        element.setAttribute('data-color-scheme', schemeName);
    }
    
    /**
     * Get a color value from the current scheme
     * @param {string} colorKey - The color key (e.g., 'highlight', 'background')
     * @param {string} schemeName - Optional: use a specific scheme instead of current
     * @returns {string} The hex color value
     */
    getColor(colorKey, schemeName = null) {
        const scheme = schemeName || this.currentScheme;
        return COLOR_SCHEMES[scheme]?.[colorKey] || '#000000';
    }
    
    /**
     * Get all colors from the current scheme
     * @param {string} schemeName - Optional: use a specific scheme instead of current
     * @returns {object} Object containing all colors
     */
    getColors(schemeName = null) {
        const scheme = schemeName || this.currentScheme;
        return COLOR_SCHEMES[scheme] || COLOR_SCHEMES[this.DEFAULT_SCHEME];
    }
    
    /**
     * Convert hex color to RGB array [r, g, b] with values 0-255
     * @param {string} hex - Hex color string
     * @returns {array} RGB values
     */
    hexToRGB(hex) {
        const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
        return result ? [
            parseInt(result[1], 16),
            parseInt(result[2], 16),
            parseInt(result[3], 16)
        ] : [0, 0, 0];
    }
    
    /**
     * Convert hex color to RGB array [r, g, b] with values 0-1 (for canvas)
     * @param {string} hex - Hex color string
     * @returns {array} Normalized RGB values
     */
    hexToRGBNormalized(hex) {
        const rgb = this.hexToRGB(hex);
        return rgb.map(v => v / 255);
    }
    
    /**
     * Get a CSS variable value
     * @param {string} varName - CSS variable name (with or without --)
     * @returns {string} The CSS variable value
     */
    getCSSVariable(varName) {
        if (!varName.startsWith('--')) {
            varName = '--' + varName;
        }
        return getComputedStyle(document.documentElement).getPropertyValue(varName).trim();
    }
    
    /**
     * Create a scheme selector dropdown UI element
     * @param {object} options - Configuration options
     * @returns {HTMLElement} The select element
     */
    createSchemeSelector(options = {}) {
        const {
            id = 'scheme-selector',
            label = 'Color Scheme:',
            containerClass = 'scheme-selector-container'
        } = options;
        
        const container = document.createElement('div');
        container.className = containerClass;
        
        if (label) {
            const labelEl = document.createElement('label');
            labelEl.textContent = label;
            labelEl.htmlFor = id;
            container.appendChild(labelEl);
        }
        
        const select = document.createElement('select');
        select.id = id;
        
        const schemes = this.getAvailableSchemes();
        schemes.forEach(scheme => {
            const option = document.createElement('option');
            option.value = scheme;
            option.textContent = scheme.replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
            if (scheme === this.currentScheme) {
                option.selected = true;
            }
            select.appendChild(option);
        });
        
        select.addEventListener('change', (e) => {
            this.setGlobalScheme(e.target.value);
        });
        
        container.appendChild(select);
        return container;
    }
    
    /**
     * Save scheme to localStorage
     */
    saveScheme(schemeName) {
        try {
            localStorage.setItem(this.STORAGE_KEY, schemeName);
        } catch (e) {
            console.warn('Could not save color scheme to localStorage:', e);
        }
    }
    
    /**
     * Load saved scheme from localStorage
     */
    loadSavedScheme() {
        try {
            const saved = localStorage.getItem(this.STORAGE_KEY);
            if (saved && COLOR_SCHEMES[saved]) {
                this.currentScheme = saved;
            }
        } catch (e) {
            console.warn('Could not load color scheme from localStorage:', e);
        }
    }
    
    /**
     * Reset to default scheme
     */
    reset() {
        this.setGlobalScheme(this.DEFAULT_SCHEME);
    }
}

// Create global instance
const styleConfig = new StyleConfig();

// Auto-apply saved scheme on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        styleConfig.setGlobalScheme(styleConfig.currentScheme, false);
    });
} else {
    styleConfig.setGlobalScheme(styleConfig.currentScheme, false);
}

// Export for use in modules or global scope
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { StyleConfig, styleConfig };
}
