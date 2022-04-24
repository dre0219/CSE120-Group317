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
    //{'data': 'address' },
    {'data': 'name'},
    {'data': 'address'}
    ],
  });
}

