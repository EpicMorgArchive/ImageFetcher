//Helpers

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
//debug output
function dbgOut(message) {
    if (e_vb) {
        console.log(message);
    }
}

//wrapper
function startProgress() {
    setTimeout(updateProgressInfo, 0);
}
//Progress bar helpers

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
            var ready = pageinfo['ready'];
            var total = pageinfo['total'];
            dbgOut('Progress render start');
            
            var mpc = $('#mpc');
            var mpb = $('#mpb');
            
            switch(window.Status) {
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

function addImage(image, imgc) {
    //imgc.append(
	dbgOut('Appending image');
	var tmp_imgurl = image['status']==2?window.images_url+image['imageid'].toString()+image['ext']:image['url'];
	dbgOut(tmp_imgurl);
	var str = '<a href="'+tmp_imgurl+'">'+'<img src="'+tmp_imgurl+'"></img>'+'</a>';
	dbgOut(str);
	imgc.append(str);
}

function addImages(images) {
    var cnt = images.length;
    var tmp = null;
    var imgc = $('#imglst');
    for (var i=0; i<cnt; i++) {
        addImage(images[i], imgc);
    }
}

//process progress data
function processUpdateInfo(data){
    try
    {
        if (data['result']!=='ok') {
            dbgOut('Data error');
            return;
        }
        dbgOut('Data ok');
        window.Status = data['page']['status'];
        window.Timestamp = data['timestamp'];
        addImages(data['images'])
    }
    catch(e) {
        dbgOut('JSON error');
    }
}

//fetch progress data
function fetchData(){
    $.ajax ({
        type: 'GET',
        url: 'progress',
        dataType: 'json',
        async: false,
        data: {
            'timestamp': window.Timestamp,
            'pageid' : window.PageID
        },
        success: function (data) {
            window.data = data;
            processUpdateInfo(data);
        }
    });
}

//update loop
function updateProgressInfo() {
    if (window.e_pf) {
        dbgOut ('Progress started');
        if (!window.FetchRunning){
            dbgOut ('Condition success');
            window.FetchRunning = true;
            fetchData();
            if(window.Status >= 2) {
                window.e_pf = false;
                dbgOut('Progress fetch stopped(no need in it)');
            }
            window.FetchRunning = false;
            dbgOut ('Progress exited');
        }
    }
    setTimeout(updateProgressInfo, window.CheckInterval);
}

