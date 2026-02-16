# CSS Styling Guide

## Overview
The HARP Firmware Updater GUI now uses a centralized CSS file (`src/harp_updater_gui/static/styles.css`) for consistent styling across all components.

## CSS Variables
Custom properties defined in `:root` for easy theming:

```css
--primary-color: #2563eb
--success-color: #10b981
--warning-color: #f59e0b
--danger-color: #ef4444
```

## Key CSS Classes

### Layout Classes
- `.app-container` - Main application container with flexbox layout
- `.sidebar-left`, `.sidebar-right` - Sidebar panels with borders
- `.header-container` - Gradient header with branding

### Component Classes

#### Device List
- `.device-card` - Individual device card with hover effects
- `.device-card.selected` - Selected device state
- `.device-status-badge` - Status indicator (healthy, warning, error)
- `.device-metadata` - Secondary device information

#### Firmware Browser
- `.firmware-section` - Major section container
- `.section-header` - Section title with border
- `.firmware-item` - Firmware version card
- `.firmware-item.selected` - Selected firmware state
- `.metadata-tag` - Small informational tags

#### Update Workflow
- `.workflow-container` - Workflow sidebar container
- `.progress-step` - Individual progress step
- `.progress-step.active` - Currently active step
- `.progress-step.completed` - Completed step
- `.progress-step-icon` - Step status icon

### Utility Classes

#### Buttons
- `.btn` - Base button style
- `.btn-primary` - Primary action button (blue)
- `.btn-secondary` - Secondary action button (gray)
- `.btn-success` - Success button (green)
- `.btn-full` - Full-width button

#### Forms
- `.input-field` - Text input styling with focus states
- `.select-field` - Dropdown/select styling

#### Chips/Tags
- `.chip` - Base chip/tag style
- `.chip-primary`, `.chip-success`, `.chip-warning` - Colored variants

#### Alerts
- `.alert` - Base alert box
- `.alert-info`, `.alert-success`, `.alert-warning`, `.alert-error` - Alert variants

#### Spacing
- `.mt-1` through `.mt-4` - Margin top utilities
- `.mb-1` through `.mb-4` - Margin bottom utilities
- `.p-1` through `.p-4` - Padding utilities
- `.gap-1` through `.gap-3` - Gap utilities for flexbox

## Using CSS in Components

### Before (inline styles):
```python
ui.button('Click me').classes('bg-blue-500 text-white font-semibold hover:bg-blue-600')
```

### After (CSS classes):
```python
ui.button('Click me').classes('btn btn-primary')
```

## Benefits

1. **Consistency** - All components use the same color palette and spacing
2. **Maintainability** - Style changes in one place
3. **Performance** - CSS is cached by browsers
4. **Theming** - Easy to change colors via CSS variables
5. **Responsive** - Centralized media queries (if needed)

## Customization

To customize the theme:
1. Edit CSS variables in `styles.css` `:root` section
2. Modify specific component classes as needed
3. No need to touch Python component code

## File Structure
```
src/harp_updater_gui/
├── static/
│   └── styles.css          # Main stylesheet
├── components/
│   ├── header.py           # Uses: .header-container, .header-title
│   ├── device_list.py      # Uses: .device-card, .device-status-badge
│   ├── firmware_browser.py # Uses: .firmware-section, .firmware-item
│   └── update_workflow.py  # Uses: .progress-step, .workflow-container
└── main.py                 # Loads CSS file
```

## Development Tips

1. **Testing Styles** - Use browser DevTools to inspect and test CSS changes
2. **Hot Reload** - Restart app to see CSS changes (reload mode disabled)
3. **Adding Classes** - Add new utility classes to `styles.css` for reusable patterns
4. **Naming Convention** - Use BEM-like naming: `component-element-modifier`
