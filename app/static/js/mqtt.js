$(document).ready(function () {

    var socket = io.connect('http://' + document.domain + ':' + location.port);

    var topic = 'house/thermometers/#';
    var qos = 0;
    var data = '{"topic": "' + topic + '", "qos": ' + qos + '}';
    socket.emit('subscribe', data = data);

    socket.on('mqtt_message', function (data) {
        console.log(data);

        var topic = data['topic'].replace(/\//g, '-');
        var retained = data['retained'];
        var payload = JSON.parse(data['payload']);
        var temperature = payload.temperature_C;
        var humidity = payload.humidity;

        $temperature = $('#' + topic);
        $temperature.text(temperature);
        $temperature.append('<span class="temperature-units">&#8239;°C</span>');

        $temperature = $('#' + topic + '-humidity');
        $temperature.text(humidity);
        $temperature.append('<span class="humidity-units">&#8239;%</span>');

        $retained = $('#' + topic + '-retained .glyphicon-time' );
        if (retained === 0) {
            $retained.hide();
        }

    })

});