class BrowserHistory:

    def __init__(self, homepage: str):
        self.his_list = ['']
        self.cur = 0
        self.head = 0
        self.his_list[0] = homepage

    def visit(self, url: str) -> None:
        self.cur += 1
        self.head = self.cur
        if self.cur < len(self.his_list):
            self.his_list[self.cur] = url
        else:
            self.his_list.append(url)

    def back(self, steps: int) -> str:
        self.cur -= steps
        if self.cur < 0:
            self.cur = 0
        return self.his_list[self.cur]

    def forward(self, steps: int) -> str:
        self.cur += steps
        if self.cur > self.head:
            self.cur = self.head
        return self.his_list[self.cur]

browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")       # 你原本在浏览 "leetcode.com" 。访问 "google.com"
browserHistory.visit("facebook.com")     # 你原本在浏览 "google.com" 。访问 "facebook.com"
browserHistory.visit("youtube.com")      # 你原本在浏览 "facebook.com" 。访问 "youtube.com"
print(browserHistory.back(1))                   # 你原本在浏览 "youtube.com" ，后退到 "facebook.com" 并返回 "facebook.com"
print(browserHistory.back(1))                   # 你原本在浏览 "facebook.com" ，后退到 "google.com" 并返回 "google.com"
browserHistory.forward(1)                # 你原本在浏览 "google.com" ，前进到 "facebook.com" 并返回 "facebook.com"
browserHistory.visit("linkedin.com")     # 你原本在浏览 "facebook.com" 。 访问 "linkedin.com"
print(browserHistory.forward(2))                # 你原本在浏览 "linkedin.com" ，你无法前进任何步数。
print(browserHistory.back(2))                   # 你原本在浏览 "linkedin.com" ，后退两步依次先到 "facebook.com" ，然后到 "google.com" ，并返回 "google.com"
print(browserHistory.back(7))                   # 你原本在浏览 "google.com"， 你只能后退一步到 "leetcode.com" ，并返回 "leetcode.com"

