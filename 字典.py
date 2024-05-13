d = {"张三":"财务部","李四":"市场部","王五":"品牌部"}
print(d)
#添加
d.setdefault("田所浩二","研发部")
print(d)
d.pop("研发部")
print(d)
for i in d:print(i)
print(d.get("张三"))
print(d.get("田所浩二"))