var resulttable;
var searchtable;

$(document).ready(function () {
  resulttable = $('#datas').DataTable({
    "language": {
      "emptyTable": "To get started, draw an area/areas and click refresh"
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
    columns: [
      { 'data': 'composite_id' },
      { 'data': 'composite_name' },
      { 'data': 'user_id' }
    ],
  });
});

function refreshTable() {
  resulttable.destroy();
  resulttable = $('#datas').DataTable({
    "autoWidth": false,
    ajax: {
      type: 'GET',
      url: '/test/tables'
    },
    "aoColumns": [
      { "mData": 'name' },
      { "mData": 'address' },
      {
        "mData": null,
        "bSortable": false,
        "mRender": function (data, type, full) {
          return '<a class="btn btn-info btn-sm" href=#/' + full[0] + '>' + 'Button' + '</a>';
        }
      }]
  });
}

function refreshSearchTable() {
  searchtable.destroy();
  searchtable = $('#searches').DataTable({
    ajax: {
      type: 'GET',
      url: '/test/searchtables'
    },
    columns: [
      { 'data': 'composite_id' },
      { 'data': 'composite_name' },
      { 'data': 'user_id' }
    ],
  });
}

function deleteEntry() {
  // Ajax call to delete entry
}