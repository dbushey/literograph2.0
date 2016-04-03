function initialize() {
        var myLatlng = new google.maps.LatLng(40.784019, -73.965398)
        var image = "/static/img/icon_2249_small.png"
        var mapOptions = {
          center: myLatlng,
          zoom: 12
        };

         var contentString = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h1 id="firstHeading" class="firstHeading">Central Park</h1>'+
      '<div id="bodyContent">'+
      '<p><b>(Central Park</b> is an urban park in Manhattan in New York City.)'+
      //'<p>Attribution: Central Park, <a href="http://en.wikipedia.org/wiki/Central_Park">'+
      //'http://en.wikipedia.org/wiki/Central_Park</a> '+
      //'(last visited June 22, 2009).</p>'+
      '</p>'+
      '<p>' +
        " I spread the map out on the dining room table, and I held down the corners with cans of V8. The dots from where I'd found things looked like the stars in the universe. I connected them, like an astrologer, and if you squinted your eyes like a Chineseperson, it kind of looked like the word 'fragile.' Fragile. What was fragile? Was <a href> Central Park </a> fragile? Was nature fragile? Were the things I found fragile? A thumbtack isn't fragile. Is a bent spoon fragile? I erased, and connected the dots in a different way, to make 'door.'" +
        '</p>' +
        '<p><a href> Continue reading... </a>' +
        '</p>' +
      
      
      '</div>'+
      '</div>';

        var infowindow = new google.maps.InfoWindow({
          content: contentString
        });



        var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);

        var marker = new google.maps.Marker({
          position: myLatlng,
          map: map,
          animation: google.maps.Animation.DROP,
          icon: image,
          draggable: true,
          title:"Central Park"
        });

        var marker2 = new google.maps.Marker({
          position: new google.maps.LatLng(40.711893, -74.013591),
          map: map,
          animation: google.maps.Animation.DROP,
          icon: image,
          draggable: true,
          title:"WTC"
        });

        var marker3 = new google.maps.Marker({
          position: new google.maps.LatLng(40.851251, -73.877004),
          map: map,
          animation: google.maps.Animation.DROP,
          icon: image,
          draggable: true,
          title:"Bronx Zoo"
        });

        google.maps.event.addListener(marker, 'click', function() {
            infowindow.open(map,marker);
            $('#moretext').removeClass('hidden');
          });
        google.maps.event.addListener(infowindow,'closeclick',function(){
            $('#moretext').addClass('hidden')
          });
      }
      google.maps.event.addDomListener(window, 'load', initialize);