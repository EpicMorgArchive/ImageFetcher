function fetchData(){
	$.ajax ({
        type: 'GET',
        url: 'progress',
        dataType: 'json',
        async: false,
        data: { 'timestamp': window.Timestamp, 'pageid' : window.PageID },
        success: function (data) {
         //process
		 window.data = data;
        }
    });
}
//removeClassIfExists
function rCIF(element, classname) {
	if (element.hasClass(classname))
		return element.removeClass(classname)
}
//addClassIfNotExists
function aCINF(element, classname) {
	if (!element.hasClass(classname))
		return element.addClass(classname)
}
//mpc - main progress container, mpb - main progress bar
//progressBarShowZero
function pBSZ(mpc, mpb){
	aCINF(mpc,s_pcss);
	rCIF(mpb, s_pbss);
	rCIF(mpb, s_pbds);
	aCINF(mpb,s_pbis);
	mpb.width(mpc.width());
}
//mpc - main progress container, mpb - main progress bar
//progressBarShowWIN
function pBSW(mpc, mpb){
	rCIF(mpc,s_pcss);
	rCIF(mpb, s_pbis);
	rCIF(mpb, s_pbds);
	aCINF(mpb,s_pbss);
	mpb.width(mpc.width());
}
//mpc - main progress container, mpb - main progress bar
//progressBarShowError
function pBSE(mpc, mpb){
	rCIF(mpc,s_pcss);
	rCIF(mpb, s_pbis);
	rCIF(mpb,s_pbss);
	aCINF(mpb, s_pbds);
	mpb.width(mpc.width());
}
function progressBarUpdate(){
	if (window.e_pr) {
		dbgOut('Progressbar update began');
		if (window.data !== undefined){
			var pageinfo = window.data["page"];
			var ready = parseInt(pageinfo['ready']);
			var total = parseInt(pageinfo['total']);
			var status = parseInt(pageinfo['status']);
			dbgOut('Progress render start');
			
			var mpc = $('#mpc');
			var mpb = $('#mpb');
			
			switch(status) {
				case 0:
					pBSZ(mpc,mpb);
					break;
				case 1:
					if (total>0){
						mpb.width(mpc.width()*ready/total);
						if (ready == total){
							e_pr = false;
							pBSW(mpc, mpb);
						}
						else {
							rCIF(mpc, s_pcss);
							rCIF(mpb, s_pbss);
							rCIF(mpb, s_pbds);
							aCINF(mpb,s_pbis);
						}
					}
					else {
						pBSZ(mpc,mpb);
					}
					dbgOut('Progress bar updated');
					break;
					break;
				case 2:
					e_pr = false;
					pBSW(mpc, mpb);
					break;
				case 3:
				case 4:
					e_pr = false;
					pBSE(mpc, mpb);
					break;

			}
			dbgOut('Progress render complete');
		}
	}	
}
function startProgress() {
	setTimeout(progress, 0);
}
function dbgOut(message) {
	if (e_vb) {
		console.log(message);
	}
}
//update loop
function progress() {
	if (window.e_pf) {
		dbgOut ('Progress started');
		if (!window.FetchRunning){
			dbgOut ('Condition success');
			window.FetchRunning = true;
			if(window.status < 2){
				fetchData();
				try
				{
					if (window.data['result']==='ok')
						dbgOut('Data ok');
					else
						dbgOut('Data error');
				}
				catch(e) {
					dbgOut('JSON error');
				}
			}
			window.FetchRunning = false;
			dbgOut ('Progress exited');
		}
	}
	setTimeout(progress, window.CheckInterval);
}