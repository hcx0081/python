class Person:
    @classmethod
    def _cm(self):
        print("类方法")

    @staticmethod
    def sm():
        print('静态方法')

    def im(self):
        print("实例方法")
