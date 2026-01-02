// Auto-generated color schemes for JavaScript use
// Generated from unified_color_schemes.py

const COLOR_SCHEMES = {
  default: {
    text_background: '#000000',
    text: '#FFFFFF',
    text_surrounding: '#000000',
    background: '#000000',
    highlight: '#FFFF00',
    accent: '#58C4DD',
    time: '#C55F73',
    displacement: '#83C167',
    dot: '#FC6255',
    contrast_1: '#FF8C00',
    contrast_2: '#00CED1'
  },

  dark_muted_pastels: {
    text_background: '#2C2C2C',
    text: '#E4E4E4',
    text_surrounding: '#2C2C2C',
    background: '#2C2C2C',
    highlight: '#ABDADC',
    accent: '#FFC1CC',
    time: '#B39CD0',
    displacement: '#B2DFDB',
    dot: '#FF6B6B',
    contrast_1: '#FFB74D',
    contrast_2: '#81C784'
  },

  deep_jewel_tones: {
    text_background: '#1a1a1a',
    text: '#f0f0f0',
    text_surrounding: '#1a1a1a',
    background: '#1a1a1a',
    highlight: '#004d61',
    accent: '#822659',
    time: '#3e5641',
    displacement: '#90EE90',
    dot: '#FF6B6B',
    contrast_1: '#FFB74D',
    contrast_2: '#9C27B0'
  },

  contrasting_vibrancy: {
    text_background: '#181818',
    text: '#f7f7f7',
    text_surrounding: '#181818',
    background: '#181818',
    highlight: '#ff5722',
    accent: '#673ab7',
    time: '#ffeb3b',
    displacement: '#009688',
    dot: '#e91e63',
    contrast_1: '#c2185b',
    contrast_2: '#4caf50'
  },

  erau: {
    text_background: '#03539E',
    text: '#FFFFFF',
    text_surrounding: '#FFCB06',
    background: '#000000',
    highlight: '#FFCB06',
    accent: '#01B2E3',
    time: '#FFE066',
    displacement: '#90EE90',
    dot: '#FF6B6B',
    contrast_1: '#FF1493',
    contrast_2: '#32CD32'
  },

  dark: {
    text_background: '#000000',
    text: '#E0E0E0',
    text_surrounding: '#000000',
    background: '#000000',
    highlight: '#FF6B6B',
    accent: '#4ECDC4',
    time: '#45B7D1',
    displacement: '#96CEB4',
    dot: '#FECA57',
    contrast_1: '#FF69B4',
    contrast_2: '#00FA9A'
  },

  high_contrast: {
    text_background: '#000000',
    text: '#FFFFFF',
    text_surrounding: '#000000',
    background: '#000000',
    highlight: '#FFFF00',
    accent: '#00FFFF',
    time: '#FF00FF',
    displacement: '#00FF00',
    dot: '#FF0000',
    contrast_1: '#FFA500',
    contrast_2: '#8A2BE2'
  },

  warm_sunset: {
    text_background: '#1a0f0a',
    text: '#fff8f0',
    text_surrounding: '#2a1810',
    background: '#1a0f0a',
    highlight: '#ff6b35',
    accent: '#f7931e',
    time: '#fdc500',
    displacement: '#c1666b',
    dot: '#d62828',
    contrast_1: '#fcbf49',
    contrast_2: '#8b4513'
  },

  cool_ocean: {
    text_background: '#0a1f2e',
    text: '#e8f4f8',
    text_surrounding: '#0a1f2e',
    background: '#0a1f2e',
    highlight: '#00d9ff',
    accent: '#1e90ff',
    time: '#40e0d0',
    displacement: '#7fffd4',
    dot: '#ff6b9d',
    contrast_1: '#ff1493',
    contrast_2: '#00fa9a'
  },

  forest_earth: {
    text_background: '#1a2e1a',
    text: '#f0f8f0',
    text_surrounding: '#1a2e1a',
    background: '#1a2e1a',
    highlight: '#90ee90',
    accent: '#8fbc8f',
    time: '#daa520',
    displacement: '#9acd32',
    dot: '#dc143c',
    contrast_1: '#ff8c00',
    contrast_2: '#4682b4'
  }
};


// Helper function to get a color from a scheme
function getColor(schemeName, colorKey) {
  return COLOR_SCHEMES[schemeName]?.[colorKey] || '#000000';
}

// Helper function to convert hex to RGB
function hexToRgb(hex) {
  const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  } : null;
}

// Helper function to convert hex to RGBA string
function hexToRgba(hex, alpha = 1.0) {
  const rgb = hexToRgb(hex);
  return rgb ? `rgba(${rgb.r}, ${rgb.g}, ${rgb.b}, ${alpha})` : 'rgba(0, 0, 0, 1)';
}

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { COLOR_SCHEMES, getColor, hexToRgb, hexToRgba };
}
