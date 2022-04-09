$(document).ready(function () {
    var deleteBtn = document.getElementsByClassName("deleteBtnPost");

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
                    url: '/admin/delete-post/' + id+"/",
                    type: 'DELETE',
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader("X-CSRFToken", token);
                    },
                    success: function (data) {
                        var html_data = ``
                        var data = data["posts"]
                        for (var i = 0; i < data.length; i++) {
                            var item = data[i]
                            html_data += `<tr>
                                            <td>${item.id}</td>
                                            <td><a href="/blog/update-post/${item.id}/" class="link">${item.title}</a></td>
                                            <td data-search=${item.category_name}}>
                                                <p class="text-success">${item.category_name}</p>
                                            </td>
                                            <td>${item.description}</td>
                                            <td> <img src="${item.image}" width="100" height="100"> </td>
                                            <td>
                                                <div class="btns">
                                                    <a href="/blog/update-post/${item.id}/" class="btn btn-info">Edit</a>
                                                    <a id=${item.id} class="btn btn-danger deleteBtn">Sil</a>
                                                </div>
                                            </td>
                                        </tr>`
                        }
                        alert()
                        $("#table-post").html(html_data);
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

    $('#post').DataTable({
        search: {
            return: true
        }
    });
});