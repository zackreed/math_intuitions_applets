// Auto-generated easing functions for JavaScript use
// Generated from unified_animation_timing.py

const EASING_FUNCTIONS = {
  linear: (t) => t,

  smooth: (t) => {
    const s = 1 - t;
    return (t**3) * (10 * s * s + 5 * s * t + t * t);
  },

  rushInto: (t) => 2 * EASING_FUNCTIONS.smooth(0.5 * t),

  rushFrom: (t) => 2 * EASING_FUNCTIONS.smooth(0.5 * (t + 1)) - 1,

  slowInto: (t) => Math.sqrt(1 - (1 - t) * (1 - t)),

  easeInSine: (t) => 1 - Math.cos((t * Math.PI) / 2),

  easeOutSine: (t) => Math.sin((t * Math.PI) / 2),

  easeInOutSine: (t) => -(Math.cos(Math.PI * t) - 1) / 2,

  easeInQuad: (t) => t * t,

  easeOutQuad: (t) => 1 - (1 - t) * (1 - t),

  easeInOutQuad: (t) => t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2,

  easeInCubic: (t) => t * t * t,

  easeOutCubic: (t) => 1 - Math.pow(1 - t, 3),

  easeInOutCubic: (t) => t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2,

  easeInBack: (t) => {
    const s = 1.70158;
    return t * t * ((s + 1) * t - s);
  },

  easeOutBack: (t) => {
    const s = 1.70158;
    return 1 + Math.pow(t - 1, 2) * ((s + 1) * (t - 1) + s);
  }
};

const CSS_TIMING_FUNCTIONS = {
  'linear': 'linear',
  'ease': 'ease',
  'ease-in': 'cubic-bezier(0.42, 0, 1.0, 1.0)',
  'ease-out': 'cubic-bezier(0, 0, 0.58, 1.0)',
  'ease-in-out': 'cubic-bezier(0.42, 0, 0.58, 1.0)',
  'smooth': 'cubic-bezier(0.37, 0, 0.63, 1)',
  'ease-in-sine': 'cubic-bezier(0.12, 0, 0.39, 0)',
  'ease-out-sine': 'cubic-bezier(0.61, 1, 0.88, 1)',
  'ease-in-out-sine': 'cubic-bezier(0.37, 0, 0.63, 1)',
  'ease-in-quad': 'cubic-bezier(0.11, 0, 0.5, 0)',
  'ease-out-quad': 'cubic-bezier(0.5, 1, 0.89, 1)',
  'ease-in-out-quad': 'cubic-bezier(0.45, 0, 0.55, 1)',
  'ease-in-cubic': 'cubic-bezier(0.32, 0, 0.67, 0)',
  'ease-out-cubic': 'cubic-bezier(0.33, 1, 0.68, 1)',
  'ease-in-out-cubic': 'cubic-bezier(0.65, 0, 0.35, 1)',
  'ease-in-back': 'cubic-bezier(0.36, 0, 0.66, -0.56)',
  'ease-out-back': 'cubic-bezier(0.34, 1.56, 0.64, 1)',
  'ease-in-out-back': 'cubic-bezier(0.68, -0.6, 0.32, 1.6)'
};


// Get easing function by name
function getEasingFunction(name) {
  return EASING_FUNCTIONS[name] || EASING_FUNCTIONS.linear;
}

// Get CSS timing function string
function getCssTimingFunction(name) {
  return CSS_TIMING_FUNCTIONS[name] || 'linear';
}

// Apply easing to a value
function applyEasing(startValue, endValue, t, easingName = 'linear') {
  const easingFunc = getEasingFunction(easingName);
  const easedT = easingFunc(t);
  return startValue + (endValue - startValue) * easedT;
}

// Export for use in modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    EASING_FUNCTIONS,
    CSS_TIMING_FUNCTIONS,
    getEasingFunction,
    getCssTimingFunction,
    applyEasing
  };
}
