递归调用


def func():
    func()

递归：
将大问题可以拆解成多个相同的小问题解决
终止条件:

N !   
        N > 0  1 * 2 * 3 * 4 * N
        N = 0  1 


N! = N * (N - 1)!
f(n) = n * f(n - 1)
n = 0 f(n) = 1


list = [3, 5, 1, 2, 1]
左边: 找比3大于或等于的第一个元素 i
右边: 找比3小的第一个元素 j
交换
[1, 5, 1, 2, 3]
[1, 3, 1, 2, 5]
[1, 2, 1, 3, 5]
i j
i >= j

list[i] (tmp) >= list[j]
    交换
        i = i + 1
        j 不变
list[i] > list[j](tmp)
        j = j - 1
        i 不变




list = [1, 2, 1, 3, 5]
list[0:3] + list[3] + list[4:]


func(list, start, end)

冒泡
插入
二分
堆
桶
....

查找
[value, value2]
{value:True}
dict.get(value) O(1)

mysql select * from table from time > 1 and time < 1
查下条件索引 btree


在模板中
{{ object.attr }}
{{ object.func }}


1. 购物车中数量为0，不让点开购物车
2. 购物车中数量为0，不提交
3. 购物车中数量为0，跳转到首页，并提示(V)


1. 收获地址不存在时，跳转到收货地址添加页面，并提示 ==> 作业

1. 新的订单在最上面
2. 订单分页
3. 用户数据权限
4. 订单查询 ==> 作业
5. 订单操作
    状态图



1. View
    OrderOperateView(LoginRequiredMixin, View)

    def post():
        order_id
        operate(cancel/makesure)

        order = Order.objects.get(pk=order_id) ==> user
        order.status = 4(cancel) order.status = 0
        order.status = 3(makesure) order.status = 1
        order.save()
        return 
2. urls.py
3. template
    button => onclick
    confirm/sweetalert
    jQuery.post('url', { order-id, operate, csrfmiddlewaretoken }, function() {
        页面刷新
    }, 'json');


需要一个后台脚本进行后台任务
统计任务
    每天统计下营业额
    每天统计用户活跃度
    每天、每小时、每N时间段 统计访问日志状态/流量/
检查任务
    每天检查库存，库存数量<10, 发邮件通知
    检查磁盘当前增长超过了硬盘的10%(剩余10%)
后台异步任务
    页面点击后，后台异步执行，统计任务状态进度，告知用户

写一个python脚本
django command => models => db

urls => view => form
                        => models => db
commands =>


计算当前（前一天）交易状态为已经完成的所有交易额的总和

select sum(price) from goods_order
where
update_time between start and end 
&& status = 2

select sum(price) from goods_order
where
status = 2

time.sleep(24 * 60 * 60)

for i in range(24 * 60)
    time.sleep(60)
    
root
chown -R www:www www
chown -R www:www media 
chown -R www:www logs