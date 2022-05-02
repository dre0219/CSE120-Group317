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

<<<<<<< HEAD
=======
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

>>>>>>> 79020d0d76897e70bb5b1bf44f832da20f1451ef
function deleteEntry(){
  // Ajax call to delete entry
}