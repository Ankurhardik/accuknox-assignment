"""
Module: score_processor.py
Package: Problem_Statement_1.task2_data_viz

Processes student test scores, computes descriptive cohort benchmarks,
and renders a modern dual-panel matplotlib visualization chart.
"""

import os
import json
import logging
from typing import List, Dict, Any, Tuple
import matplotlib.pyplot as plt

logger = logging.getLogger("ScoreProcessor")


class StudentScoreProcessor:
    def __init__(
        self,
        data_path: str = "students_scores.json",
        output_image: str = "student_scores_visualization.png"
    ):
        self.data_path = data_path
        self.output_image = output_image

    def load_data(self) -> List[Dict[str, Any]]:
        """Loads score records from JSON file with safe fallback."""
        if os.path.exists(self.data_path):
            try:
                with open(self.data_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    logger.info("Loaded %d student records from '%s'.", len(data), self.data_path)
                    return data
            except Exception as e:
                logger.warning("Error reading '%s': %s. Using default dataset.", self.data_path, e)

        return [
            {"student_id": "STU001", "name": "Aarav Sharma", "math": 88, "science": 92, "english": 79, "computer_science": 95},
            {"student_id": "STU002", "name": "Diya Patel", "math": 76, "science": 85, "english": 88, "computer_science": 82},
            {"student_id": "STU003", "name": "Rohan Verma", "math": 95, "science": 89, "english": 74, "computer_science": 98},
            {"student_id": "STU004", "name": "Ananya Iyer", "math": 64, "science": 70, "english": 85, "computer_science": 78},
            {"student_id": "STU005", "name": "Kabir Mehta", "math": 82, "science": 78, "english": 80, "computer_science": 89},
            {"student_id": "STU006", "name": "Sneha Reddy", "math": 91, "science": 94, "english": 90, "computer_science": 96},
            {"student_id": "STU007", "name": "Vikram Singh", "math": 58, "science": 65, "english": 72, "computer_science": 68},
            {"student_id": "STU008", "name": "Meera Joshi", "math": 85, "science": 88, "english": 92, "computer_science": 91}
        ]

    def compute_metrics(
        self,
        data: List[Dict[str, Any]]
    ) -> Tuple[List[Dict[str, Any]], Dict[str, float], float]:
        """Calculates per-student averages, subject benchmarks, and overall mean."""
        subjects = ["math", "science", "english", "computer_science"]
        students = []
        subject_totals = {s: 0.0 for s in subjects}
        total_score, total_count = 0.0, 0

        for item in data:
            scores = [float(item[s]) for s in subjects if s in item and isinstance(item[s], (int, float))]
            avg = sum(scores) / len(scores) if scores else 0.0
            
            for s in subjects:
                if s in item:
                    subject_totals[s] += float(item[s])
            
            total_score += sum(scores)
            total_count += len(scores)
            
            students.append({
                "name": item.get("name", item.get("student_id", "Unknown")),
                "average": round(avg, 2)
            })

        subject_averages = {s: round(v / len(data), 2) for s, v in subject_totals.items()}
        class_average = round(total_score / total_count, 2) if total_count > 0 else 0.0

        return students, subject_averages, class_average

    def render_chart(
        self,
        students: List[Dict[str, Any]],
        subjects: Dict[str, float],
        class_avg: float
    ) -> str:
        """Renders styled dual-panel chart."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), gridspec_kw={'width_ratios': [2, 1]})

        names = [s["name"] for s in students]
        averages = [s["average"] for s in students]
        colors = ['#2b5c8f' if a >= class_avg else '#d95f02' for a in averages]

        bars1 = ax1.bar(names, averages, color=colors, width=0.6, edgecolor='#1b3b5f', linewidth=1.2, zorder=3)
        ax1.axhline(class_avg, color='#e7298a', linestyle='--', linewidth=1.8, label=f'Class Average: {class_avg:.2f}', zorder=4)
        ax1.set_title("Student Average Test Scores", fontsize=14, fontweight='bold', pad=12)
        ax1.set_ylabel("Average Score (%)", fontsize=11)
        ax1.set_ylim(0, 105)
        ax1.set_xticks(range(len(names)))
        ax1.set_xticklabels(names, rotation=35, ha='right', fontsize=9)
        ax1.grid(axis='y', linestyle=':', alpha=0.6, zorder=0)
        ax1.legend(loc='lower right', framealpha=0.9)

        for bar in bars1:
            yval = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f"{yval:.1f}", ha='center', va='bottom', fontsize=9)

        subject_labels = [k.replace('_', '\n').title() for k in subjects.keys()]
        subject_vals = list(subjects.values())
        subj_colors = ['#1b9e77', '#7570b3', '#e6ab02', '#66a61e']

        bars2 = ax2.bar(subject_labels, subject_vals, color=subj_colors, width=0.55, edgecolor='#333333', linewidth=1.1, zorder=3)
        ax2.set_title("Subject Cohort Averages", fontsize=14, fontweight='bold', pad=12)
        ax2.set_ylabel("Subject Average (%)", fontsize=11)
        ax2.set_ylim(0, 105)
        ax2.grid(axis='y', linestyle=':', alpha=0.6, zorder=0)

        for bar in bars2:
            yval = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2.0, yval + 1.5, f"{yval:.1f}", ha='center', va='bottom', fontsize=9)

        plt.tight_layout()
        plt.savefig(self.output_image, dpi=300)
        plt.close()
        logger.info("Saved visualization to '%s'.", self.output_image)
        return self.output_image

    def run(self) -> None:
        """Executes full processing and rendering lifecycle."""
        data = self.load_data()
        students, subjects, class_avg = self.compute_metrics(data)
        
        print("\n" + "=" * 65)
        print("                 STUDENT PERFORMANCE METRICS                 ")
        print("=" * 65)
        print(f"{'Student Name':<22} | {'Average Score':<15} | {'Status vs Cohort':<15}")
        print("-" * 65)
        for s in students:
            status = "Above Average" if s['average'] >= class_avg else "Below Average"
            print(f"{s['name']:<22} | {s['average']:<15.2f} | {status:<15}")
        print("=" * 65)
        print(f"Overall Cohort Average: {class_avg:.2f} / 100\n")
        
        img = self.render_chart(students, subjects, class_avg)
        print(f"Chart successfully exported to: {img}\n")
