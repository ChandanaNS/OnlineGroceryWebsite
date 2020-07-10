// Initialize the platform object:
$(document).ready(function(){
    console.log(data)
    if(data == undefined || data == null || (Object.values(data) > -1)){
        data = {data: {}, api_key: "oILvnb3yIsakFmQI-UJafpCXmRvN4INE2EZSwgt0R8s", latitude: 13.34004, longitude: 77.10151}
    }
    var platform = new H.service.Platform({
    'apikey': data['api_key']
    });
	const lng = data['longitude'];
	const lat = data['latitude'];
// Obtain the default map types from the platform object
	var defaultLayers = platform.createDefaultLayers();

// Instantiate (and display) a map object:
var map = new H.Map(
    document.getElementById('mapContainer'),
    defaultLayers.vector.normal.map,
    {
      zoom: 10,
      center: { lat: lat, lng: lng }
    });

	const marker = new H.map.Marker({lat: lat, lng: lng});
	map.addObject(marker);

    if(data['postAction']== 'submit'){

        $('.FullName, .PhoneNumber, .Email, .location, .search,.address, .addressLine,.newAddress,.placeOrder, .confirm').toggleClass('displayNone');
        address = data['data'].items[0].address;
        var templateString = 'Your item will be delivered to '+
        data['address'] +
        ', '+ address.city +', '+ address.county +', '+ address.countryName + ', '+ address.postalCode;
         $(".addressLine").html(templateString);



    }

});
