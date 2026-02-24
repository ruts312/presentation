import re

html_file = '/Users/alikbekmukanbetov/Desktop/presentation/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update body CSS
content = re.sub(
    r'body\s*{[^}]*}',
    r'''body {
            font-family: 'PT Serif', serif;
            margin: 0;
            padding: 0;
            overflow: hidden; /* Prevent all scrolling */
            background-color: #2a0a0a;
            display: flex;
            justify-content: center;
            align-items: center; /* Center vertically */
            height: 100vh;
        }''',
    content
)

# 2. Update .slide CSS
content = re.sub(
    r'\.slide\s*{[^}]*}',
    r'''.slide {
            width: 1280px;
            height: 900px; /* Fixed height */
            display: none;
            position: absolute; /* Stack them */
            top: 50%;
            left: 50%;
            margin: 0;
            transform: translate(-50%, -50%) scale(var(--scale-factor, 1));
            opacity: 0;
            transition: opacity 0.5s ease-in-out;
            transform-origin: center center;
        }''',
    content
)

# 3. Update @keyframes fadeIn
content = re.sub(
    r'@keyframes fadeIn\s*{[^}]*from\s*{[^}]*}\s*to\s*{[^}]*}\s*}',
    r'''@keyframes fadeIn {
            from {
                opacity: 0;
                transform: translate(-50%, -50%) scale(calc(var(--scale-factor, 1) * 0.95));
            }
            to {
                opacity: 1;
                transform: translate(-50%, -50%) scale(var(--scale-factor, 1));
            }
        }''',
    content
)

# 4. Remove padding/margins from body if they are left in any other rules (none exist, but good to be careful)

# 5. Fix inner div heights in slides
content = content.replace('min-h-[900px]', 'h-[900px]')
content = content.replace('h-auto', '')

# 6. Add JS resize function
resize_js = """
        function calculateScale() {
            // Calculate scale to fit horizontally and vertically with a little margin
            // The controls are at the bottom, so leave some extra space at the bottom (e.g. 80px)
            const availableHeight = window.innerHeight - 80; 
            const scaleX = window.innerWidth / 1300; // 1280 + margin
            const scaleY = availableHeight / 920; // 900 + margin
            const scale = Math.min(scaleX, scaleY);
            document.documentElement.style.setProperty('--scale-factor', scale);
        }

        window.addEventListener('resize', calculateScale);
        calculateScale(); // Initial call
"""

if 'calculateScale' not in content:
    content = content.replace('// Initialize', resize_js + '\n        // Initialize')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Scroll fixed successfully.")
