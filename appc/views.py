from django.http import HttpResponse

# Create your views here.

from appc import tasks


def create_worker_add(requet):
    res = tasks.add.delay(2, 3)
    print(res)
    return HttpResponse(res)


def create_worker_multi(requet):
    res = tasks.multi.delay(2, 3)
    print(res)
    return HttpResponse(res)


# 延迟执行的任务
def create_eta_worker(request):
    res = tasks.send_msg.apply_async(args=(2, 4), countdown=10)
    print('这是一个延迟任务', res)
    return HttpResponse(res)


def get_result(requet):
    from ccnn import celery_app
    from celery.result import AsyncResult

    task_id = requet.GET.get('task_id')
    result = AsyncResult(id=task_id, app=celery_app)

    resp = None
    if result.successful():
        resp = result.get()
        print('异步任务的结果是：', resp)
    elif result.failed():
        print('异步任务执行失败！')
    elif result.status == 'PENDING':
        print('任务等待被执行中')
    elif result.status == 'RETRY':
        print('任务出现异常后正在重试！')
    elif result.status == 'STARTED':
        print('任务已经开始被执行啦！')
    return HttpResponse(resp)
