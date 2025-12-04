"""
Agentic Infographic Generation System
A multi-agent approach to convert text into infographics

This demonstrates the concept - requires OpenAI API key and additional libraries
Install: pip install openai pillow matplotlib numpy
"""

import json
import re
from typing import Dict, List, Any
from dataclasses import dataclass
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np

# Note: In production, use actual OpenAI API
# This is a demonstration of the architecture

@dataclass
class InfographicConcept:
    """Structured representation of infographic concept"""
    title: str
    sections: List[Dict[str, Any]]
    visual_type: str
    color_scheme: List[str]
    layout: str
    data_points: List[Dict[str, Any]]


class AnalyzerAgent:
    """Agent responsible for analyzing text and extracting key information"""
    
    def __init__(self):
        self.name = "Analyzer"
    
    def analyze_text(self, text: str) -> Dict[str, Any]:
        """
        Analyze text to extract:
        - Main concepts
        - Data points (numbers, statistics)
        - Relationships
        - Structure (sequential, hierarchical, comparative)
        """
        print(f"[{self.name}] Analyzing text structure...")
        
        # Extract numbers and statistics
        numbers = re.findall(r'\d+(?:\.\d+)?%?', text)
        
        # Identify structure keywords
        structure_keywords = {
            'sequential': ['first', 'then', 'next', 'finally', 'step'],
            'comparative': ['versus', 'compared to', 'better than', 'vs'],
            'hierarchical': ['top', 'bottom', 'level', 'tier'],
            'temporal': ['timeline', 'history', 'evolution', 'year']
        }
        
        detected_structure = 'general'
        for structure_type, keywords in structure_keywords.items():
            if any(keyword in text.lower() for keyword in keywords):
                detected_structure = structure_type
                break
        
        # Extract sentences as key points
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        analysis = {
            'key_points': sentences[:5],  # Top 5 points
            'data_points': numbers,
            'structure_type': detected_structure,
            'word_count': len(text.split()),
            'complexity': 'simple' if len(sentences) < 5 else 'complex'
        }
        
        print(f"[{self.name}] Detected structure: {detected_structure}")
        print(f"[{self.name}] Found {len(numbers)} data points")
        
        return analysis


