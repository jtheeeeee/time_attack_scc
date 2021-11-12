$(document).ready(function(){
    showMemos();


})


function save_memo(memoDto){
    var content = $('#content').val();
    $.ajax({
        type: "POST",
        url: `/api/memos`,
        contentType: "application/json",
        data: JSON.stringify(memoDto),
        success: function (response) {
            alert("데이터를 확인하시겠습니까?")
        }
    })
}

function showMemos(){
    $.ajax({
        type: "GET",
        url: `/api/memos`,
        contentType: "application/json",
        success: function (response) {

        }
    })
}
