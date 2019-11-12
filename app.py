from flask import Flask, render_template, request

app = Flask(__name__)

@ app.route('/')
def index():
   #Renders the home page with link to Fortune page.
   return render_template('index.html')

@app.route('/fortune')
def fortune():
   return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
   gender_input = request.args.get('gender')
   
   if gender_input == 'male':
      fortune = "In the Summer you will meet a new friend"

   elif gender_input == 'female':
      fortune =  "This year will be a year of good changes for you..."

   elif gender_input == 'none':
      fortune = "This year a business oppurtunity will arise for you"

   elif gender_input == 'other':
      fortune = "In the next two weeks a gift will arrive for you"
   
   else:
      fortune = "you have no luck coming up"

   return render_template('fortune_results.html', fortune=fortune)