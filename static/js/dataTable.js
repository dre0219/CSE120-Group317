var table;

$(document).ready(function () {
  table = $('#datas').DataTable({
    "language": {
      "emptyTable": "To get started, draw an area/areas and click refresh"
    },
    columns: [
    {data: 'name'},
    {data: 'address'}
  ],
});
});

function refreshTable(){
  table.destroy();
  table = $('#datas').DataTable({
    "autoWidth": false,
    ajax: {type: 'GET',
          url:'/test/tables'},
          "aoColumns": [{
            "mData": 'name'
          }, {
            "mData": 'address'
          }, {
            "mData": null,
            "bSortable": false,
            "mRender": function(data, type, full) {
              return '<a class="btn btn-info btn-sm" href=#/' + full[0] + '>' + 'Button' + '</a>';
            }
          }]
  });
}

function deleteEntry(){
  // Ajax call to delete entry
}