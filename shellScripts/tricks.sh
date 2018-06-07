1,删除所有的.bak后缀
 rename 's/\.bak$//' *.bak

2,把.jpe文件后缀修改为.jpg
 rename 's/\.jpe$/\.jpg' *.jpe

3,将abcd.jpg重命名为abcd_efg.jpg
 for file in *.jpg;do mv '$var' '${var%.jpg}_efg.jpg';done

4,将文件名中所有小写字母改为大写字母
 for var in `ls`;do mv -f '$var' `echo '$var' |tr a-z A-Z`;done

5,把文件的前三个字母变为vzomik
 for var in `ls`; do mv -f "$var" `echo "$var" |sed 's/^.../vzomik/'`; done

6,把文件名的后四个字母变为vzomik
 for var in `ls`; do mv -f "$var" `echo "$var" |sed 's/....$/vzomik/'`; done

7,以两个字符为一组，迭代字符串
 s="helloworld!"
 for((i=0;i<${#s};i++));do
     echo ${s:i:2}
     let "i+=1"
 done

8,统计文件的行数
 awk 'END{print NR}' filename
 wc -l filename

9,移除空白行
 sed '/^$/d' filename

10,打印除第二列的所有列
 cut -f2 -d";" --complement filename
