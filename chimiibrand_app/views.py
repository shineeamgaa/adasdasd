from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ChimiibrandBE.settings import *
# Create your views here.
@csrf_exempt
def clothdetails(request):
    if request.method == 'POST':
        action = 'clothdetails'
        con = connectDB()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM t_cloth")
        results = cursor.fetchall()
        cursor.close()
        column_names = [desc[0] for desc in cursor.description]
        data=[]
        for row in results:
            row_dict = dict(zip(column_names, row))
            data.append(row_dict)
        return sendresponse(200, 'Successfully',data, action)
@csrf_exempt
def login(request):
    if request.method == 'POST':
        action = 'login'
        jsond = json.loads(request.body)
        username = jsond.get('username')
        password = jsond.get('password')
        con = connectDB()
        cursor = con.cursor()
        cursor.execute(f"""SELECT * FROM t_user WHERE username = '{username}' AND password = '{password}'""")
        row = cursor.fetchone()
        if row:
            username = row
            data = [{
                "username":username
            }]
            return sendresponse(200,"Success", data, action)
        return sendresponse(404, "User not found", "")


