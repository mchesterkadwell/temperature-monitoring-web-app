$(document).ready(function () {

    var socket = io.connect('http://' + document.domain + ':' + location.port);

    var topic = 'house/thermometers/#';
    var qos = 0;
    var data = '{"topic": "' + topic + '", "qos": ' + qos + '}';
    socket.emit('subscribe', data = data);

    socket.on('mqtt_message', function (data) {
        var topic = data['topic'].replace(/\//g, '-');
        var payload = JSON.parse(data['payload']);
        var temperature = payload.temperature_C;
        $('#' + topic).text(temperature + ' °C');
    })

});