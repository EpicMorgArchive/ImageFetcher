function fetchData(){
	$.ajax ({
        type: "GET",
        url: 'progress',
        dataType: 'json',
        async: false,
        data: { "timestamp": window.timestamp, "pageid" : window.pageid },
        success: function (data) {
         window.data = data;
        }
    });
}
function startProgress() {
	window.setTimeout(progress(), window.check_interval);
}
function progress() {
	alert ('Progress started');
	if (!fetch_running){
		alert ('Condition success');
		fetch_running = true;
		if(window.status < 2){
			fetchData();
			if (window.data["result"]==="ok")
				alert('Data ok');
			else
				alert('Data error');
		}
		fetch_running = false;
		alert ('Progress exited');
		window.setTimeout(progress(), window.check_interval);
	}
}