var table;

$(document).ready(function () {

  table = $('#tables').DataTable({
    columns: [
    {data: 'name'}
  ],
});
});





function refreshTable(){
  table.destroy();
  table = $('#datas').DataTable({
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