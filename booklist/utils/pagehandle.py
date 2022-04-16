import math

class PageInfo(object):
    def __init__(self, current_page, all_count,per_page,page_url,page_num=3):
        print(current_page)
        try:
            self.current_page = int(current_page)
            #
            # if current_page==0:
            #     self.current_page=1
            # else:
            #     self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1

        self.per_page = per_page

        a,b =divmod(all_count,per_page)#总数量/每页数量=页数 a 商，b余数
        if b: #如果有余数，则页数+1
            a= a+1
        a1 = math.ceil(3/2)
        print(a1)
        self.pager_count = a 
        self.page_num=page_num
        self.page_url = page_url
    #当前页展示书籍，从第几本开始，到第几本结束，当前页第一本和最后一本，序号相差一页的数量
    def start(self):
        return ((self.current_page-1)*self.per_page)

    def end(self):
        return (self.current_page*self.per_page)


    def pager(self):
        v = "<a href='/booklist/showbooks/?page=1'>1</a>"
        page_list = []
        half = int((self.page_num-1)/2)

        if self.pager_count<self.page_num:
            begin = 1
            stop = self.pager_count+1

        else:
            if self.current_page<=half:#总页数 < 中间页
                begin=1
                stop=self.page_num+1
            else:
                if self.current_page+half>self.pager_count:
                    begin = self.pager_count-self.page_num+1
                    stop = self.pager_count+1
                else:
                    begin = self.current_page-half
                    stop = self.current_page+half+1

        if self.current_page<=1:
            prev = "<a href='#'>Prev</a>"
        else:
            prev = "<a href='%s?page=%s'>Prev</a>" %(self.page_url,self.current_page-1)
        page_list.append(prev)
        for i in range(begin,stop):
            if i ==self.current_page:
                temp = "<li class='active'><a class='active' href='%s?page=%s'>%s</a></li>" %(self.page_url,i,i)
                # temp = "<a class='active' href='%s?page=%s'>%s</a>" %(self.page_url,i,i)
            else:
                temp = "<li><a href='%s?page=%s'>%s</a></li>" %(self.page_url,i,i)

            page_list.append(temp)

        if self.current_page >= self.pager_count:
            next = "<li><a href='#'>next</a></li>"
        else:
            next = "<li><a href='%s?page=%s'>next</a></li>" % (self.page_url,self.current_page+1)
        page_list.append(next)
        # for i in page_list:
        #     print(i)
        return ''.join(page_list)

# p = PageInfo(1,10,2,132,3)