class MyContextMgr:
    def __enter__(self):
        print("执行enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("执行exit")


with MyContextMgr() as mgr:
    print("执行上下文代码块")
