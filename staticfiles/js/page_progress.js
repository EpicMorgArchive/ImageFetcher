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
	setTimeout(progress, 0);
}
function dbgOut(message) {
	console.log(message);
}
//update loop
function progress() {
	if (progress_enabled) {
		dbgOut ('Progress started');
		if (!fetch_running){
			dbgOut ('Condition success');
			fetch_running = true;
			if(window.status < 2){
				fetchData();
				try
				{
					if (window.data["result"]==="ok")
						dbgOut('Data ok');
					else
						dbgOut('Data error');
				}
				catch(e) {
					dbgOut('JSON error');
				}
			}
			fetch_running = false;
			dbgOut ('Progress exited');
			setTimeout(progress, window.check_interval);
		}
	}
}