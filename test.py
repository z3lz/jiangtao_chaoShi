# import tkinter as tk
#
# root = tk.Tk()
# products = {
#     "苹果": {"位置": "第一排第3个", "售价": '1.00元/斤'},
#     "香蕉": {"位置": "第二排第5个", "售价": '8.00元/斤'},
#     "橘子": {"位置": "第一排第8个", "售价": '14.00元/斤'},
#     "葡萄": {"位置": "第三排第3个", "售价": '12.00元/斤'},
#     "西瓜": {"位置": "第一排第2个", "售价": '10.00元/斤'},
# }
#
# root.title("超市货品信息搜索软件")
#
# # 添加标签、输入框、按钮等元素
# tk.Label(root, text="商品名称:").grid(row=0)
# tk.Entry(root).grid(row=0, column=1)
# tk.Label(root, text="价格范围:").grid(row=1)
# tk.Entry(root).grid(row=1, column=1)
# tk.Label(root, text="-").grid(row=1, column=2)
# tk.Entry(root).grid(row=1, column=3)
# tk.Button(root, text="搜索").grid(row=2, columnspan=2)
#
# root.mainloop()



import tkinter as tk

# 创建商品字典
goods = {
    "苹果": {"位置": "第一排第3个", "售价": '1.00元/斤'},
    "香蕉": {"位置": "第二排第5个", "售价": '8.00元/斤'}
}

# 定义搜索函数
def search():
    keyword = entry.get()  # 获取搜索关键词
    if keyword in goods:
        result.config(text=f"位置：{goods[keyword]['位置']}，售价：{goods[keyword]['售价']}")
    else:
        result.config(text="未找到该商品")

# 创建窗口
window = tk.Tk()
window.title("5502超市货品信息搜索软件")

# 创建搜索框和按钮
label = tk.Label(window, text="请输入要搜索的商品：")
label.pack()
entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="搜索", command=search)
button.pack()

# 创建结果显示标签
result = tk.Label(window, text="")
result.pack()

# 运行窗口
window.mainloop()

# from flask import Flask, request, jsonify
# import tkinter as tk
#
# # 创建商品字典
# goods = {
#     "苹果": {"位置": "第一排第3个", "售价": '1.00元/斤'},
#     "香蕉": {"位置": "第二排第5个", "售价": '8.00元/斤'}
# }
#
# # 定义搜索函数
# def search(keyword):
#     if keyword in goods:
#         return {"位置": goods[keyword]['位置'], "售价": goods[keyword]['售价']}
#     else:
#         return {"位置": "", "售价": ""}
#
# # 创建窗口
# window = tk.Tk()
# window.title("5502超市货品信息搜索软件")
#
# # 创建搜索框和按钮
# label = tk.Label(window, text="请输入要搜索的商品：")
# label.pack()
# entry = tk.Entry(window)
# entry.pack()
# button = tk.Button(window, text="搜索", command=lambda: search(entry.get()))
# button.pack()
#
# # 创建结果显示标签
# result = tk.Label(window, text="")
# result.pack()
#
# app = Flask(__name__)
#
# @app.route('/search', methods=['GET'])
# def search_api():
#     keyword = request.args.get('keyword')
#     result = search(keyword)
#     return jsonify(result)
#
# if __name__ == '__main__':
#     app.run(debug=True)




# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
#
# # 创建商品字典
# goods = {
#     "苹果": {"位置": "第一排第3个", "售价": '1.00元/斤'},
#     "香蕉": {"位置": "第二排第5个", "售价": '8.00元/斤'}
# }
#
#
# # 定义搜索函数
# def search(instance):
#     keyword = text_input.text  # 获取搜索关键词
#     if keyword in goods:
#         Result_label.text = f"位置：{goods[keyword]['位置']}，售价：{goods[keyword]['售价']}"
#     else:
#         result_label.text = "未找到该商品"
#
# class MyApp(App):
#
#     def build(self):
#         # 创建布局
#         layout = BoxLayout(orientation='vertical')
#
#         # 创建搜索框和按钮
#         search_label = Label(text="请输入要搜索的商品：")
#         text_input = TextInput()
#         search_button = Button(text="搜索")
#         search_button.bind(on_press=search)
#
#         # 创建结果显示标签
#         result_label = Label(text="")
#
#         # 添加控件到布局中
#         layout.add_widget(search_label)
#         layout.add_widget(text_input)
#         layout.add_widget(search_button)
#         layout.add_widget(result_label)
#
#         return layout
#
# if __name__ == '__main__':
#     MyApp().run()


# import json
# from flask import Flask
#
# app = Flask(__name__)
#
# # 创建超市货品信息字典
# goods_dict = {
#     "苹果": {"位置": "第一排第3个", "售价": '1.00元/斤'},
#     "香蕉": {"位置": "第二排第5个", "售价": '8.00元/斤'}
# }
#
# # 将字典转换为JSON格式并保存到文件中
# with open('goods.json', 'w') as fp:
#     json.dump(goods_dict, fp)
#
# # 在浏览器中访问http://localhost:5000/goods 可以查看JSON格式的超市货品信息
# # http://172.20.10.8:5000/goods
# @app.route('/goods', methods=['POST','GET'])
# def get_goods():
#     with open('goods.json', 'r') as fp:
#         goods_json = json.load(fp)
#     return goods_json
#
# if __name__ == '__main__':
#     # app.run()
#     app.run(host='0.0.0.0', port=5000, debug=True)


