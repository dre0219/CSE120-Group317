var resulttable;
var searchtable;

$(document).ready(function () {
  resulttable = $('#datas').DataTable({
    columns: [
    {'data': 'name'},
    {'data': 'address'}
  ],
  });
  searchtable = $('#searches').DataTable({
    ajax: {type: 'GET',
          url:'/test/searchtables'},
    columns: [
    {'data': 'composite_id'},
    {'data': 'composite_name'},
    {'data': 'user_id'}
  ],
  });
});

function refreshTable(){
  resulttable.destroy();
  resulttable = $('#datas').DataTable({
    ajax: {type: 'GET',
          url:'/test/tables'},
    columns: [
    {'data': 'name'},
    {'data': 'address'}
    ],
  });
}

function refreshSearchTable(){
  searchtable.destroy();
  searchtable = $('#searches').DataTable({
    ajax: {type: 'GET',
          url:'/test/searchtables'},
    columns: [
    {'data': 'composite_id'},
    {'data': 'composite_name'},
    {'data': 'user_id'}
    ],
  });
}

function deleteEntry(){
  // Ajax call to delete entry
}