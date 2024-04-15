import jinja2
import pdfkit
from datetime import datetime

#html template!!
name = input("What student full name and surname ")
about = input("Tell us about yourself ")
skills = input("Your skills ")
qualification = input("Qualification ")
employment_history = input("Employment history ")
achievements = input("Acheivements ")
school =  input("Which academy are you currently attending? ")
current_date = datetime.today().strftime("%d %b, %Y")

#CREATING DICTIONARY - attempting to link the variables recieved from the user to the html
#key is the html while values is whats on the python file
context = {"name" : name ,
            "about" :about,
            "skills"   : skills,
            "qualification" : qualification,
            "employment_history" : employment_history, 
            "school" : school,
            "current_date" : current_date}

#xreating an envirnoment that can accomodate hmtl using jinja2 (to create hmtl. xml that are returned to the user via http response)
#loader =  where the hmtl document located
template_loader = jinja2.FileSystemLoader('./') #print out the location of the file
template_env = jinja2.Environment(loader= template_loader)

template = template_env.get_template("template.html")
output = template.render(context)

config = pdfkit.configuration(wkhtmltopdf= "/usr/bin/wkhtmltopdf")
pdfkit.from_string(output, "pdf_generated.pdf", configuration=config)