function LoadProgress(){
    $.post({
	  dataType: "json",
	  url: './progress',
	  data: { timestamp: timestamp, pageid: pageid }
	  success: (function(data){
		window.fetchedinfo = data;
	  })
	});
}