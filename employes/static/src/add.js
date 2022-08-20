
odoo.define('employes.add', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
var core = require('web.core');
var _t = core._t;

var timeout;

publicWidget.registry.addValue = publicWidget.Widget.extend({

    selector: '.oe_add_value',

    events: {
        'click .addValueBtn': '_onAddValue',
    },
    _onAddValue: function (ev) {

        var num1 = $("input[name='add1']").val();
        var num2 = $("input[name='add2']").val();
        var elem = document.getElementById('btn_1');
        var txt = elem.textContent || elem.innerText;
        console.log(txt)

        console.log("gokulllllllllll")

        this._rpc({
            route: "/result/ans",
            params: {
                num1: parseInt(num1, 10),
                num2: parseInt(num2, 10),
            },
        }).then(function (data) {
        console.log('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', data)
            $("input[name='sum']").val(data['sum'])
        });

     },
});


return {
    AcademyAddValue: publicWidget.registry.addValue,
};

});





































