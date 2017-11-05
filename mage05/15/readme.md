var u1 = {'name' : 'kk', 'age' : 29}

var u2 = {name : 'kk', age: 29}

if(cond1) {

} else if(cond2) {

} else if(cond3) {

} else {

}


switch(value) {
    case value1:
        break;
    case value2:
        break;
    default:
        break;
}

for(var i = 0; i < arr.length; i++) {
    arr[i]
}
var g_var = value
function funcname(args) {
    var func_var = 1
    func_var2 = 2(可以 不要写这种方式)
    console.log(g_var)
    body
    return
}

func_var
func_var2

作用域链


function(a, b, c) {
    return a + b + c;
}(1, 2, 4)

add(1, 2, 5)


留言板异步请求
1. 留言按钮绑定 click事件
    jQuery('.btn-message').on('click', function() {

    });

2. 留言内容发给服务器
    a. 获取用户填写的信息
        title
        content
        id
        jQuery('#title').val()
        csrf_token

        form.serialize()
        form.serializeArray()
    b. 发起请求
        ajax
        jQuery.post(url, data, function() {}, "json")


        /online/save_ajax/      => name = 'namespace:save_ajax'

        app1 save_ajax
        app2 save_ajax

3. 刷新表格
    a. 获取数据
        ajax
        jQuery.get(url, function(data) {}, 'json') //最近20条
    b. 展示
        dom操作 tbody html/text <div style="color:red">aaa</div>
        i. 清空页面上原有的数据
            tbody.empty()``
        ii. 创建dom节点append
            html <tr><td></td></tr>

            tbody.html(tbody_str)


问题：
1. 未登录的怎么办
    session验证
    return json {}
        status: 200 ok
        status: 403 not login
        status: 400 数据错误
2. 用户提交数据的验证
    验证
        a. 自己验证
        b. form
    成功
        提示成功
        刷新页面/表格
    失败
        提示用户失败（错误原因）


jQuery(selector).on('click', function() {

})


jQuery(document).on('click', selector, function() {

})


作业
1. 用户管理列表加载使用Datatable ajax方式
2. 用户添加、修改、修改密码使用Dialog+ajax+Datatable.ajax.reload+sweetalert方式
    jQuery.load()
3. 删除用户之前使用sweetalert让用户确认是否真的删除
4. 留言板Datatables国际化
