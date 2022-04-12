$(document).ready(function () {
    $('#data').DataTable({
        ajax: '/test/data',
        serverSide: true,
        columns: [
          {data: 'name'},
          {data: 'age'},
          {data: 'address', orderable: false},
          {data: 'phone', orderable: false},
          {data: 'email'}
        ],
      });
    });