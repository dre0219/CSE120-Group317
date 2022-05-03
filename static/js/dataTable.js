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
      { 'data': 'user_id' }
    ]
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
    ]
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
    "columnDefs": [
      { "width": "6%", "targets": 3 }],
    columns: [
      { 'data': 'composite_id' },
      { 'data': 'composite_name' },
      { 'data': 'user_id' },
      {
        'data': null,
        orderable: false,
        "render": function (data, type, full) { // return string is html format
          return '<div> <button onclick="hi()" class="button small"> <i class="material-icons small">file_upload</i> <span class="button-text"> Load </span> </button> </div>';
        }
      }
    ]
  });
}
function hi(){
  alert("Hi");
}

function deleteEntry() {
  // Ajax call to delete entry
}