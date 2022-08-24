import execjs


with open('ras.js','r',encoding='utf8') as f:
    js_file = f.read()

js_obj = execjs.compile(js_file)
js_result = js_obj.call('test','123123123123')
print(js_result)