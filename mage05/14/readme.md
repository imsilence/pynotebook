前端:
    html: 定义展示内容
    css: 定义展示样式
        head
            link rel="stylesheet" type="text/css" href=
            style type="text/css"
    javascript: 定义展示动作

js
    js基本语法(ES6)
        js基于原类 property

    DOM 文档对象模型 => js对文档对象进行操作
        添加/删除/修改一个dom节点(内容/属性)
        事件
        document.getElementById() one
        document.getElementsByTagName() array
        document.getElementsByClassName() array

        获取值/设置值
        内容 innerHTML
        属性 id/value/style

    BOM 浏览器对象模型 => js对浏览器的操作
        打开一个浏览器窗口
        刷新一下当前请求页面
        重新发起新的请求页面
        获取浏览器的信息
        ...

基本语法
    js
        </body>之前
        <script type="text/javascript" src=""></script>
        <script type="text/javascript">

        </script>

    jquery
        选择器

        innerHTML ==> html() html(value)
        innerText ==> text() text(value)
        attr
            id, name, src, href   ==> attr("id/name") attr("id/name/src/href", value)
            style.xxx             ==> css()
            class                 ==> addClass/removeClass(className)
            value                 ==> val() val(value)

        绑定事件


    ajax 异步的javascript 和 xml(json)

留言板功能做成异步
1. 提交数据异步
2. 获取页面数据异步
