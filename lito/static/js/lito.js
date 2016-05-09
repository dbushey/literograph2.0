var map;
var story_points_list; 
var story_pk = 0;

 $(document).ready(function() {

  // Get the story ID from HTML
  story_pk = $("#story_data").attr("pk");

  // Use the story PK to get JSON for this story!

  $.getJSON('/story_points_json/' + story_pk + '/', function(jd) {
    story_points_json = jd;
    var story_points = JSON.parse( story_points_json );
    for (i = 0; i < story_points.length; i++) { 
      var x = story_points[i].fields.location_name;
    }
    story_points_list = story_points;

  initialize_map(story_points);
  
  });

  //google.maps.event.addDomListener(window, 'load', initialize);

});

function initialize_map(story_points) {
  console.log("creating map");
  /*
  TODO:
    * Set the map to load centered at the latitude an longitude 
      of the first story point
    * Build a marker for each storypoint

  */
  
  var center_lat = parseFloat(story_points[0].fields.latitude);
  var center_lng = parseFloat(story_points[0].fields.longitude);
  var map = new google.maps.Map(document.getElementById("map"), {
      center: {lat: center_lat, lng: center_lng},
      zoom: 12
    });
  var infowindow = new google.maps.InfoWindow();

  var bounds = new google.maps.LatLngBounds();

  for (i = 0; i < story_points.length; i++) { 
    var lat = parseFloat(story_points[i].fields.latitude);
    var lng = parseFloat(story_points[i].fields.longitude);
    var title = story_points[i].fields.title;
    var loc_name = story_points[i].fields.location_name;
    var text = story_points[i].fields.text;
    var num = story_points[i].fields.num_order;

    var contentString = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h1 id="firstHeading" class="firstHeading">' + loc_name + '</h1>'+
      '<h2 id="secondHeading" class="secondHeading">' + title + '</h2>'+
      '<div id="bodyContent">'+
      '<p>' + text + '</p>'+
      '</div>'+
      '</div>';

    var marker = new google.maps.Marker({
      position: {lat: lat, lng: lng},
      map: map,
      animation: google.maps.Animation.DROP,
      contentString: contentString,
      icon: '//chart.apis.google.com/chart?chst=d_map_pin_letter&chld=' + num + '|FE6256|000000'
    });
    
    marker.setValues({type: "point", id: num});
    

    bounds.extend(marker.getPosition());

    /*google.maps.event.addListener(marker, 'click', function() { 
        //infowindow.setContent(this.contentString);
        //infowindow.open(map,this);
        console.log(marker);
        $('.scrollable').scrollTo($('#7'),1500);
    });*/

    attachListener(marker, num);

  };

  map.fitBounds(bounds);

}

function attachListener(marker, num) {
  marker.addListener('click', function() {
        console.log(num);
        $('.scrollable').scrollTo($('#' + num),1500);
  });
}