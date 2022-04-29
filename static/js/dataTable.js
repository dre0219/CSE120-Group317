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
    columns: [
    {'data': 'name'},
    {'data': 'address'}
    ],
  });
}

function deleteEntry(){
  // Ajax call to delete entry
}