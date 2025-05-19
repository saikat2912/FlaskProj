from flask import Blueprint,request, jsonify, render_template_string

api_users = Blueprint('api_users', __name__, url_prefix='/api/users')

@api_users.route('/', methods=['GET'])
def get_users():
    return jsonify([
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ])

@api_users.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        message = request.form.get('message','No message')
        return render_template_string('<h1>You submitted :<hr/> {{message}}</h1>',message= message)
    else:
        return '''
        <form method="post" action="/api/users/submit">
        <input type="text" name="message" placeholder="Enter a message" />
        <input type="submit"/>
        </form>
        '''
