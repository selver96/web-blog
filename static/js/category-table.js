$(document).ready(function () {
    var deleteBtn = document.getElementsByClassName("deleteBtn");

    var deleteCategory = function (e) {
        var alert = function () {
            Swal.fire(
                'Deleted!',
                'Category has been deleted.',
                'success'
            )
        }
        var token = document.cookie.split('=')[1]
        const id = e.target.id;
        Swal.fire({
            title: 'Are you sure?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!'
        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    url: '/admin/delete-category/' + id +"/",
                    type: 'DELETE',
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader("X-CSRFToken", token);
                    },
                    success: function (data) {
                        var html_data = ``
                        var data = data["categories"]
                        for (var i = 0; i < data.length; i++) {
                            var item = data[i]
                            html_data += `<tr>
                                            <td data-search="${item.id}">${item.id}</td>
                                            <td data-search="${item.name}">
                                                <a href="/blog/update-category/${item.id}/" class="link">${item.name}</a>
                                            </td>
                                            <td></td>
                                            <td></td>
                                            <td>
                                                <div class="btns">
                                                    <a href="/blog/update-category/${item.id}/" class="btn btn-info">Edit</a>
                                                    <a id=${item.id} class="btn btn-danger deleteBtn">Sil</a>
                                                </div>
                                            </td>
                                        </tr>`
                        }
                        alert()
                        $("#table-data").html(html_data);
                    }
                });

            }
        })
    }

    for (var i = 0; i < deleteBtn.length; i++) {
        deleteBtn[i].addEventListener("click", deleteCategory);
    }

    var eventFired = function (type) {

    }

    $('#category').DataTable({
        search: {
            return: true
        }
    });
});