#!/usr/bin/env python3
"""
Entry point for Task 2: Data Processing and Visualization.
Run directly via: python run.py
"""
import os
import sys

# Ensure module path resolution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from Problem_Statement_1.task2_data_viz.score_processor import StudentScoreProcessor

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, "students_scores.json")
    chart_path = os.path.join(current_dir, "student_scores_visualization.png")
    
    processor = StudentScoreProcessor(data_path=json_path, output_image=chart_path)
    processor.run()
