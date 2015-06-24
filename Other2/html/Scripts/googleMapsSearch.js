var map;
var service;
var infowindow;

navigator.geolocation.getCurrentPosition(showPosition);

function showPosition(position) {
	initialize(position.coords.latitude,position.coords.longitude);
	window.myLatitude = position.coords.latitude;
	window.myLongitude = position.coords.longitude;
}

function initialize(latitude,longitude) {
	console.log(latitude);
	var location = new google.maps.LatLng(latitude,longitude);

	map = new google.maps.Map(document.getElementById('map'), {
		center: location,
		zoom: 15
	});
	service = new google.maps.places.PlacesService(map);

}
	
function search(query) {
	var request = {
		// location: new google.maps.LatLng(window.myLatitude,window.myLongitude),
		radius: '500',
		query: query
	};

	service = new google.maps.places.PlacesService(map);
	service.textSearch(request, callback);
}

function callback(results, status) {
	if (status == google.maps.places.PlacesServiceStatus.OK) {
		for (var i = 0; i < results.length; i++) {
			var place = results[i];
			createMarker(results[i]);
		}
	}
}

function createMarker(place) {
	console.log(place);
	var marker = new google.maps.Marker({
		map: map,
		position: place.geometry.location,
		title: place.name
	});
}


$(document).ready(function(){
	$("#enterSearch").click(function(){
			search($("#inputGoogleSearch").val());
	});
});