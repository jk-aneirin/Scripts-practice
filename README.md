niceall:当在服务器上运行非核心且耗费cpu的任务时，将执行优先级设置为最低

fuzzyfinder.py实现模糊匹配，参数collection是待选的字符串列表，user_input是用户的输入字符串，通过输入字符串对比collection中的字符串，挑选出相似字符串保存在suggestions中

count200.py:统计apache日志中的HTTP状态，并将个数统计出来

filemonitor.py:监控一个指定目录，如果目录中的文件有修改，则将修改后的文件保存在指定目录

sendmail.py:使用qq邮箱向163邮箱发封邮件，发送前需要开启qq邮箱的IMAP/SMTP服务并获得授权码

popmail.py:使用pop协议接收来自服务器pop.qq.com上的邮件，取得的密码是通过开通qq邮箱的pop3/smtp服务获得的

sysinfo-server.py||sysinfo-client.py:使用模块Pyro4实现RPC，客户端可以获得运行服务端程序的服务器的cpu disk memory信息，因为没有使用ns，每次重启服务端，客户端需要换uri地址

setsys.py:设置系统时间

omitpoundsign.py:删除文件中开头包含井号的行

ipstat.py:统计tengine日志文件的ip数目

singleProRunning.py:保证同时只有一个singleProRunning.py在运行，实际工作的代码可以放在函数_run()中

pg-failover.py:使用了fabric，来实现postgresql数据库的主备切换
