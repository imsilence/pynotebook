#encoding: utf-8

'''
1. 存储所有的任务用list, tasks
2. while循环
3. input
4. 输入非do, append
    do, 按照先进先出的原则
    (检查list是否为空，为空则打印无任务并退出)
    把任务弹出 pop(0)，并打印
'''


tasks = []

while True:
    input_text = input('please input do or a task:')
    if input_text != 'do':
        tasks.append(input_text)
    else:
        if len(tasks) == 0:
            print('无任务')
            break
        else:
            task = tasks.pop(0)
            print('任务:', task)
