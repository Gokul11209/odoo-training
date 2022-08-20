from odoo import http
from odoo.http import request
import requests
import json



class Employes(http.Controller):

    @http.route('/academy/academy', auth='public')
    def index(self, **kw):
        return "Hello, World"

    @http.route('/academy', auth='public', website=True)
    def list(self, **kw):
        # return "hiii gokul"

        return request.render('employes.add_value', {})


    @http.route('/result/ans',type='json',website=True)
    def add_value_sum(self, **kw):
        print('summmmmmmmmmmmmmmmmmmmmm', kw)
        num1 = kw.get('num1')
        num2 = kw.get('num2')
        sum = num1 + num2
        print('summmmmmmmmmmmmmmmmmmmmm', sum)
        return {'sum':sum}

    @http.route('/descripiton',type='http',auth='public',website=True)
    def descripition_page(self,**kw):
        return request.render("employes.descripition",{})



    @http.route("/weather",type='http',auth='public',website=True)
    def Weather_report(self,**kw):
        return request.render("employes.weather_template",{})

    @http.route('/weather/result', type='json', website=True)
    def add_value_sum(self, **kw):
        print('cityyyyyyyyyyyyyy', kw)
        city = kw.get('val')
        url = F"http://api.weatherapi.com/v1/current.json?key=0b15e0847b8a400bb87133910220808&q={city}&aqi=no&dt=2022-08-09"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        dict =json.loads(response.text)
        print(response.text)
        weather_dt ={
            'name': dict['location']['name'],
            'region': dict['location']['region'],
            'country': dict['location']['country'],
            'continent': dict['location']['tz_id'],
            'time': dict['location']['localtime'],
            'lat': dict['location']['lat'],
            'lon': dict['location']['lon'],
            'temp_c': dict['current']['temp_c'],
            'temp_f': dict['current']['temp_f'],
            'text': dict['current']['condition']['text'],
            'wind_spped': dict['current']['wind_kph'],
            'pressure': dict['current']['pressure_in'],
            'humidity': dict['current']['humidity']
        }
        print(weather_dt)
        return weather_dt





    @http.route("/create/student", type='http', auth='public', website=True)
    def Weather_report(self, **kwargs):
        return request.render("employes.student_info", {
            'country': request.env['res.country'].search([]),
            'state': request.env['res.country.state'].search([]),
        })

    @http.route('/weather/information', auth='public', website=True)
    def list(self, **kw):
        return request.render('employes.listing', {
            'objects': request.env['res.partner'].search([]),

        })

    @http.route('/student/env', type='json', website=True)
    def gokull(self,**kw):
        print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii",kw)

        name = kw.get('name')
        email = kw.get('country')
        phone = kw.get('state')
        state = kw.get('phone')
        request.env['res.partner'].sudo().create({
            'name': name,
            'phone': phone,
            'email': email,
            'state_id': state,
        })













