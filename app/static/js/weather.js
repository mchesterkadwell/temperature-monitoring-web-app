$(document).ready(function () {

    (function weather_worker() {
        $.get( "/weather", function( data ) {
            // Update the weather panel
            $('#weather').html(data);
            var now = new Date().toLocaleString();
            console.log("Weather requested: " + now);
        })
          .done(function() {
              // Fetch weather again in 15 minutes
              setTimeout(weather_worker, 900000);
          })
          .fail(function() {
              setTimeout(weather_worker, 60000);
              console.log("Weather request failed. Trying again in 1 minute.");
          });
    })();

});