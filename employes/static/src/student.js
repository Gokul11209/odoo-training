console.log("goooooooooookkkkkkkkkkkkuuuuuuuuuuulllllllllll")
odoo.define('employes.student_report', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
var core = require('web.core');
var _t = core._t;

var timeout;

publicWidget.registry.addValue = publicWidget.Widget.extend({

    selector: '.student_value_con',

    events: {
        'click .addValueBtn': '_onstudentReport',
    },

    _onstudentReport:function(ev){
    var name =$("input[name='name']").val();
    var country_id = $(".country_id option:selected").data('country-id');
    var state_id = $(".state_id option:selected").data('state-id');
    var phone =$("input[name='phone']").val();
    console.log(name)
    console.log(country_id)
    console.log(state_id)


    this._rpc({
        route:'/student/env',
        params: {
                name:name,
                country:country_id,
                state:state_id
                phone:phone
            },})
//        }).then(function (data) {
////            data  received from python
//            console.log("gokulllllllllllllllllllllllllllll")
//            $("input[name='name']").val(data['name'])
//
//        });


    }

});

});













