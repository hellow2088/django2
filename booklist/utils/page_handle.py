import math


def current_page_handle(total_counts,per_page_num,current_page):
    total_pages = math.ceil(total_counts / per_page_num)
    if not current_page:
        current_page = 1
    # elif int(current_page) <= 1:
    #         current_page = 1
    # elif int(current_page)>total_pages:
    #     current_page =  total_pages
    else:
        current_page = int(current_page)
    return current_page


class pageino():

    def __init__(self,total_count,per_page_num=0,currrent_page_num=0,show_pages=11):
        self.total_count = total_count
        self.per_page_num = per_page_num
        # print('currrent_page_num=%s'%currrent_page_num)
        self.currrent_page_num = currrent_page_num

        self.show_pages = show_pages

    def showpages(self):#一共展示多少页
        # self.show_pages =
        if self.show_pages > math.ceil(self.total_count/self.per_page_num):
            self.show_pages = math.ceil(self.total_count/self.per_page_num)
        else:
            self.show_pages  = self.show_pages
        # print(self.show_pages)

        return self.show_pages

    def current_data(self):
        #从第几个开始
        start = (self.currrent_page_num-1)*self.per_page_num
        #到第几个结束
        end = self.currrent_page_num*self.per_page_num

        # print('当前页数据%s:%s'%(start,end))

        return start,end

    def next_prev(self):
        next = self.currrent_page_num+1

        prev = self.currrent_page_num-1

        return next,prev



p  = pageino(total_count=11,per_page_num=4,currrent_page_num=3,show_pages=9)
p.showpages()
p.current_data()