class StrategistAgent:
    """Agent responsible for determining visualization strategy"""
    
    def __init__(self):
        self.name = "Strategist"
    
    def determine_strategy(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Based on analysis, determine:
        - Best visualization type
        - Layout approach
        - Color scheme
        - Visual elements needed
        """
        print(f"[{self.name}] Determining visualization strategy...")
        
        structure = analysis['structure_type']
        
        # Map structure to visualization type
        viz_mapping = {
            'sequential': {
                'type': 'flowchart',
                'layout': 'horizontal',
                'elements': ['arrows', 'numbered_boxes', 'icons']
            },
            'comparative': {
                'type': 'comparison',
                'layout': 'side_by_side',
                'elements': ['split_view', 'vs_symbol', 'checkmarks']
            },
            'hierarchical': {
                'type': 'pyramid',
                'layout': 'vertical',
                'elements': ['levels', 'hierarchy_lines', 'labels']
            },
            'temporal': {
                'type': 'timeline',
                'layout': 'horizontal',
                'elements': ['timeline_line', 'date_markers', 'milestones']
            },
            'general': {
                'type': 'mixed',
                'layout': 'grid',
                'elements': ['sections', 'icons', 'text_blocks']
            }
        }
        
        strategy = viz_mapping.get(structure, viz_mapping['general'])
        
        # Determine color scheme based on content
        color_schemes = {
            'professional': ['#2C3E50', '#3498DB', '#ECF0F1'],
            'energetic': ['#E74C3C', '#F39C12', '#ECF0F1'],
            'natural': ['#27AE60', '#16A085', '#ECF0F1'],
            'tech': ['#9B59B6', '#3498DB', '#ECF0F1']
        }
        
        strategy['color_scheme'] = color_schemes['professional']
        strategy['font_sizes'] = {
            'title': 24,
            'heading': 18,
            'body': 12
        }
        
        print(f"[{self.name}] Recommended: {strategy['type']} visualization")
        
        return strategy


class DesignerAgent:
    """Agent responsible for creating the visual design"""
    
    def __init__(self):
        self.name = "Designer"
    
    def create_infographic(self, analysis: Dict[str, Any], 
                          strategy: Dict[str, Any]) -> plt.Figure:
        """
        Create the actual infographic based on strategy
        """
        print(f"[{self.name}] Creating visual design...")
        
        viz_type = strategy['type']
        
        if viz_type == 'flowchart':
            return self._create_flowchart(analysis, strategy)
        elif viz_type == 'comparison':
            return self._create_comparison(analysis, strategy)
        elif viz_type == 'timeline':
            return self._create_timeline(analysis, strategy)
        else:
            return self._create_general(analysis, strategy)
    
    def _create_flowchart(self, analysis, strategy):
        """Create a flowchart-style infographic"""
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis('off')
        
        colors = strategy['color_scheme']
        key_points = analysis['key_points'][:4]  # Max 4 steps
        
        # Title
        ax.text(5, 4.5, 'Process Flow', 
                ha='center', va='center', 
                fontsize=strategy['font_sizes']['title'],
                fontweight='bold', color=colors[0])
        
        # Create flow boxes
        box_width = 1.8
        box_height = 0.8
        spacing = 2.2
        start_x = 1
        y_pos = 2.5
        
        for i, point in enumerate(key_points):
            x_pos = start_x + i * spacing
            
            # Box
            box = FancyBboxPatch(
                (x_pos, y_pos - box_height/2),
                box_width, box_height,
                boxstyle="round,pad=0.1",
                facecolor=colors[1],
                edgecolor=colors[0],
                linewidth=2
            )
            ax.add_patch(box)
            
            # Number
            ax.text(x_pos + 0.3, y_pos + 0.3, str(i+1),
                   fontsize=16, fontweight='bold',
                   color='white',
                   bbox=dict(boxstyle='circle', facecolor=colors[0]))
            
            # Text (truncated)
            text = point[:30] + '...' if len(point) > 30 else point
            ax.text(x_pos + box_width/2, y_pos - 0.1, text,
                   ha='center', va='center',
                   fontsize=10, color='white',
                   wrap=True)
            
            # Arrow
            if i < len(key_points) - 1:
                arrow_x = x_pos + box_width + 0.1
                ax.annotate('', xy=(arrow_x + 0.3, y_pos),
                           xytext=(arrow_x, y_pos),
                           arrowprops=dict(arrowstyle='->', 
                                         lw=2, color=colors[0]))
        
        plt.tight_layout()
        return fig
    
    def _create_comparison(self, analysis, strategy):
        """Create a comparison infographic"""
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        colors = strategy['color_scheme']
        
        # Title
        ax.text(5, 9, 'Comparison', 
                ha='center', fontsize=24, fontweight='bold')
        
        # VS symbol
        ax.text(5, 5, 'VS', 
                ha='center', va='center',
                fontsize=36, fontweight='bold',
                color=colors[1],
                bbox=dict(boxstyle='circle', facecolor=colors[2], 
                         edgecolor=colors[0], linewidth=3))
        
        # Left side
        left_box = Rectangle((0.5, 2), 3.5, 5, 
                             facecolor=colors[1], alpha=0.3,
                             edgecolor=colors[0], linewidth=2)
        ax.add_patch(left_box)
        ax.text(2.25, 6.5, 'Option A', 
                ha='center', fontsize=18, fontweight='bold')
        
        # Right side
        right_box = Rectangle((6, 2), 3.5, 5,
                              facecolor=colors[1], alpha=0.3,
                              edgecolor=colors[0], linewidth=2)
        ax.add_patch(right_box)
        ax.text(7.75, 6.5, 'Option B',
                ha='center', fontsize=18, fontweight='bold')
        
        plt.tight_layout()
        return fig
    
    def _create_timeline(self, analysis, strategy):
        """Create a timeline infographic"""
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 5)
        ax.axis('off')
        
        colors = strategy['color_scheme']
        
        # Title
        ax.text(5, 4.5, 'Timeline', 
                ha='center', fontsize=24, fontweight='bold')
        
        # Timeline line
        ax.plot([1, 9], [2.5, 2.5], color=colors[0], linewidth=3)
        
        # Milestones
        milestones = analysis['key_points'][:5]
        positions = np.linspace(1, 9, len(milestones))
        
        for i, (pos, milestone) in enumerate(zip(positions, milestones)):
            # Marker
            ax.plot(pos, 2.5, 'o', markersize=15, 
                   color=colors[1], markeredgecolor=colors[0],
                   markeredgewidth=2)
            
            # Text (alternating above/below)
            y_text = 3.2 if i % 2 == 0 else 1.8
            text = milestone[:25] + '...' if len(milestone) > 25 else milestone
            ax.text(pos, y_text, text,
                   ha='center', va='center',
                   fontsize=9, wrap=True,
                   bbox=dict(boxstyle='round', facecolor=colors[2],
                           edgecolor=colors[0]))
        
        plt.tight_layout()
        return fig
    
    def _create_general(self, analysis, strategy):
        """Create a general infographic"""
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        
        colors = strategy['color_scheme']
        
        # Title
        ax.text(5, 9, 'Key Information', 
                ha='center', fontsize=24, fontweight='bold',
                color=colors[0])
        
        # Create grid of information boxes
        key_points = analysis['key_points'][:6]
        rows, cols = 2, 3
        
        for i, point in enumerate(key_points):
            row = i // cols
            col = i % cols
            
            x = 1 + col * 3
            y = 7 - row * 3
            
            # Box
            box = FancyBboxPatch(
                (x, y - 1), 2.5, 1.5,
                boxstyle="round,pad=0.1",
                facecolor=colors[1], alpha=0.3,
                edgecolor=colors[0], linewidth=2
            )
            ax.add_patch(box)
            
            # Number badge
            ax.text(x + 0.3, y - 0.2, str(i+1),
                   fontsize=14, fontweight='bold',
                   color='white',
                   bbox=dict(boxstyle='circle', facecolor=colors[0]))
            
            # Text
            text = point[:40] + '...' if len(point) > 40 else point
            ax.text(x + 1.25, y - 0.5, text,
                   ha='center', va='center',
                   fontsize=9, wrap=True)
        
        plt.tight_layout()
        return fig


class OptimizerAgent:
    """Agent responsible for optimizing and refining the design"""
    
    def __init__(self):
        self.name = "Optimizer"
    
    def optimize(self, fig: plt.Figure, preferences: Dict[str, Any]) -> plt.Figure:
        """
        Optimize the infographic:
        - Adjust spacing
        - Improve readability
        - Apply final touches
        """
        print(f"[{self.name}] Optimizing design...")
        
        # Add watermark if requested
        if preferences.get('add_watermark'):
            ax = fig.axes[0]
            ax.text(0.5, 0.02, preferences.get('watermark_text', 'Created with AI'),
                   ha='center', va='bottom',
                   fontsize=8, alpha=0.5,
                   transform=fig.transFigure)
        
        # Adjust DPI for quality
        fig.set_dpi(preferences.get('dpi', 150))
        
        print(f"[{self.name}] Optimization complete")
        
        return fig


class InfographicAgentSystem:
    """Main orchestrator for the multi-agent system"""
    
    def __init__(self):
        self.analyzer = AnalyzerAgent()
        self.strategist = StrategistAgent()
        self.designer = DesignerAgent()
        self.optimizer = OptimizerAgent()
    
    def create_infographic(self, text: str, 
                          preferences: Dict[str, Any] = None) -> plt.Figure:
        """
        Main pipeline to create infographic from text
        """
        if preferences is None:
            preferences = {}
        
        print("\n" + "="*60)
        print("INFOGRAPHIC GENERATION PIPELINE")
        print("="*60 + "\n")
        
        # Step 1: Analyze
        print("STEP 1: Analysis")
        print("-" * 60)
        analysis = self.analyzer.analyze_text(text)
        
        # Step 2: Strategy
        print("\nSTEP 2: Strategy")
        print("-" * 60)
        strategy = self.strategist.determine_strategy(analysis)
        
        # Step 3: Design
        print("\nSTEP 3: Design")
        print("-" * 60)
        fig = self.designer.create_infographic(analysis, strategy)
        
        # Step 4: Optimize
        print("\nSTEP 4: Optimization")
        print("-" * 60)
        final_fig = self.optimizer.optimize(fig, preferences)
        
        print("\n" + "="*60)
        print("GENERATION COMPLETE")
        print("="*60 + "\n")
        
        return final_fig


# ============================================
# Example Usage
# ============================================

if __name__ == '__main__':
    # Initialize the system
    system = InfographicAgentSystem()
    
    # Example 1: Process text
    text1 = """
    First, gather all requirements from stakeholders. 
    Then, create a detailed project plan with timelines. 
    Next, assemble your team and assign responsibilities. 
    Finally, execute the plan and monitor progress regularly.
    """
    
    print("Example 1: Process Flow")
    fig1 = system.create_infographic(text1, {
        'add_watermark': True,
        'watermark_text': 'AI Generated',
        'dpi': 150
    })
    fig1.savefig('gif_output/infographic_process.png', 
                 bbox_inches='tight', dpi=150)
    print("✓ Saved: gif_output/infographic_process.png\n")
    
    # Example 2: Comparison text
    text2 = """
    Product A offers better performance compared to Product B.
    Product A has 50% faster processing versus Product B.
    However, Product B is more affordable than Product A.
    """
    
    print("\nExample 2: Comparison")
    fig2 = system.create_infographic(text2, {'dpi': 150})
    fig2.savefig('gif_output/infographic_comparison.png',
                 bbox_inches='tight', dpi=150)
    print("✓ Saved: gif_output/infographic_comparison.png\n")
    
    # Example 3: Timeline text
    text3 = """
    In 2020, the company was founded.
    By 2021, we reached 1000 customers.
    In 2022, we expanded to international markets.
    2023 saw the launch of our mobile app.
    In 2024, we achieved profitability.
    """
    
    print("\nExample 3: Timeline")
    fig3 = system.create_infographic(text3, {'dpi': 150})
    fig3.savefig('gif_output/infographic_timeline.png',
                 bbox_inches='tight', dpi=150)
    print("✓ Saved: gif_output/infographic_timeline.png\n")
    
    print("✅ All infographics generated successfully!")
    print("\nNote: This is a demonstration of the agentic architecture.")
    print("For production use, integrate with:")
    print("  - OpenAI API for intelligent analysis")
    print("  - DALL-E for AI-generated graphics")
    print("  - Advanced layout engines")
    print("  - Real-time collaboration features")
