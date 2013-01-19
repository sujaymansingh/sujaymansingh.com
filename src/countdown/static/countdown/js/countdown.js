var countdown_startTime;
var countdown_endTime;
var countdown_callback;
var lastUpdateMilliSeconds;

function countdown_init(startTimeStr, endTimeStr, callback) {
 
    countdown_startTime = moment(startTimeStr);
    countdown_endTime = moment(endTimeStr);
    countdown_callback = callback;
    countdown_update();
}


function pad(num, size) {
    var s = num+"";
    while (s.length < size) s = "0" + s;
    return s;
}


function countdown_update() {

    // How many ms since the last time we checked?
    var currentMilliSeconds = moment().valueOf();
    var deltaMilliSeconds = currentMilliSeconds - lastUpdateMilliSeconds;

    lastUpdateMilliSeconds = currentMilliSeconds;

    var time = countdown_startTime.add('milliseconds', deltaMilliSeconds);
    var x = countdown_endTime.diff(time);

    var msInSeconds = 1000;
    var msInMinute = 1000 * 60;
    var msInHour = 1000 * 60 * 60;
    var msInDay = 1000 * 60 * 60 * 24;

    var days = x / msInDay;
    x = x % msInDay;

    var hours = x / msInHour;
    x = x % msInHour;

    var minutes = x / msInMinute;
    x = x % msInMinute;

    var seconds = x / msInSeconds;
    x = x % msInSeconds;

    countdown_callback(
        Math.floor(days),
        pad(Math.floor(hours), 2),
        pad(Math.floor(minutes), 2),
        pad(Math.floor(seconds), 2)
    );

    window.setTimeout(countdown_update, 200);
}
