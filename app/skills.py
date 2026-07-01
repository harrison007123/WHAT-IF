# app/skills.py

import json

# ==========================================
# REUSABLE ADK SKILLS
# ==========================================
# These are standalone logic blocks that can be shared across multiple agents.
# They are more complex than simple tool functions and often involve calculations.

def risk_assessment_skill(risk_factors: list[str]) -> str:
    """
    Skill: Analyzes a list of risk factors and returns a formatted Risk Matrix.
    Used by: Legal Agent, Finance Agent, or a dedicated Risk Agent.
    """
    if not risk_factors:
        return "No immediate risks identified."
    
    score = len(risk_factors) * 25
    severity = "HIGH" if score > 50 else "MEDIUM" if score > 25 else "LOW"
    
    report = f"### Risk Assessment (Severity: {severity})\n"
    report += f"**Calculated Score:** {score}/100\n"
    for factor in risk_factors:
        report += f"- ⚠️ {factor}\n"
    return report

def roi_calculation_skill(investment: float, expected_return: float) -> str:
    """
    Skill: Calculates Return on Investment (ROI).
    Used by: Finance Agent, Sales Agent.
    """
    if investment <= 0:
        return "Invalid investment amount."
    
    roi_percentage = ((expected_return - investment) / investment) * 100
    
    return f"**ROI Calculation:**\nInvestment: ${investment:,.2f}\nExpected Return: ${expected_return:,.2f}\nProjected ROI: {roi_percentage:.2f}%"

def format_board_recommendation(department_reports: dict) -> str:
    """
    Skill: Decision Fusion. Combines multiple JSON reports into a single Board Recommendation.
    Used by: Executive Decision Agent.
    """
    markdown = "# Executive Board Recommendation\n\n"
    markdown += "## Department Breakdown\n"
    
    for dept, report in department_reports.items():
        markdown += f"### {dept.capitalize()} Perspective\n"
        markdown += f"{report}\n\n"
        
    markdown += "---\n## Final Verdict\n"
    markdown += "*(Synthesized by Executive Agent based on above reports)*"
    
    return markdown
