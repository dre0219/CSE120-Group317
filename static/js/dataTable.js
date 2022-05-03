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
<<<<<<< HEAD
=======
=======
>>>>>>> 95b84aa142ba99d7baa996d0f3c779044a83abef
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

<<<<<<< HEAD
>>>>>>> 79020d0d76897e70bb5b1bf44f832da20f1451ef
=======
>>>>>>> 95b84aa142ba99d7baa996d0f3c779044a83abef
function deleteEntry(){
  // Ajax call to delete entry
}