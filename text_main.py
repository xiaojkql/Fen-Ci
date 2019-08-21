def f1():
    print("Hello, world!")


print(23)

""" 控制模块的使用方式
当是以为python该文件时则运行__name__以下的内容，当是导入其他的python文件时则不运行 """
if __name__ == "__main__":
    f1()
