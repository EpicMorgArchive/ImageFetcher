var csrftoken = $.cookie('csrftoken');
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
function progress()