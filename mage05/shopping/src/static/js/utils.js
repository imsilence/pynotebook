function openDialogLogin() {
    jQuery('#dialog_login').modal('show');
}

function ajax(url, data, callback, type) {
    type = type || 'POST';
    var success = function(data) {
        if(data['status'] == 200) {
            callback(data);
        } else if(data['status'] == 400) {
            var errors = [];
            jQuery.each(data['errors'], function(key, value) {
                errors.push(value[0]['message']);
            });
            swal({
                title: "验证失败",
                text: errors.join('\n'),
                type: "error",
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "确定"
            });
        } else if(data['status'] == 401) {
            var errors = data['errors'] || [];
            swal({
                title: "用户未登录",
                text: errors.join('\n'),
                type: "error",
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "确定",
                closeOnConfirm : false
            }, function() {
                swal.close();
                openDialogLogin();
            });
        } else if (data['status'] == 500) {
            var errors = data['errors'] || [];
            swal({
                title: "服务器错误",
                text: errors.join('\n'),
                type: "error",
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "确定"
            });
        } else {

        }
    }
    jQuery.ajax({url : url, type : type, data : data, success : success, dataType : 'json'});
}