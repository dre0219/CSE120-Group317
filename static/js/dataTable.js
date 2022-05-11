var resulttable;
var searchtable;

$(document).ready(function () {
  resulttable = $('#datas').DataTable({
    "language": {
      "emptyTable": "To get started, draw a rectangle/rectangles on the map and click refresh"
    },
    columns: [
      { data: 'name' },
      { data: 'address' }
    ], 
    scrollY: "310px",
    scrollCollapse: true
  });


  searchtable = $('#searches').DataTable({
    ajax: {
      type: 'GET',
      url: '/test/searchtables'
    },
    "autoWidth": false,

    columns: [
      { 'data': 'composite_id' },
      { 'data': 'composite_name' },
      { 'data': 'user_id' },
      {
        'data': null,
        orderable: false,
        "render": function (data, type, full) {
          return '<div> <a href="/load> <button class="button small"> <i class="material-icons small">file_upload</i> <span class="button-text"> Load </span> </button> </a> </div>';
        }
      }
    ], 
    scrollY: "310px",
    scrollCollapse: true
  });
});


function refreshTable() {
  resulttable.destroy();
  resulttable = $('#datas').DataTable({
    ajax: {
      type: 'GET',
      url: '/test/tables'
    },
    "autoWidth": false,
    columns: [
      { 'data': 'name' },
      { 'data': 'address' }
    ], 
    scrollY: "310px",
    scrollCollapse: true
  });
}


function refreshSearchTable() {
  searchtable.destroy();
  searchtable = $('#searches').DataTable({
    ajax: {
      type: 'GET',
      url: '/test/searchtables'
    },
    "autoWidth": false,

    columns: [
      { 'data': 'composite_id' },
      { 'data': 'composite_name' },
      { 'data': 'user_id' },
      {
        'data': null,
        orderable: false,
        "render": function (data, type, full) { // return string is html format
          return '<div> <a href="/load"> <button class="button small"> <i class="material-icons small">file_upload</i> <span class="button-text"> Load </span> </button> </a> </div>';
        }
      }
    ], 
    scrollY: "310px",
    scrollCollapse: true
  });
}

function openTable(evt, tableName) {
  var i, tabcontent, tablinks;
  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(tableName).style.display = "block";
  evt.currentTarget.className += " active";
}

function deleteEntry() {
  // Ajax call to delete entry
}