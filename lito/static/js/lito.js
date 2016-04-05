var map;
var story_points_debug; 

 $(document).ready(function() {

  $.getJSON('/story_points_json', function(jd) {

    console.log(jd);

    story_points_json = jd;

    var story_points = JSON.parse( story_points_json );

    for (i = 0; i < story_points.length; i++) { 
      var x = story_points[i].fields.location_name;
      console.log(x);
    }

    story_points_debug = story_points;

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

}



      