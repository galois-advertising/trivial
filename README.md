# 员工信息整理程序



## 下载

点击github右上角`code`菜单并单击`Download Zip`。将下载下来的文件解压到本地目录，例如`D:/trivial`。


## 准备

假设：
* employee.txt
	- 有2千职工姓名+编号的一个数据列
* D:/trivial/data/
	- 有一个杂乱的移动硬盘（但各格式文件名中都有“姓名+编号”字段）

实际情况可根据你的路径来的出。

安装`python` [点击我下载安装](https://www.python.org/downloads/) 如果有就不用安装了

## 使用


1. 打开`命令提示符`:开始->运行->输入cmd

2. 运行下面命令即可在`D:/trivial`下创建所有文件夹

```shell
cd D:/trivial
python process.py mkdir employee.txt 
```

3. 运行下列命令即可将`D:/trivial/data/`中的文件分发到到不同的文件夹

```shell
cd D:/trivial
python process.py arrange employee.txt D:/trivial/data/
```



