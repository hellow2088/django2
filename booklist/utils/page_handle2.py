import math

# 中间页是当前页：由总数，每页数，获取中间页码数
def current_page_handle(total_counts,per_page_num):
    # 总数/每页数=总页数，向上取整得出中间页数
    total_pages = math.ceil(total_counts / per_page_num)
    # print("总页数=%d"%total_pages)
    current_page = math.ceil(total_pages/2)
    print("当前=%d" % current_page)
    # 只有1页的时，中间页时负数时，第一页就是当前页
    if not current_page:
        current_page = 1
    elif int(current_page) <= 1:
            current_page = 1
    return current_page

class pageino():

    def __init__(self,total_count,per_page_num,currrent_page_num,show_pages):
        self.total_count = total_count
        self.per_page_num = per_page_num
        print('currrent_page_num=%s'%currrent_page_num)
        self.currrent_page_num = currrent_page_num
        # if currrent_page_num == None or currrent_page_num =='':
        #     self.currrent_page_num = 1
        # elif int(currrent_page_num)<=0:
        #     self.currrent_page_num =1
        # else:
        #     self.currrent_page_num = int(currrent_page_num)

        self.show_pages = show_pages

    def showpages(self):#一共展示多少页
        if self.show_pages > math.ceil(self.total_count/self.per_page_num):
            self.show_pages = math.ceil(self.total_count/self.per_page_num)
        # print(self.show_pages)

        return self.show_pages


    # 获取当前页的数据量
    def current_data(self):
        #从第几个开始
        start = (self.currrent_page_num-1)*self.per_page_num
        #到第几个结束
        end = self.currrent_page_num*self.per_page_num

        print('当前页数据量%s:%s'%(start,end))

        return start,end

    # 上下一页数，当前页码数+-1
    def next_prev(self):
        next = self.currrent_page_num+1

        prev = self.currrent_page_num-1

        return next,prev




total_count = 11
per_page_num = 4
currrent_page_num = current_page_handle(total_count,per_page_num)
show_pages = 9

p  = pageino(total_count,per_page_num,currrent_page_num,show_pages)
print("当前页：%d"%currrent_page_num)
p.showpages()
p.current_data()