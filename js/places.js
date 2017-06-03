// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
//<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDH1YrWFskgNklcR8GF_Ki2gyq4VTITZ-A&libraries=places">
var map;
var userRadius = 12000;
var infowindow;
var service;
var userKeyword = 'livemusic'; // Can be updated by index.html: id="venueSearch"
var locationFound = true;
var coordinates = new Array(2); //coordinates[0] == latitude: coordinates[1] == longitude

function initialize() {
  var center;

  if (locationFound) {
    center = new google.maps.LatLng(coordinates[0], coordinates[1]);
  } else {
    center = new google.maps.LatLng(38.9431697, -95.2748186);
  }
  //var center = new google.maps.LatLng(parseFloat(coordinates[0]), parseFloat(coordinates[1]));
  map = new google.maps.Map(document.getElementById('map'), {
    center: center,
    zoom: 10

  });

  var request = {
    location: center,
    radius: userRadius,
    keyword: [userKeyword]
  };

  service = new google.maps.places.PlacesService(map);



  service.nearbySearch(request, callback);



}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(setLocation, showLocationError);
  } else {
    console.log("Geolocation is not supported by this browser.\n");
  }
}

function setLocation(position) {
  coordinates[0] = position.coords.latitude;
  coordinates[1] = position.coords.longitude;
  console.log(coordinates[0]); // debug purposes only
  console.log(coordinates[1]); // debug purposes only

  initialize();
}

function showLocationError(error) {

  switch (error.code) {
    case error.PERMISSION_DENIED:
      console.log("User denied the request for Geolocation.");
      break;
    case error.POSITION_UNAVAILABLE:
      console.log("Location information is unavailable.");
      break;
    case error.TIMEOUT:
      console.log("The request to get user location timed out.");
      break;
    case error.UNKNOWN_ERROR:
      console.log("An unknown error occured.")
      break;
  }

  console.log("what")
  locationFound = false;
  initialize();
}

function callback(results, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    for (var i = 0; i < results.length; i++) {
      console.log(results[i].name)
      createMarker(results[i]);
    }
  }
}

function createMarker(place) {


  var request = {
    placeId: place.place_id
  };
  var isAVenue = false;
  service.getDetails(request, function(place, status) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
      //console.log(place.reviews[0].text);

      for (var i = 0; i < place.reviews.length; i++) {

        if (place.reviews[i].text.includes('band') ||
          place.reviews[i].text.includes('live music') ||
          place.reviews[i].text.includes('shows') ||
          place.reviews[i].text.includes('venue')) {

          isAVenue = true;
          console.log(place.reviews[i].text);


        }
      }

      if (isAVenue == true) {
        console.log(place.name);
        var placeLoc = place.geometry.location;
        var marker = new google.maps.Marker({
          map: map,
          position: place.geometry.location
        });

        infowindow = new google.maps.InfoWindow();
        google.maps.event.addListener(marker, 'click', function() {
          infowindow.setContent('<div><strong>' + place.name + '</strong><br>' +
            'Place ID: ' + place.place_id + '<br>' +
            place.formatted_address + '</div>');
          infowindow.open(map, this);
        });
        console.log(place);
      }
    }
  });

}
