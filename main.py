import matplotlib
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path


def main():
    matplotlib.rcParams['font.family'] = 'SimHei'
    matplotlib.rcParams['axes.unicode_minus'] = False

    root = tk.Tk()
    root.state('zoomed')
    root.title("猛兽选择器")

    # 加载标题图片
    title_photo = ImageTk.PhotoImage(file="images/title.png")

    # 加载背景图片
    # bg_image_left = ImageTk.PhotoImage(file="path_to_left_side_image.png")  # 替换为你的左侧背景图片路径
    bg_image_right = ImageTk.PhotoImage(file="images/background.png")  # 替换为你的右侧背景图片路径

    # 创建主Canvas
    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=title_photo, anchor="nw")

    # 创建左右两侧容器
    main_frame = tk.Frame(canvas, bg='#FEF7E2')
    main_frame.place(x=250, y=0, width=200, height=root.winfo_screenheight())

    image_frame = tk.Frame(canvas, bg='#FEF7E2')
    image_frame.place(x=440, y=0, width=root.winfo_screenwidth() - 440, height=root.winfo_screenheight())

    # 在右侧容器中添加背景图片Label
    bg_label = tk.Label(image_frame, image=bg_image_right)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # 填充整个容器
    bg_label.image = bg_image_right  # 保持图片引用

    # 复选框选项配置
    options = [
        ("犬科动物", tk.BooleanVar()),
        ("猫科动物", tk.BooleanVar()),
        ("食草动物", tk.BooleanVar()),
        ("食肉动物", tk.BooleanVar()),
        ("会潜水", tk.BooleanVar()),
        ("会飞行", tk.BooleanVar()),
        ("有角", tk.BooleanVar()),
        ("大眼睛", tk.BooleanVar()),
        ("毛茸茸", tk.BooleanVar()),
        ("会下蛋", tk.BooleanVar()),
        ("尾巴长", tk.BooleanVar())
    ]

    # 动物数据
    # 定义动物列表
    animals_list = {
        "犬科动物": ["尼莫", "斯帕奇", "八公", "珞珞", "毛毛", "麦克斯", "白菜狗", "卡托", "雪诺",
                     "桑尼", "山姆", "哈士企", "罗恩", "斯黛拉"],

        "猫科动物": ["玛奇朵", "泰哥", "加肥", "利威尔", "希子", "嘟嘟", "玛奈奇", "苗苗", "星期天"],

        "食草动物": ["卡洛特", "培根", "芭比", "瓦力", "莫斯", "阿瓜", "阿呆", "柯蒂斯", "白菜狗", "咕咕", "优罗莎",
                     "宝伯", "小新", "可乐", "高非", "奥姆诺姆", "豆豆", "福吉", "福宝"],

        "食肉动物": ["尼莫", "鳄霸", "地包天", "玛奇朵", "瓦特", "泰哥", "斯帕奇", "图斯卡尔", "八公",
                     "加肥", "珞珞", "木木", "毛毛", "麦克斯", "锤子", "利威尔", "布鲁斯", "希子", "卡托",
                     "雪诺", "嘟嘟", "刺头", "桑尼", "玛奈奇", "山姆", "哈士企", "苗苗", "星期天", "罗恩", "斯黛拉"],

        "会潜水": ["鳄霸", "瓦特", "阿瓜", "阿呆", "图斯卡尔", "锤子", "布鲁斯", "阿宝", "哈士企"],

        "会飞行": ["阿瓜", "阿呆", "木木", "咕咕", "优罗莎", "暴莉", "阿宝"],

        "有角": ["地包天", "瓦力", "莫斯", "柯蒂斯", "暴莉", "咩咩", "阿宝"],

        "大眼睛": ["鳄霸", "地包天", "阿瓜", "木木", "柯蒂斯", "咕咕", "奥里", "咩咩", "嘟嘟", "阿宝", "奥姆诺姆",
                   "豆豆", "哈士企"],

        "毛茸茸": ["尼莫", "玛奇朵", "卡洛特", "瓦特", "泰哥", "芭比", "瓦力", "莫斯", "八公", "加肥", "珞珞",
                   "毛毛", "麦克斯", "利威尔", "希子", "卡托", "宝伯", "咩咩", "雪诺", "嘟嘟", "刺头", "可乐", "阿宝",
                   "高非", "玛奈奇", "山姆", "福吉", "福宝", "哈士企", "苗苗", "星期天", "罗恩", "斯黛拉"],

        "会下蛋": ["鳄霸", "地包天", "阿瓜", "阿呆", "木木", "柯蒂斯", "锤子", "咕咕", "布鲁斯", "阿宝", "豆豆",
                   "泰雷斯"],

        "尾巴长": ["鳄霸", "地包天", "玛奇朵", "泰哥", "斯帕奇", "八公", "加肥", "珞珞", "毛毛", "麦克斯", "柯蒂斯",
                   "锤子", "利威尔", "咕咕", "布鲁斯", "奥里", "希子", "卡托", "雪诺", "嘟嘟", "阿宝", "玛奈奇", "山姆",
                   "福吉", "苗苗", "星期天"]
    }

    # 图片展示相关变量
    IMAGE_SIZE = (95, 120)  # 统一图片尺寸
    COLUMNS = 9  # 每行显示数量
    photo_cache = {}  # 图片缓存
    current_labels = []  # 当前显示的标签

    def clear_images():
        """清除当前显示的图片"""
        for label in current_labels:
            label.destroy()
        current_labels.clear()

    def load_image(animal):
        """加载并缓存图片"""
        if animal not in photo_cache:
            try:
                path = Path(f"images/{animal}.png")
                img = Image.open(path).resize(IMAGE_SIZE, Image.Resampling.LANCZOS)
                photo_cache[animal] = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"无法加载 {animal} 的图片: {str(e)}")
                return None
        return photo_cache[animal]

    def show_images(animals):
        """显示图片网格"""
        clear_images()

        if not animals:
            # label = tk.Label(image_frame, text="没有找到符合条件的动物",
            #                  font=("汉仪正圆-85W", 24), bg='#FEF7E2')
            # label.grid(row=0, column=0)
            # current_labels.append(label)
            not_found_image = tk.PhotoImage(file="images/notfound.png")
            label = tk.Label(image_frame, image=not_found_image, bg='#FEF7E2')
            label.place(x=0, y=0, relwidth=1, relheight=1)  # 填充整个容器
            label.image = not_found_image  # 保存对图片的引用，防止被垃圾回收
            current_labels.append(label)
            return

        for idx, animal in enumerate(sorted(animals)):
            row = idx // COLUMNS
            col = idx % COLUMNS

            # 加载图片
            photo = load_image(animal)
            if not photo:
                continue

            # 创建图片容器
            container = tk.Frame(image_frame, bg='#FEF7E2')
            container.grid(row=row * 2, column=col, padx=10, pady=10)

            # 显示图片
            img_label = tk.Label(container, image=photo, bg='#FEF7E2')
            img_label.pack()

            # 显示动物名称
            name_label = tk.Label(container, text=animal, font=("汉仪正圆-85W", 14),
                                  bg='#fff1da', fg='#333333')
            name_label.pack()

            current_labels.extend([container, img_label, name_label])

    def animals():
        """更新筛选结果"""
        selected_options = [text for text, var in options if var.get()]

        if not selected_options:
            show_images(set())
            return
        animal_sets = [set(animals_list[option]) for option in selected_options]
        result = set.intersection(*animal_sets)
        # print(selected_options)
        # print(result)
        show_images(result)

    # 创建复选框
    for text, var in options:
        cb = tk.Checkbutton(
            main_frame,
            text=text,
            variable=var,
            anchor="w",
            justify="left",
            padx=10,
            pady=14,
            font=("方正兰亭圆简体_特", 25, "bold"),
            fg="#2B2D30",
            bg="#FEF7E2",
            activebackground="#DCA65E",
            command=animals,
            highlightthickness=0,  # 去除组件外层的白色高亮边框
            borderwidth=0  # 去除默认的1像素边框
        )
        cb.pack(side=tk.TOP, fill=tk.X)

    root.mainloop()


if __name__ == "__main__":
    main()
