# 慕课学生成绩导出

## 1. 说明

本项目为[空间分析课程](https://www.icourse163.org/learn/WHUT-1460838161?tid=1468773480)的学生成绩导出脚本，其他课程的适用性未测试，最后一次适用时间为2022年12月10日。

本脚本主要通过请求慕课的学生成绩接口(http://www.icourse163.org/mm-tiku/web/j/mocTermScoreSummaryRpcBean.getStudentScorePagination.rpc)获取数据，该接口需要权限认证及若干参数。

### 1.1 权限认证

暂时采用直接设置Cookie的方式通过权限认证，因此需要先在网页中登录慕课，再通过浏览的请求获取本机的Cookie，并在脚本中设置。

### 1.2 爬取结果

本脚本旨在爬取具体数据，故在代码逻辑中添加了学校的筛选，只爬取请求结果中==schoolName==字段为具体值的用户数据，若需要所有可去除该过滤条件。

## 2. 环境依赖

需要安装
**requests**
**pandas**

## 3. 使用说明

### 3.1 参数设置

#### 3.1.1 设置Cookie

1. 用户登录：在浏览器中登录慕课，进入课程管理后台-选择具体课程-工具-学生成绩管理
2. 打开开发者工具：按F12，部分电脑需要Fn+F12，打开开发者工具，并再次刷新页面
3. 请求定位：切换到NetWork（网络）标签，找到mocTermScoreSummaryRpcBean.getStudentScorePagination.rpc请求，如图所示。

<center><img src='/imgs/fig1.jpg'></center>

4. Cookie获取：点击上述请求查看详情，切换到Headers标签，在Request Headers（请求头）中即可找到相应的Cookie。

<center><img src='/imgs/fig2.jpg'></center>

5. 修改脚本：替换脚本中的headers['Cookie']

#### 3.1.2 其他参数设置

**csrfKey**,**termId**：

1. 参数获取：同样在上述的请求详情中，切换到Payload标签，可在参数及表单信息中找到csrfKey和termId的值。

<center><img src='/imgs/fig3.jpg'></center>

2. 修改脚本：替换脚本中的csrfKey和termId

**resultName**：该参数为可选参数，为保存的结果文件名。

### 3.2 运行程序

执行该脚本即可，最终将在脚本的同级文件夹中生成结果文件。

<center><img src='/imgs/fig4.jpg'></center>
