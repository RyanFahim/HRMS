console.log("Hellooo");
// Create Django Ajax Call
$("form#addNotice").submit(function() {
    var titleInput = $('input[name="title"]').val().trim();
    var dateInput = $('input[name="date"]').val().trim();
    var desInput = $('input[name="des"]').val().trim();
    if (titleInput && dateInput && desInput) {
        // Create Ajax Call
        $.ajax({
            url: '{% url "create_notice" %}',
            data: {
                'title':titleInput,
                'date':dateInput,
                'des':desInput
            },
            dataType: 'json',
            success: function (data) {
                if (data.notice) {
                  appendToNoticeTable(data.notice);
                }
            }
        });
      } else {
        alert("All fields must have a valid value.");
    }
    $('form#addNotice').trigger("reset");
    return false;
});
function appendToNoticeTable(notice) {
  $("#noticeTable > tbody:last-child").append(`
        <tr id="notice-${notice.id}">
            <td class="noticeName" name="title">${notice.title}</td>
            '<td class="noticeAddress" name="date">${notice.date}</td>
            '<td class="noticeAge" name="des">${notice.des}</td>
            '<td align="center">
                <button class="btn btn-success form-control" onClick="editNotice(${notice.id})" data-toggle="modal" data-target="#myModal")">EDIT</button>
            </td>
            <td align="center">
                <button class="btn btn-danger form-control" onClick="deleteNotice(${notice.id})">DELETE</button>
            </td>
        </tr>
    `);
}



    // // Create Django Ajax Call

    // Create Django Ajax Call
$("form#updateNotice").submit(function() {
    var idInput = $('input[name="formId"]').val().trim();
    var titleInput = $('input[name="formTitle"]').val().trim();
    var dateInput = $('input[name="formDate"]').val().trim();
    var desInput = $('input[name="formDes"]').val().trim();
    if (titleInput && dateInput && desInput) {
        // Create Ajax Call
        $.ajax({
            url: '{% url "update_notice" %}',
            data: {
                'id': idInput,
                'title': titleInput,
                'date': dateInput,
                'des': desInput
            },
            dataType: 'json',
            success: function (data) {
                if (data.notice) {
                  updateToNoticeTabel(data.notice);
                }
            }
        });
       } else {
        alert("All fields must have a valid value.");
    }
    $('form#updateNotice').trigger("reset");
    $('#myModal').modal('hide');
    return false;
});

// Update Django Ajax Call
function editNotice(id) {
  if (id) {
    tr_id = "#notice-" + id;
    title = $(tr_id).find(".noticeTitle").text();
    date = $(tr_id).find(".noticeDate").text();
    des = $(tr_id).find(".noticeDes").text();
    $('#form-id').val(id);
    $('#form-title').val(title);
    $('#form-date').val(date);
    $('#form-des').val(des);
  }
}
function updateToNoticeTabel(user){
    $("#noticeTable #notice-" + notice.id).children(".noticeData").each(function() {
        var attr = $(this).attr("title");
        if (attr == "title") {
          $(this).text(notice.title);
        } else if (attr == "date") {
          $(this).text(notice.date);
        } else {
          $(this).text(notice.des);
        }
      });
}


function deleteNotice(id) {
  var action = confirm("Are you sure you want to delete this user?");
  if (action != false) {
    $.ajax({
        url: '{% url "delete_notice" %}',
        data: {
            'id': id,
        },
        dataType: 'json',
        success: function (data) {
            if (data.deleted) {
              $("#noticeTable #notice-" + id).remove();
            }
        }
    });
  }
}

