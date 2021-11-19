$(document).ready(function(){
    showMemos();


})


function save_memo(){
    let content = $('#content').val();
    $.ajax({
        type: "POST",
        url: `/api/memos`,
        contentType: "application/json",
        data: JSON.stringify({content: content}),
        success: function (response) {
            alert(confirm("데이터를 확인하시겠습니까?"))
            showMemos(response['id'])
        }
    })
}

function showMemos(id){
    $.ajax({
        type: "GET",
        url: `/api/memos`,
        contentType: "application/json",
        success: function (response) {

        }
    })
}
