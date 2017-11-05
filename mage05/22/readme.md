1. 查看商品详情
    a. 点击href请求后台要查看商品
        pk
        goods/\d+/
        goods/(\d+)/            
        goods/(?P<pk>\d+)/      get,post (self, request, args, kwargs)

    b. view(函数，View, ListView, FormView, DetailView, **)
        pk
        get_object()
        render(template)

        DetailView
            model
            template_name

    c. template
        object.a
        object.b
        objecct.c

    问题：
        商品删除后，可以通过原URL进行访问
            DetailView
            方法一: get_queryset
            方法二: get_object
        商品扩展信息删除后，商品信息中还是现实
            方法一: template 通过ext.status == 0

            方法二:
            背景知识:
                goods.goodsext_set
                goodsext.objects.filter(goods=goods)

                template ext.attrormethod
                    attrormethod ==> ext 属性
                                     ext 方法

                GoodsExt.exts(self):
                    return self.goodsext_set.filter(status=0)
                    return GoodsExt.objects.filter(goods=self, status=0)

                goods.exts

        重写objects对象为新的Manager

2. 加入购物车
    查看购物车


3. 下单
    修改商品的数量
        <input type="text"> 什么时候触发请求
        a. 要发请求，修改数据中
        b. 只有修改自己的
        c. 更新小计
        d. 更新购物车数量
    选择下单的商品
    选择收货人地址
    xxx

    用户
    商品s => 商品=>数量
    下单日期
    收货人
    状态


作业
0. 完成今天课程练习和整理今天知识点
1. 删除以后的商品禁止访问
2. 下订单时可对商品数量进行修改
3. 尝试展示订单列表