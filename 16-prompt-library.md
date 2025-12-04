# AI Prompt Library for Infographics

A comprehensive collection of tested prompts for generating infographics using various AI tools.

---

## Table of Contents
1. [ChatGPT/Claude Prompts](#chatgptclaude-prompts)
2. [DALL-E/Midjourney Prompts](#dall-emidjourney-prompts)
3. [Canva AI Prompts](#canva-ai-prompts)
4. [Code Generation Prompts](#code-generation-prompts)
5. [Multi-Step Workflows](#multi-step-workflows)

---

## ChatGPT/Claude Prompts

### Prompt 1: Mermaid Diagram Generator
```
I need you to convert the following text into a Mermaid diagram.

Text: [PASTE YOUR TEXT]

Requirements:
1. Analyze the text structure (process, hierarchy, comparison, etc.)
2. Choose the most appropriate Mermaid diagram type
3. Create a clean, well-organized diagram
4. Use colors to highlight important elements
5. Add clear labels and descriptions
6. Ensure the diagram is visually balanced

Output the complete Mermaid code that I can paste directly into a markdown file.
```

### Prompt 2: SVG Infographic Generator
```
Create an SVG infographic based on this information:

[PASTE YOUR TEXT]

Specifications:
- Size: 800x600px
- Style: Modern and minimalist
- Color scheme: Use complementary colors (suggest a palette)
- Include: Icons, text, and data visualization elements
- Layout: Organize information hierarchically

Provide:
1. Complete SVG code
2. Explanation of design choices
3. Suggestions for customization

Make it production-ready and well-commented.
```

### Prompt 3: Data Visualization Recommender
```
I have the following data/information:

[PASTE YOUR TEXT OR DATA]

Please:
1. Analyze what type of information this is
2. Recommend the 3 best visualization types
3. Explain why each would work well
4. Provide pros and cons for each option
5. Suggest color schemes for each
6. Give me the code to create the top recommendation

Target audience: [specify]
Platform: [web/print/social media]
```

### Prompt 4: Infographic Structure Planner
```
Help me plan an infographic for this topic:

Topic: [YOUR TOPIC]
Key points: [LIST KEY POINTS]
Target audience: [AUDIENCE]
Purpose: [inform/persuade/educate/entertain]

Please provide:
1. Suggested title and subtitle
2. Information hierarchy (what goes where)
3. Visual elements needed (charts, icons, illustrations)
4. Color palette recommendation with hex codes
5. Layout structure (sections and flow)
6. Typography suggestions (font pairings)
7. Call-to-action if applicable

Format your response as a detailed design brief.
```

### Prompt 5: Accessibility Checker
```
Review this infographic concept for accessibility:

[DESCRIBE YOUR INFOGRAPHIC OR PASTE DESIGN DETAILS]

Check for:
1. Color contrast ratios (WCAG AA compliance)
2. Text readability
3. Alternative text needs
4. Colorblind-friendly palette
5. Font size appropriateness
6. Information hierarchy clarity

Provide specific recommendations for improvements.
```

---

## DALL-E/Midjourney Prompts

### Prompt 6: Professional Infographic
```
Professional infographic design, [TOPIC], clean modern layout, 
flat design style, featuring [KEY ELEMENTS], 
color palette: [COLOR 1] and [COLOR 2] and white,
sans-serif typography, icons and data visualization,
minimalist aesthetic, high contrast, white background,
organized sections, visual hierarchy, 
aspect ratio 2:3, 8k resolution, vector style
```

**Example:**
```
Professional infographic design, "5 Steps to Better Sleep", clean modern layout,
flat design style, featuring numbered steps with moon and bed icons,
color palette: navy blue and soft purple and white,
sans-serif typography, icons and data visualization,
minimalist aesthetic, high contrast, white background,
organized sections, visual hierarchy,
aspect ratio 2:3, 8k resolution, vector style
```

### Prompt 7: Statistical Infographic
```
Data-driven infographic, [TOPIC], editorial style,
featuring bar charts, pie charts, and statistics,
color scheme: [COLORS], modern typography,
clean grid layout, numbers and percentages prominently displayed,
professional business aesthetic, white background,
data visualization focus, clear labels,
aspect ratio 16:9, high resolution, magazine quality
```

### Prompt 8: Timeline Infographic
```
Timeline infographic design, [TOPIC], horizontal layout,
chronological flow from left to right,
milestone markers with dates, connecting line,
color gradient from [COLOR 1] to [COLOR 2],
modern flat design, icons for each milestone,
clean typography, white background,
professional style, aspect ratio 3:1, 8k resolution
```

### Prompt 9: Comparison Infographic
```
Side-by-side comparison infographic, [OPTION A] vs [OPTION B],
split screen design, contrasting colors [COLOR A] and [COLOR B],
checkmarks and X marks, feature comparison table,
modern flat design, clear visual separation,
professional typography, white background,
balanced layout, aspect ratio 1:1, high resolution
```

### Prompt 10: Process Flow Infographic
```
Process flow infographic, [TOPIC], flowchart style,
numbered steps with arrows, circular flow or linear progression,
color scheme: [PRIMARY COLOR] with [ACCENT COLOR],
modern minimalist design, icons for each step,
clean sans-serif fonts, white background,
professional business style, clear visual hierarchy,
aspect ratio 4:3, vector style, 8k resolution
```

---

## Canva AI Prompts

### Prompt 11: Social Media Infographic
```
Create a social media infographic about [TOPIC] with these elements:
- Eye-catching title at the top
- 3-5 key statistics with large numbers
- Icons representing each point
- Color scheme: [COLORS]
- Modern, trendy design
- Optimized for Instagram (1080x1080px)
```

### Prompt 12: Educational Infographic
```
Design an educational infographic explaining [CONCEPT]:
- Clear step-by-step breakdown
- Illustrations or diagrams
- Easy-to-read fonts
- Friendly, approachable style
- Color palette suitable for learning materials
- Include a summary section
```

### Prompt 13: Business Report Infographic
```
Create a professional business infographic showing [DATA/METRICS]:
- Corporate color scheme
- Charts and graphs
- Key performance indicators highlighted
- Clean, minimal design
- Professional typography
- Suitable for presentations
```

---

## Code Generation Prompts

### Prompt 14: Python Matplotlib Generator
```
Generate Python code using matplotlib to create an infographic with:

Data: [PROVIDE DATA]
Type: [bar chart/line graph/pie chart/etc.]
Style: [modern/minimal/colorful]
Colors: [COLOR SCHEME]

Requirements:
1. Clean, well-commented code
2. Customizable parameters
3. High-resolution output (300 DPI)
4. Professional styling
5. Save as PNG and SVG

Include example usage and customization tips.
```

### Prompt 15: D3.js Interactive Generator
```
Create D3.js code for an interactive infographic:

Topic: [TOPIC]
Data: [PROVIDE DATA]
Interactions: [hover effects/click events/animations]
Style: [modern/minimal/bold]

Requirements:
1. Responsive design
2. Smooth animations
3. Tooltip on hover
4. Mobile-friendly
5. Accessible (ARIA labels)

Provide complete HTML, CSS, and JavaScript.
```

### Prompt 16: React Component Generator
```
Build a React component for an infographic showing [TOPIC]:

Features needed:
- Props for customization
- Responsive design
- Animation on scroll
- TypeScript types
- Styled-components or CSS modules

Data structure: [DESCRIBE DATA]
Visual style: [DESCRIBE STYLE]

Include:
1. Component code
2. PropTypes/TypeScript interfaces
3. Usage example
4. Styling
5. Animation logic
```

---

## Multi-Step Workflows

### Workflow 1: Complete Infographic Creation

**Step 1: Content Analysis**
```
Analyze this text and extract key information for an infographic:

[PASTE TEXT]

Provide:
1. Main message (one sentence)
2. 3-5 key points
3. Any statistics or data
4. Suggested visual metaphors
5. Recommended infographic type
```

**Step 2: Design Strategy**
```
Based on this analysis:
[PASTE STEP 1 OUTPUT]

Create a design strategy including:
1. Layout structure (sketch in text)
2. Color palette (3-5 colors with hex codes)
3. Typography (font suggestions)
4. Visual elements needed
5. Information flow
```

**Step 3: Code Generation**
```
Using this design strategy:
[PASTE STEP 2 OUTPUT]

Generate [Python/JavaScript/SVG] code to create the infographic.
Make it production-ready with comments.
```

**Step 4: Optimization**
```
Review this infographic code/design:
[PASTE CODE OR DESCRIPTION]

Optimize for:
1. File size
2. Load time
3. Accessibility
4. Mobile responsiveness
5. Cross-browser compatibility

Provide specific improvements.
```

### Workflow 2: Data to Visual

**Step 1: Data Understanding**
```
I have this data:
[PASTE DATA]

Help me understand:
1. What story does this data tell?
2. What patterns or trends exist?
3. What's the most important insight?
4. What comparisons would be valuable?
5. What visualization would work best?
```

**Step 2: Visualization Design**
```
Based on the data analysis:
[PASTE STEP 1 OUTPUT]

Design a visualization that:
1. Highlights the main insight
2. Makes comparisons clear
3. Is easy to understand at a glance
4. Works for [TARGET AUDIENCE]
5. Fits [PLATFORM/SIZE]

Provide detailed specifications.
```

**Step 3: Implementation**
```
Create the visualization using [TOOL/LANGUAGE]:
[PASTE SPECIFICATIONS]

Include:
- Complete code
- Customization options
- Export functionality
- Responsive behavior
```

---

## Advanced Prompts

### Prompt 17: AI-Powered Layout Generator
```
You are an expert infographic designer. Given this content:

[PASTE CONTENT]

Generate 3 different layout concepts:

For each concept, provide:
1. Layout name and description
2. ASCII art sketch of the layout
3. Pros and cons
4. Best use case
5. Color scheme suggestion
6. Estimated complexity (easy/medium/hard)

Help me choose the best option for [PURPOSE].
```

### Prompt 18: Brand-Aligned Infographic
```
Create an infographic that aligns with this brand:

Brand: [BRAND NAME]
Brand colors: [COLORS]
Brand personality: [ADJECTIVES]
Target audience: [AUDIENCE]
Content: [TOPIC/DATA]

Design an infographic that:
1. Reflects brand identity
2. Appeals to target audience
3. Communicates information clearly
4. Is shareable on social media
5. Stands out from competitors

Provide complete design specifications.
```

### Prompt 19: Animated Infographic Planner
```
Plan an animated infographic for:

Topic: [TOPIC]
Duration: [SECONDS]
Platform: [web/video/presentation]
Key points: [LIST POINTS]

Provide:
1. Storyboard (describe each scene)
2. Animation sequence and timing
3. Transition effects
4. Color and style guide
5. Technical requirements
6. Tools/libraries needed

Format as a production-ready animation brief.
```

### Prompt 20: A/B Testing Variants
```
Create 2 different infographic concepts for A/B testing:

Content: [PASTE CONTENT]
Goal: [increase engagement/drive clicks/educate]
Audience: [DESCRIBE AUDIENCE]

For each variant:
1. Design approach and rationale
2. Visual style description
3. Color scheme
4. Layout structure
5. Key differentiators
6. Hypothesis for which will perform better

Help me set up the test properly.
```

---

## Prompt Modifiers

### Style Modifiers
Add these to any prompt for specific styles:
- `minimalist and clean`
- `bold and colorful`
- `corporate and professional`
- `playful and friendly`
- `elegant and sophisticated`
- `tech-focused and modern`
- `hand-drawn and organic`
- `retro and vintage`

### Quality Modifiers
- `high resolution, 8k`
- `vector style, scalable`
- `print quality, 300 DPI`
- `web optimized`
- `mobile-first design`

### Audience Modifiers
- `for executives and decision makers`
- `for general public`
- `for technical audience`
- `for children and students`
- `for social media users`

---

## Tips for Better Prompts

### Do's
✅ Be specific about dimensions and format
✅ Specify color schemes with hex codes
✅ Mention target audience and platform
✅ Include examples or references
✅ Request multiple options
✅ Ask for explanations of choices
✅ Specify accessibility requirements

### Don'ts
❌ Use vague terms like "nice" or "good"
❌ Forget to mention constraints
❌ Skip the purpose/goal
❌ Ignore platform requirements
❌ Assume the AI knows your brand
❌ Request too many elements at once

---

## Prompt Testing Checklist

Before using a prompt, verify:
- [ ] Clear objective stated
- [ ] Specific requirements listed
- [ ] Format/dimensions specified
- [ ] Style preferences included
- [ ] Target audience mentioned
- [ ] Platform/use case defined
- [ ] Color preferences noted
- [ ] Output format requested

---

## Resources

### Prompt Inspiration
- PromptBase (marketplace for prompts)
- OpenArt (AI art prompts)
- Lexica (Stable Diffusion prompts)
- MidJourney Showcase

### Testing Tools
- ChatGPT (GPT-4 recommended)
- Claude (Anthropic)
- DALL-E 3
- Midjourney
- Stable Diffusion

### Prompt Engineering Guides
- OpenAI Prompt Engineering Guide
- Anthropic Prompt Library
- Learn Prompting (learnprompting.org)
