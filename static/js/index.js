function initMap(){

  // Initializing variables to be used
  var all_overlays = []
  var coordinatesArray = [];
  var selectedShape
  var map;
  var options;
  var markers;

  // For the shapes
  function clearSelection() {
    if (selectedShape) {
      selectedShape.setEditable(false);
      selectedShape = null;
    }
  }

  function setSelection(shape) {
    clearSelection();
    selectedShape = shape;
    shape.setEditable(true);

  }




  function deleteSelectedShape() {
    if (selectedShape) {
      selectedShape.setMap(null);
    }
  }

  function deleteAllShape() {
    for (var i = 0; i < all_overlays.length; i++) {
      all_overlays[i].overlay.setMap(null);
    }
    all_overlays = [];
  
  /*  
    $.ajax({
      type: 'DELETE',
      url: "/deleteallshapes",
    })*/
  }

  
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 10,
      center: new google.maps.LatLng(37.7694, -122.4862), //37.7694° N, 122.4862° W
      mapTypeId: google.maps.MapTypeId.ROADMAP,
      disableDefaultUI: true,
      zoomControl: true
    });
  
    var polyOptions = {
      strokeWeight: 0,
      fillOpacity: 0.45,
      editable: true
    };
    // Creates a drawing manager attached to the map that allows the user to draw
    // markers, lines, and shapes.
    drawingManager = new google.maps.drawing.DrawingManager({
      drawingMode: google.maps.drawing.OverlayType.POLYGON,
      markerOptions: {
        draggable: true
      },
      polylineOptions: {
        editable: true
      },
      rectangleOptions: polyOptions,
      circleOptions: polyOptions,
      polygonOptions: polyOptions,
      map: map
    });

  
    google.maps.event.addListener(drawingManager, 'overlaycomplete', function(e) {
      all_overlays.push(e);
      if (e.type != google.maps.drawing.OverlayType.MARKER) {
        // Switch back to non-drawing mode after drawing a shape.
        drawingManager.setDrawingMode(null);
  
        // Add an event listener that selects the newly-drawn shape when the user
        // mouses down on it.
        var newShape = e.overlay;
        newShape.type = e.type;


        var bounds = e.overlay.getBounds();
        var start = bounds.getNorthEast();
        var end = bounds.getSouthWest();

        const testcoordNE = start.toJSON(); 
        const testcoordSW = end.toJSON();

        $.ajax({
          type: 'POST',
          url: "/save",
          data: {
          //'data': JSON.stringify(data),
          'testcoordNE': testcoordNE,
          'testcoordSW': testcoordSW
          },
        })
        google.maps.event.addListener(newShape, 'click', function() {
          setSelection(newShape);
        });
        setSelection(newShape);
      }
    });
  
    // Clear the current selection when the drawing mode is changed, or when the
    // map is clicked.
    google.maps.event.addListener(drawingManager, 'drawingmode_changed', clearSelection);
    google.maps.event.addListener(map, 'click', clearSelection);
    google.maps.event.addDomListener(document.getElementById('delete-button'), 'click', deleteSelectedShape);
    google.maps.event.addDomListener(document.getElementById('delete-all-button'), 'click', deleteAllShape);

  };


  // Listen for click and add marker 
  google.maps.event.addListener(map, 'click', function(event){
  // Add marker
  addMarker({coords:event.latLng});
  });
  

  // Store map coordinates for polygons
  // read this for tomorrow https://stackoverflow.com/questions/32899213/getting-coordinates-of-rectangle-polygon-when-drawn-on-google-maps-with-drawing/32902755
  // google.maps.event.addListener(drawMgr, 'overlaycomplete', function(overlay) {
  // //alert("Created Box!");

  //   // rectangle = overlay;

  //   // var bounds = overlay.overlay.getBounds();
  //   // var start = bounds.getNorthEast();
  //   // var end = bounds.getSouthWest();

  //   // const testcoordNE = start.toJSON(); 
    // const testcoordSW = end.toJSON();
    // const data = {testcoordNE, testcoordSW};
    
    // console.log(test);

    // var test = {'name': "jowi" }
    // $.ajax({
    //   type: 'POST',
    //   url: "/save",
    //   data: {
    //     //'data': JSON.stringify(data),
    //     'testcoordNE': testcoordNE,
    //     'testcoordSW': testcoordSW
  //   //   },
  //   // })
  // });