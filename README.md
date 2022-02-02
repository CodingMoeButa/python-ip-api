# python-ip-api
A Python Crawler for IP-API.com

## 使用方法
1. 安装依赖：
```bash
pip3 install requests
pip3 install pymysql
```
2. 在MySQL数据库中执行`ipv4.sql`。

3. 修改`main.py`中的数据库地址、端口号、用户名、密码和数据库名称。

4. 运行`main.py`，输入起始IP（curip）和终末IP+0.0.1.0（endip）。
