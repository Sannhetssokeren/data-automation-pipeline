import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json
import numpy as np  # Добавить эту строку
from .logger import setup_logger

logger = setup_logger('report_generator', 'logs/pipeline.log')

def generate_visualizations(df, output_dir='reports'):
    plt.figure(figsize=(10,6))
    sns.histplot(df.select_dtypes(include=[np.number]).iloc[:, 0])
    plt.title("Distribution of first numeric column")
    plt.savefig(f"{output_dir}/histogram.png")
    plt.close()

    fig = px.scatter(df, x=df.columns[0], y=df.columns[1])
    fig.write_html(f"{output_dir}/scatter_plot.html")
    logger.info("Visualizations generated")

def generate_pdf_report(output_path='reports/report.pdf'):
    c = canvas.Canvas(output_path, pagesize=A4)
    c.drawString(100, 750, "Automated Data Analysis Report")
    c.save()
    logger.info(f"PDF report saved to {output_path}")

def send_email_with_attachment(config, file_path):
    with open("config/config.json") as f:
        cfg = json.load(f)

    msg = MIMEMultipart()
    msg['From'] = cfg['email']['sender_email']
    msg['To'] = cfg['email']['recipient_email']
    msg['Subject'] = "Automated Report"

    body = "Please find the attached report."
    msg.attach(MIMEText(body, 'plain'))

    with open(file_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {file_path.split('/')[-1]}")
        msg.attach(part)

    server = smtplib.SMTP(cfg['email']['smtp_server'], cfg['email']['port'])
    server.starttls()
    server.login(cfg['email']['sender_email'], cfg['email']['sender_password'])
    server.send_message(msg)
    server.quit()
    logger.info("Email sent with attachment")