odoo.define('employes.weather', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
var core = require('web.core');
var _t = core._t;

var timeout;


publicWidget.registry.addValue = publicWidget.Widget.extend({

    selector: '.weather_summit_btn',

    events: {
        'click .addValueBtn': '_onweatherReport',
    },

    _onweatherReport:function(ev){
    var city =$("input[name='city']").val();
    console.log(city)

    this._rpc({
        route:'/weather/result',
        params: {
                val:city,
            },
        }).then(function (data) {
//            data  received from python
            console.log("gokulllllllllllllllllllllllllllll")
            $("input[name='name']").val(data['name'])
            $("input[name='region']").val(data['region'])
            $("input[name='country']").val(data['country'])
            $("input[name='conti']").val(data['continent'])
            $("input[name='time']").val(data['time'])
            $("input[name='cloud']").val(data['text'])
            $("input[name='lat']").val(data['lat'])
            $("input[name='lon']").val(data['lon'])
            $("input[name='wind']").val(data['wind_spped'])
            $("input[name='pressure']").val(data['pressure'])
            $("input[name='humdity']").val(data['humidity'])
            $("input[name='cel']").val(data['temp_c'])
            $("input[name='far']").val(data['temp_f'])
        });


    }

});

});













