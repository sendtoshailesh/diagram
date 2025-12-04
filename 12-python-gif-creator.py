"""
Python GIF Creator - Multiple Examples
Install: pip install pillow imageio matplotlib numpy
"""

from PIL import Image, ImageDraw, ImageFont
import imageio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

# Create output directory
os.makedirs('gif_output', exist_ok=True)

# ============================================
# Example 1: Simple Animation with Pillow
# ============================================
def create_simple_gif():
    """Create a simple animated GIF with moving circle"""
    frames = []
    width, height = 400, 300
    
    for i in range(30):
        # Create new image
        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)
        
        # Draw moving circle
        x = int(50 + (width - 100) * (i / 29))
        y = height // 2
        
        # Background gradient
        for j in range(height):
            color = (100 + j // 2, 150 + j // 3, 200)
            draw.line([(0, j), (width, j)], fill=color)
        
        # Draw circle
        radius = 30
        draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                     fill='red', outline='darkred', width=3)
        
        # Add text
        draw.text((10, 10), f'Frame {i+1}/30', fill='black')
        
        frames.append(img)
    
    # Save as GIF
    frames[0].save('gif_output/simple_animation.gif',
                   save_all=True,
                   append_images=frames[1:],
                   duration=100,
                   loop=0)
    print("✓ Created: gif_output/simple_animation.gif")


# ============================================
# Example 2: Data Visualization GIF
# ============================================
def create_chart_gif():
    """Create animated bar chart"""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    categories = ['A', 'B', 'C', 'D', 'E']
    frames = []
    
    for i in range(20):
        ax.clear()
        
        # Generate data
        values = [20 + i * 2, 30 + i * 1.5, 25 + i * 3, 35 + i * 2.5, 40 + i * 1.8]
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#95E1D3']
        
        # Create bar chart
        bars = ax.bar(categories, values, color=colors)
        
        # Styling
        ax.set_ylim(0, 100)
        ax.set_ylabel('Value', fontsize=12)
        ax.set_title(f'Animated Bar Chart - Step {i+1}', fontsize=14, fontweight='bold')
        ax.grid(axis='y', alpha=0.3)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontsize=10)
        
        # Save frame
        plt.tight_layout()
        fig.canvas.draw()
        frame = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        frame = frame.reshape(fig.canvas.get_width_height()[::-1] + (3,))
        frames.append(frame)
    
    plt.close()
    
    # Save as GIF
    imageio.mimsave('gif_output/chart_animation.gif', frames, duration=0.2)
    print("✓ Created: gif_output/chart_animation.gif")


# ============================================
# Example 3: Loading Spinner
# ============================================
def create_loading_spinner():
    """Create a loading spinner GIF"""
    frames = []
    size = 200
    center = size // 2
    
    for i in range(12):
        img = Image.new('RGBA', (size, size), color=(255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        
        angle = i * 30  # 12 positions
        
        # Draw spinner bars
        for j in range(12):
            bar_angle = (angle + j * 30) % 360
            opacity = int(255 * (1 - j / 12))
            
            # Calculate bar position
            rad = np.radians(bar_angle)
            x1 = center + np.cos(rad) * 40
            y1 = center + np.sin(rad) * 40
            x2 = center + np.cos(rad) * 70
            y2 = center + np.sin(rad) * 70
            
            color = (78, 205, 196, opacity)
            draw.line([(x1, y1), (x2, y2)], fill=color, width=8)
        
        frames.append(img)
    
    frames[0].save('gif_output/loading_spinner.gif',
                   save_all=True,
                   append_images=frames[1:],
                   duration=80,
                   loop=0,
                   transparency=0,
                   disposal=2)
    print("✓ Created: gif_output/loading_spinner.gif")


# ============================================
# Example 4: Text Animation
# ============================================
def create_text_animation():
    """Create animated text GIF"""
    frames = []
    width, height = 500, 200
    text = "Hello, World!"
    
    for i in range(len(text) + 10):
        img = Image.new('RGB', (width, height), color='#2C3E50')
        draw = ImageDraw.Draw(img)
        
        # Draw text progressively
        visible_text = text[:min(i, len(text))]
        
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        except:
            font = ImageFont.load_default()
        
        # Center text
        bbox = draw.textbbox((0, 0), visible_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        
        # Draw with shadow
        draw.text((x+2, y+2), visible_text, fill='#34495E', font=font)
        draw.text((x, y), visible_text, fill='#ECF0F1', font=font)
        
        # Add cursor
        if i < len(text):
            cursor_x = x + text_width + 5
            draw.rectangle([cursor_x, y, cursor_x+3, y+text_height], fill='#3498DB')
        
        frames.append(img)
    
    frames[0].save('gif_output/text_animation.gif',
                   save_all=True,
                   append_images=frames[1:],
                   duration=150,
                   loop=0)
    print("✓ Created: gif_output/text_animation.gif")


# ============================================
# Example 5: Progress Bar
# ============================================
def create_progress_bar():
    """Create animated progress bar"""
    frames = []
    width, height = 400, 100
    
    for i in range(101):
        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)
        
        # Background
        draw.rectangle([20, 30, width-20, 70], outline='#BDC3C7', width=2)
        
        # Progress fill
        progress_width = int((width - 40) * (i / 100))
        if progress_width > 0:
            # Gradient effect
            for x in range(progress_width):
                color_val = int(78 + (205-78) * (x / max(progress_width, 1)))
                draw.line([(20 + x, 30), (20 + x, 70)], 
                         fill=(color_val, 205, 196))
        
        # Percentage text
        draw.text((width//2, height//2), f'{i}%', 
                 fill='black', anchor='mm')
        
        frames.append(img)
    
    frames[0].save('gif_output/progress_bar.gif',
                   save_all=True,
                   append_images=frames[1:],
                   duration=50,
                   loop=0)
    print("✓ Created: gif_output/progress_bar.gif")


# ============================================
# Run all examples
# ============================================
if __name__ == '__main__':
    print("Creating GIF animations...\n")
    
    create_simple_gif()
    create_chart_gif()
    create_loading_spinner()
    create_text_animation()
    create_progress_bar()
    
    print("\n✅ All GIFs created successfully in 'gif_output' folder!")
    print("\nTips:")
    print("- Reduce duration for faster animation")
    print("- Increase duration for slower animation")
    print("- Use fewer frames to reduce file size")
    print("- Optimize with: gifsicle -O3 input.gif -o output.gif")
