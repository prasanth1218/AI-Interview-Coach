from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    history,
    average_score,
    readiness_score,
    ai_report
):

    pdf_file = "AI_Interview_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "AI Interview Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            f"Average Score: {average_score}",
            styles["Normal"]
        )
    )

    elements.append(
        Paragraph(
            f"Readiness Score: {readiness_score}%",
            styles["Normal"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            "Interview History",
            styles["Heading2"]
        )
    )

    for item in history:

        elements.append(
            Paragraph(
                f"Question: {item['question']}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Score: {item['score']}/10",
                styles["Normal"]
            )
        )

        elements.append(
            Spacer(1, 6)
        )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            "AI Analysis",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            ai_report,
            styles["Normal"]
        )
    )

    doc.build(elements)

    return pdf_file