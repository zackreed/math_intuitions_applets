/**
 * Global Style Configuration
 * 
 * This file controls the color scheme used across all pages and walkthroughs.
 * To change the global style, simply update the GLOBAL_COLOR_SCHEME constant below.
 * 
 * Available color schemes:
 * - 'default' - Classic black background with vibrant colors
 * - 'dark_muted_pastels' - Soft pastels on dark gray
 * - 'deep_jewel_tones' - Rich, saturated jewel colors
 * - 'contrasting_vibrancy' - Bright, bold, maximum energy
 * - 'erau' - ERAU university branding
 * - 'dark' - Modern sophisticated dark theme
 * - 'high_contrast' - Maximum accessibility
 * - 'warm_sunset' - Warm oranges and browns
 * - 'cool_ocean' - Blues and cyans
 * - 'forest_earth' - Greens and earth tones
 */

// ============================================
// CHANGE THIS TO SET THE GLOBAL COLOR SCHEME
// ============================================
const GLOBAL_COLOR_SCHEME = 'dark_muted_pastels';
// ============================================

/**
 * Apply the global color scheme to the current page
 * This function runs automatically when the page loads
 */
function applyGlobalColorScheme() {
    // Set the data-color-scheme attribute on the document root
    document.documentElement.setAttribute('data-color-scheme', GLOBAL_COLOR_SCHEME);
    
    // Also set it on body as a fallback
    document.body.setAttribute('data-color-scheme', GLOBAL_COLOR_SCHEME);
    
    // Log for debugging (can be removed in production)
    console.log(`Applied color scheme: ${GLOBAL_COLOR_SCHEME}`);
}

/**
 * Get the current active color scheme
 */
function getActiveColorScheme() {
    return GLOBAL_COLOR_SCHEME;
}

/**
 * Get colors from the active scheme
 * Requires color-schemes.js to be loaded
 */
function getSchemeColor(colorKey) {
    if (typeof COLOR_SCHEMES !== 'undefined' && COLOR_SCHEMES[GLOBAL_COLOR_SCHEME]) {
        return COLOR_SCHEMES[GLOBAL_COLOR_SCHEME][colorKey];
    }
    console.warn(`Color scheme or color key not found: ${GLOBAL_COLOR_SCHEME}.${colorKey}`);
    return null;
}

// Apply the color scheme immediately when the script loads
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyGlobalColorScheme);
} else {
    // DOMContentLoaded has already fired
    applyGlobalColorScheme();
}

// Export for use in other scripts
if (typeof window !== 'undefined') {
    window.GLOBAL_COLOR_SCHEME = GLOBAL_COLOR_SCHEME;
    window.getActiveColorScheme = getActiveColorScheme;
    window.getSchemeColor = getSchemeColor;
}
