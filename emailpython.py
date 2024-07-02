import smtplib
from email.mime.text import MIMEText

# Configuration
sysadmin_email = 'guillaume777@yahoo.com'
subject = 'Rapport concernant le CPU du serveur'

# Get system information
memory_usage = round(100 * (memory_get_usage() / memory_get_peak_usage()), 2)
cpu_usage = round(100 - (float(os.popen('grep "cpu " /proc/stat | awk "{print $5/$2*100}"').read().strip())), 2)
disk_free = round(100 * shutil.disk_usage('/').free / shutil.disk_usage('/').total, 2)

# Prepare email body
body = "Server Performance Report:\n"
body += f"Memory Usage: {memory_usage}%\n"
body += f"CPU Usage: {cpu_usage}%\n"
body += f"Disk Space Available: {disk_free}%\n"

# Create email message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = 'guillaume777@yahoo.com'
msg['To'] = sysadmin_email

# Send email with smtplib
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@example.com', 'your_password')
        smtp.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
    
    
    
    
    
    
    
import psutil
from email.mime.text import MIMEText
import smtplib

# Configuration
sysadmin_email = 'nganongoguillaume@gmail.com'
subject = 'Server Performance Report'

# Get system information
memory_usage = round(100 * (psutil.virtual_memory().used / psutil.virtual_memory().total), 2)
cpu_usage = round(100 - psutil.cpu_percent(interval=1), 2)
disk_free = round(100 * psutil.disk_usage('/').free / psutil.disk_usage('/').total, 2)

# Prepare email body
body = "Server Performance Report:\n"
body += f"Memory Usage: {memory_usage}%\n"
body += f"CPU Usage: {cpu_usage}%\n"
body += f"Disk Space Available: {disk_free}%\n"

# Create email message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = 'nganongoguillaume@gmail.com'
msg['To'] = sysadmin_email

# Send email with smtplib
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('nganongoguillaume@gmail.com', 'Vilhelmo7')
        smtp.send_message(msg)
        #smtp.sendmail('nganongoguillaume@gmail.com','nganongoguillaume@gmail.com',"Eureka, sa marche!!")
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
