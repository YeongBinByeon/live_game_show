class live_stream:
    # 맴버변수 (실제 컬럼보다는 작게 세팅했음)
    name = '' 
    viewerCount = '' 
    link = ''
    img = ''
    # 생성자
    def __init__(self, name, viewerCount, link, img=None):
        self.name = name
        self.viewerCount = viewerCount
        self.link = link
        self.img = img