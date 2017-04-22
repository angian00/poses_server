var currTime;
var timer;

function startCountdown() {
	var timeStr = findGetParameter("time");
	if (timeStr == null)
		return;

	var timeAmount = parseInt(timeStr);
	if (isNaN(timeAmount))
		return;

	currTime = timeAmount;
	document.getElementById('timeText').classList.remove("blinking");
	updateTimeText();

	timer = setInterval(function() {
		currTime = currTime - 1;

		if (currTime >= 0) {
			updateTimeText();
		} else {
			clearInterval(timer);
			document.getElementById("timeText").innerHTML = "TIMER EXPIRED";
			document.getElementById('timeText').classList.add("blinking");
			playSound();
		}
	}, 1000);
}


function findGetParameter(paramName) {
    var result = null, tmp = [];
    location.search.substr(1)
        .split("&")
        .forEach(function (item) {
        tmp = item.split("=");
        if (tmp[0] === paramName) result = decodeURIComponent(tmp[1]);
    });

    return result;
}


function updateTimeText() {
	var mins = Math.floor(currTime / 60);
	var secs = currTime % 60;
	document.getElementById('timeText').innerHTML = zeropad(mins) + ":" + zeropad(secs);
}

function zeropad(num) {
	var str = "" + num;
	var pad = "00";
	return pad.substring(0, pad.length - str.length) + str;
}


function playSound() {
  	var audio = new Audio('/stop.mp3');
	audio.play();
}
