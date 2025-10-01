# Among Us Tools v1.0.7 by 忆梦
# 本程序仅供学习交流使用，请勿用于商业用途。
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
import psutil
import random
from datetime import datetime

class AmongUsTools:
    def __init__(self, root):
        self.root = root
        self.root.title("Among Us 私服安装工具箱")
        
        # 设置窗口大小
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        
        # 设置窗口居中显示
        self.center_window()
        
        # 设置样式
        self.root.configure(bg='#f0f0f0')

        # 创建选项卡
        self.tabControl = ttk.Notebook(root)
        
        # 创建"私服安装"选项卡
        self.install_tab = tk.Frame(self.tabControl, bg='#f0f0f0')
        self.tabControl.add(self.install_tab, text="私服安装")
        
        # 创建"更多"选项卡
        self.more_tab = tk.Frame(self.tabControl, bg='#f0f0f0')
        self.tabControl.add(self.more_tab, text="更多")
        
        # 默认显示"私服安装"选项卡
        self.tabControl.pack(expand=1, fill="both")
        
        # 创建"私服安装"页的内容
        self.create_install_tab()
        self.create_more_tab()
        
        # 初始化今日人品点击次数
        self.rp_click_count = 0
        
        # 存储regioninfo.json文件路径
        self.regioninfo_path = None
        
        # 存储自定义服务器数据
        self.custom_server_data = None
        
        # 定义服务器配置
        self.server_configs = {
            "清风": [
                {
                    "$type": "StaticHttpRegionInfo, Assembly-CSharp",
                    "Name": "<color=#16FFFF>清风服</color><color=#1B5EB7>[宁波]</color>",
                    "PingServer": "https://nb.server.qingfengawa.top",
                    "Servers": [
                        {
                            "Name": "Http-1",
                            "Ip": "https://nb.server.qingfengawa.top",
                            "Port": 443,
                            "UseDtls": False,
                            "Players": 0,
                            "ConnectionFailures": 0
                        }
                    ],
                    "TargetServer": None,
                    "TranslateName": 1003
                }
            ],
            "帆船": [
                {
                    "$type": "StaticHttpRegionInfo, Assembly-CSharp",
                    "Name": "<color=#ff7518>帆船服<color=#ffff00>[广东广州]",
                    "PingServer": "https://gz.fcaugame.cn",
                    "Servers": [
                        {
                            "Name": "Http-1",
                            "Ip": "https://gz.fcaugame.cn",
                            "Port": 443,
                            "UseDtls": False,
                            "Players": 0,
                            "ConnectionFailures": 0
                        }
                    ],
                    "TargetServer": None,
                    "TranslateName": 1003
                }
            ],
            "核电站": [
                {
                    "$type": "StaticHttpRegionInfo, Assembly-CSharp",
                    "Name": "<color=#FFA500>核电站</color><color=#ffff00>[宁波]</color>",
                    "PingServer": "https://nb.aunpp.cn",
                    "Servers": [
                        {
                            "Name": "http-1",
                            "Ip": "https://nb.aunpp.cn",
                            "Port": 8888,
                            "UseDtls": False,
                            "Players": 0,
                            "ConnectionFailures": 0
                        }
                    ],
                    "TargetServer": None,
                    "TranslateName": 1003
                }
            ],
            "碧水港": [
                {
                    "$type": "StaticHttpRegionInfo, Assembly-CSharp",
                    "Name": "<color=#00E0FF>碧水港</color><color=#ffff00>[香港]</color>",
                    "PingServer": "miaowuhk.fcaugame.cn",
                    "Servers": [
                        {
                            "Name": "http-1",
                            "Ip": "miaowuhk.fcaugame.cn",
                            "Port": 443,
                            "UseDtls": False,
                            "Players": 0,
                            "ConnectionFailures": 0
                        }
                    ],
                    "TargetServer": None,
                    "TranslateName": 1003
                }
            ],
            "Niko": [
                {
                    "$type": "StaticHttpRegionInfo, Assembly-CSharp",
                    "Name": "<color=#ffe000ff>Niko233(NA)</color>",
                    "PingServer": "https://au-us.niko233.me",
                    "Servers": [
                        {
                            "Name": "Http-1",
                            "Ip": "https://au-us.niko233.me",
                            "Port": 443,
                            "UseDtls": False,
                            "Players": 0,
                            "ConnectionFailures": 0
                        }
                    ],
                    "TargetServer": None,
                    "TranslateName": 1003
                },
                {
                    "$type": "StaticHttpRegionInfo, Assembly-CSharp",
                    "Name": "<color=#ffe000ff>Niko233(AS)</color>",
                    "PingServer": "https://au-as.niko233.me",
                    "Servers": [
                        {
                            "Name": "Http-1",
                            "Ip": "https://au-as.niko233.me",
                            "Port": 443,
                            "UseDtls": False,
                            "Players": 0,
                            "ConnectionFailures": 0
                        }
                    ],
                    "TargetServer": None,
                    "TranslateName": 1003
                },
                {
                    "$type": "StaticHttpRegionInfo, Assembly-CSharp",
                    "Name": "<color=#ffe000ff>Niko233(EU)</color>",
                    "PingServer": "https://au-eu.niko233.me",
                    "Servers": [
                        {
                            "Name": "Http-1",
                            "Ip": "https://au-eu.niko233.me",
                            "Port": 443,
                            "UseDtls": False,
                            "Players": 0,
                            "ConnectionFailures": 0
                        }
                    ],
                    "TargetServer": None,
                    "TranslateName": 1003
                },
                {
                    "$type": "StaticHttpRegionInfo, Assembly-CSharp",
                    "Name": "<color=#ffe000ff>Niko233(CN)</color>",
                    "PingServer": "https://au-as.niko233.me",
                    "Servers": [
                        {
                            "Name": "Http-1",
                            "Ip": "https://au-as.niko233.me",
                            "Port": 443,
                            "UseDtls": False,
                            "Players": 0,
                            "ConnectionFailures": 0
                        }
                    ],
                    "TargetServer": None,
                    "TranslateName": 1003
                }
            ]
        }
        
    def center_window(self):
        """将窗口居中显示"""
        # 强制更新窗口以获取准确的尺寸信息
        self.root.update_idletasks()
        
        # 获取窗口尺寸
        width = 600
        height = 400
        
        # 获取屏幕尺寸
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # 计算居中位置
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        # 设置窗口位置和大小
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def create_install_tab(self):
        # 标题
        title_label = tk.Label(self.install_tab, text="Among Us 私服安装", font=("Arial", 18, "bold"), 
                              bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=15)
        
        # 描述标签
        desc_label = tk.Label(self.install_tab, text="选择要添加的服务器源，然后安装到游戏中", 
                             font=("Arial", 10), bg='#f0f0f0', fg='#666666')
        desc_label.pack(pady=5)
        
        # 服务器源选择框架
        self.server_frame = tk.LabelFrame(self.install_tab, text="选择服务器源", padx=20, pady=15, 
                                    font=("Arial", 12, "bold"), bg='#f0f0f0', fg='#333333')
        self.server_frame.pack(pady=20, padx=30, fill="x")
        
        # 服务器源说明
        server_desc = tk.Label(self.server_frame, text="请选择一个或多个服务器源添加到游戏中：", 
                              font=("Arial", 9), bg='#f0f0f0', fg='#555555')
        server_desc.pack(anchor='w', pady=(0, 10))
        
        # 服务器源选择变量
        self.server_vars = {
            "清风": tk.BooleanVar(),
            "帆船": tk.BooleanVar(),
            "核电站": tk.BooleanVar(),
            "碧水港": tk.BooleanVar(),
            "Niko": tk.BooleanVar()
        }
        
        # 初始化复选框引用字典
        self.server_checkbuttons = {}
        self.server_labels = {}
        
        # 创建复选框容器
        self.server_container = tk.Frame(self.server_frame, bg='#f0f0f0')
        self.server_container.pack()
        
        # 创建复选框
        for i, (server_name, var) in enumerate(self.server_vars.items()):
            cb_frame = tk.Frame(self.server_container, bg='#f0f0f0')
            cb_frame.pack(side=tk.LEFT, padx=15)
            
            cb = tk.Checkbutton(cb_frame, variable=var, bg='#f0f0f0', activebackground='#f0f0f0')
            cb.pack()
            self.server_checkbuttons[server_name] = cb  # 保存引用
            
            cb_label = tk.Label(cb_frame, text=server_name, font=("Arial", 10), bg='#f0f0f0')
            cb_label.pack()
            self.server_labels[server_name] = cb_label  # 保存引用
        
        # 初始化时禁用服务器选择
        self.disable_server_selection()
        
        # 按钮框架
        button_frame = tk.Frame(self.install_tab, bg='#f0f0f0')
        button_frame.pack(pady=30)
        
        # 载入数据按钮 - 与开始安装按钮样式一致
        load_btn = tk.Button(button_frame, text="载入数据", command=self.load_data, 
                            bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), 
                            width=12, height=1, relief=tk.RAISED, bd=2)
        load_btn.pack(side=tk.LEFT, padx=15)
        
        # 开始安装按钮
        install_btn = tk.Button(button_frame, text="开始安装", command=self.install_servers, 
                               bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), 
                               width=12, height=1, relief=tk.RAISED, bd=2)
        install_btn.pack(side=tk.LEFT, padx=15)
        
        # 状态标签框架
        status_frame = tk.Frame(self.install_tab, bg='#f0f0f0')
        status_frame.pack(side=tk.BOTTOM, fill='x', pady=15)
        
        # 状态标签
        self.status_label = tk.Label(status_frame, text="请先载入数据", fg="gray", 
                                    bg='#f0f0f0', font=("Arial", 9))
        self.status_label.pack()
        
    def disable_server_selection(self):
        """禁用服务器选择框"""
        for server_name in self.server_vars.keys():
            self.server_checkbuttons[server_name].config(state=tk.DISABLED)
            self.server_labels[server_name].config(fg='#aaaaaa')  # 灰色文字表示禁用状态
        
    def enable_server_selection(self):
        """启用服务器选择框"""
        for server_name in self.server_vars.keys():
            self.server_checkbuttons[server_name].config(state=tk.NORMAL)
            self.server_labels[server_name].config(fg='#000000')  # 黑色文字表示启用状态
        
    def create_more_tab(self):
        # 更多页面内容
        title_label = tk.Label(self.more_tab, text="更多功能", font=("Arial", 18, "bold"), 
                              bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=20)
        
        # 创建画布用于装饰性分隔线
        canvas = tk.Canvas(self.more_tab, height=2, bg='#f0f0f0', highlightthickness=0)
        canvas.pack(fill='x', padx=50, pady=10)
        canvas.create_line(0, 1, 500, 1, fill='#cccccc', width=2)
        
        # 功能按钮框架
        button_frame = tk.Frame(self.more_tab, bg='#f0f0f0')
        button_frame.pack(pady=20, expand=True)
        
        # 今日人品按钮
        rp_btn = tk.Button(button_frame, text="今日人品", command=self.check_personality,
                          bg="#FFA500", fg="white", font=("Arial", 12, "bold"),
                          width=20, height=2, relief=tk.RAISED, bd=2)
        rp_btn.pack(pady=10)
        
        # 小游戏按钮
        game_btn = tk.Button(button_frame, text="小游戏", command=self.mini_game,
                           bg="#2196F3", fg="white", font=("Arial", 12, "bold"),
                           width=20, height=2, relief=tk.RAISED, bd=2)
        game_btn.pack(pady=10)
        
        # 修复旧版黑屏按钮
        fix_btn = tk.Button(button_frame, text="修复旧版黑屏", command=self.fix_black_screen,
                           bg="#9E9E9E", fg="white", font=("Arial", 12, "bold"),
                           width=20, height=2, relief=tk.RAISED, bd=2)
        fix_btn.pack(pady=10)
        
    def check_personality(self):
        """检查今日人品功能"""
        # 增加点击次数
        self.rp_click_count += 1
        
        # 检查是否触发彩蛋
        if self.rp_click_count > 5:
            # 显示彩蛋信息
            messagebox.showinfo("提示", "不要再点我啦！")
            
        # 获取AUTools文件夹路径
        username = os.getenv('USERNAME')
        folder_path = f"C:\\Users\\{username}\\AppData\\Local\\AUTools"
        
        # 如果文件夹不存在则创建
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
        file_path = os.path.join(folder_path, "rp.json")
        today = datetime.now().strftime("%Y/%m/%d")
        
        # 获取每日一言
        try:
            import urllib.request
            import ssl
            
            # 创建不验证SSL证书的上下文（某些环境下可能需要）
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            
            # 获取每日一言
            hitokoto_url = "https://v1.hitokoto.cn/?encode=text"
            request = urllib.request.Request(hitokoto_url)
            response = urllib.request.urlopen(request, context=ssl_context, timeout=5)
            hitokoto = response.read().decode('utf-8')
        except Exception as e:
            hitokoto = "今日无言"
        
        # 如果文件存在
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    
                # 解析文件内容
                time_line = lines[0].strip() if len(lines) > 0 else ""
                rp_line = lines[1].strip() if len(lines) > 1 else ""
                
                # 检查时间是否为今日
                if time_line.startswith("time="):
                    stored_time = time_line.split("=")[1]
                    if stored_time == today:
                        # 今日已生成人品值
                        if rp_line.startswith("rp="):
                            rp_value = rp_line.split("=")[1]
                            messagebox.showinfo("今日人品", f"你今日的人品是 {rp_value}！\n\n{hitokoto}")
                            return
                
                # 不是今日或者文件格式不正确，重新生成
                rp_value = str(random.randint(0, 100))
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f"time={today}\n")
                    f.write(f"rp={rp_value}\n")
                    
                messagebox.showinfo("今日人品", f"你今日的人品是 {rp_value}！\n\n{hitokoto}")
                
            except Exception as e:
                # 文件读取或解析出错，重新生成
                rp_value = str(random.randint(0, 100))
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(f"time={today}\n")
                    f.write(f"rp={rp_value}\n")
                    
                messagebox.showinfo("今日人品", f"你今日的人品是 {rp_value}！\n\n{hitokoto}")
        else:
            # 文件不存在，创建新文件
            rp_value = str(random.randint(0, 100))
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(f"time={today}\n")
                f.write(f"rp={rp_value}\n")
                
            messagebox.showinfo("今日人品", f"你今日的人品是 {rp_value}！\n\n{hitokoto}")
            
    def mini_game(self):
        """小游戏功能"""
        # 创建小游戏选择窗口
        game_window = tk.Toplevel(self.root)
        game_window.title("小游戏")
        game_window.geometry("300x200")
        game_window.resizable(False, False)
        game_window.configure(bg='#f0f0f0')
        
        # 窗口居中
        game_window.update_idletasks()
        width = 300
        height = 200
        x = (game_window.winfo_screenwidth() // 2) - (width // 2)
        y = (game_window.winfo_screenheight() // 2) - (height // 2)
        game_window.geometry(f"{width}x{height}+{x}+{y}")
        
        # 标题
        title_label = tk.Label(game_window, text="选择小游戏", font=("Arial", 16, "bold"), 
                              bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=20)
        
        # 贪吃蛇按钮
        snake_btn = tk.Button(game_window, text="贪吃蛇", command=lambda: self.start_snake_game(game_window),
                             bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
                             width=15, height=2, relief=tk.RAISED, bd=2)
        snake_btn.pack(pady=10)
        
    def fix_black_screen(self):
        """修复旧版黑屏功能"""
        # 显示警告对话框
        warning_result = messagebox.askyesno(
            "警告",
            "该操作将从网络下载设置文件并替换您当前的游戏设置，可能存在一定风险。\n\n是否继续？",
            icon='warning'
        )
        
        if not warning_result:
            return
            
        try:
            import urllib.request
            import ssl
            
            # 创建不验证SSL证书的上下文（某些环境下可能需要）
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            
            # 获取游戏设置文件路径
            appdata_local_low = os.path.expandvars(r"%LOCALAPPDATA%\..\LocalLow")
            settings_path = os.path.join(appdata_local_low, "Innersloth", "Among Us", "settings.amogus")
            
            # 下载文件
            url = "http://api.mxyx.club/download/among-us/OtherFiles/settings.amogus"
            urllib.request.urlretrieve(url, settings_path)
            
            messagebox.showinfo("成功", "设置文件已成功更新！")
        except Exception as e:
            messagebox.showerror("错误", f"操作失败: {str(e)}")

    def start_snake_game(self, parent_window):
        """启动贪吃蛇游戏"""
        # 关闭选择窗口
        parent_window.destroy()
        
        # 创建贪吃蛇游戏窗口
        snake_game = SnakeGame()
        
    def load_data(self):
        # 询问用户选择方式
        choice = messagebox.askquestion("选择载入方式", "是否使用默认路径自动载入regioninfo.json文件？\n\n是：自动选择\n否：手动选择", icon='question')
        
        if choice == 'yes':
            self.auto_select()
        elif choice == 'no':
            self.manual_select()
        
    def auto_select(self):
        # 默认路径
        appdata_local_low = os.path.expandvars(r"%LOCALAPPDATA%\..\LocalLow")
        regioninfo_path = os.path.join(appdata_local_low, "Innersloth", "Among Us", "regioninfo.json")
        
        if os.path.exists(regioninfo_path):
            self.regioninfo_path = regioninfo_path
            self.status_label.config(text=f"已加载: {os.path.basename(regioninfo_path)}", fg="green")
            self.enable_server_selection()  # 启用服务器选择
            messagebox.showinfo("成功", f"已成功加载regioninfo.json文件\n路径: {regioninfo_path}")
        else:
            self.status_label.config(text="未找到regioninfo.json文件", fg="red")
            messagebox.showerror("错误", f"未在默认路径找到regioninfo.json文件\n请确认文件是否存在:\n{regioninfo_path}")
            
    def manual_select(self):
        file_path = filedialog.askopenfilename(
            title="选择regioninfo.json文件",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            if os.path.basename(file_path).lower() == "regioninfo.json":
                self.regioninfo_path = file_path
                self.status_label.config(text=f"已加载: {os.path.basename(file_path)}", fg="green")
                self.enable_server_selection()  # 启用服务器选择
                messagebox.showinfo("成功", f"已成功加载regioninfo.json文件\n路径: {file_path}")
            else:
                self.status_label.config(text="请选择正确的regioninfo.json文件", fg="red")
                messagebox.showerror("错误", "请选择正确的regioninfo.json文件")
        else:
            self.status_label.config(text="未选择文件", fg="red")
            
    def install_servers(self):
        if not self.regioninfo_path:
            self.status_label.config(text="请先载入数据", fg="red")
            messagebox.showerror("错误", "请先载入regioninfo.json文件")
            return
            
        # 检查是否有选中的服务器
        selected_servers = [name for name, var in self.server_vars.items() if var.get()]
        if not selected_servers:
            self.status_label.config(text="请选择至少一个服务器", fg="red")
            messagebox.showerror("错误", "请选择至少一个服务器")
            return
            
        # 显示警告对话框
        warning_result = messagebox.askyesno(
            "警告",
            "该操作可能会导致你的服务器数据出现错误/被重新排版，推荐备份后再继续安装！\n\n是否继续安装？",
            icon='warning'
        )
        
        if not warning_result:
            self.status_label.config(text="安装已取消", fg="gray")
            return
            
        # 检查是否有运行中的Among Us进程
        among_us_processes = [p for p in psutil.process_iter(['pid', 'name']) if p.info['name'] == 'Among Us.exe']
        if among_us_processes:
            result = messagebox.askyesno("警告", "检测到Among Us正在运行，是否关闭游戏进程以继续安装？")
            if result:
                try:
                    for proc in among_us_processes:
                        proc.terminate()
                        proc.wait(timeout=5)  # 等待最多5秒
                    messagebox.showinfo("成功", "已关闭Among Us进程，请重新启动游戏以应用更改")
                except Exception as e:
                    messagebox.showerror("错误", f"关闭进程时出错: {str(e)}")
                    return
            else:
                # 用户选择不关闭进程，继续进行安装
                pass
                
        # 执行attrib命令移除regioninfo.json文件的只读属性
        try:
            import subprocess
            subprocess.run(['attrib', '-r', self.regioninfo_path], check=True, capture_output=True)
        except Exception as e:
            # 即使attrib命令执行失败也继续安装流程
            pass  # 不中断安装过程
                
        # 读取regioninfo.json文件
        try:
            with open(self.regioninfo_path, 'r', encoding='utf-8') as f:
                region_data = json.load(f)
        except Exception as e:
            self.status_label.config(text="读取regioninfo.json文件失败", fg="red")
            messagebox.showerror("错误", f"读取regioninfo.json文件失败: {str(e)}")
            return
            
        # 添加选中的服务器配置
        installed_servers = []  # 记录成功安装的服务器
        duplicate_servers = []  # 记录重复的服务器
        
        for server_name in selected_servers:
            if server_name in self.server_configs:
                for config in self.server_configs[server_name]:
                    # 检查是否已存在相同的服务器配置
                    existing = False
                    for existing_region in region_data.get("Regions", []):
                        if (existing_region.get("Name") == config["Name"] and 
                            existing_region.get("PingServer") == config["PingServer"]):
                            existing = True
                            duplicate_servers.append(config["Name"])
                            break
                    
                    # 如果不存在，则添加
                    if not existing:
                        region_data.setdefault("Regions", []).append(config)
                        # 记录安装的服务器名称，避免重复
                        if server_name not in installed_servers:
                            installed_servers.append(server_name)
        
        # 写入修改后的数据到regioninfo.json文件
        try:
            with open(self.regioninfo_path, 'w', encoding='utf-8') as f:
                json.dump(region_data, f, ensure_ascii=False, indent=2)
                
            # 构建安装结果信息
            result_message = ""
            if installed_servers:
                result_message += f"已成功安装以下服务器:\n" + "\n".join(installed_servers) + "\n\n"
                
            if duplicate_servers:
                result_message += f"以下服务器已存在，未重复安装:\n" + "\n".join(duplicate_servers)
                
            if not result_message:
                result_message = "没有新的服务器需要安装"
                
            self.status_label.config(text=f"安装完成：{len(installed_servers)} 个新服务器，{len(duplicate_servers)} 个重复服务器", fg="green")
            messagebox.showinfo("安装结果", result_message)
        except Exception as e:
            self.status_label.config(text="写入regioninfo.json文件失败", fg="red")
            messagebox.showerror("错误", f"写入regioninfo.json文件失败: {str(e)}")


class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("贪吃蛇")
        self.window.geometry("600x600")
        self.window.resizable(False, False)
        
        # 游戏参数
        self.cell_size = 20
        self.grid_width = 30  # 600 / 20
        self.grid_height = 30  # 600 / 20
        self.speed = 130  # 略微加快游戏速度（从150毫秒调整到130毫秒）
        self.win_length = 50  # 胜利条件：蛇的长度
        
        # 游戏状态
        self.game_started = False
        self.game_over = False
        self.direction = "Right"  # 初始方向
        self.next_direction = "Right"  # 下一个方向
        
        # 蛇的初始位置（列表存储身体节段的坐标）
        self.snake = [(5, 15), (4, 15), (3, 15)]
        
        # 食物位置
        self.food = self.generate_food()
        
        # 创建画布
        self.canvas = tk.Canvas(self.window, width=600, height=600, bg='#333333')
        self.canvas.pack()
        
        # 显示开始提示
        self.start_text = self.canvas.create_text(
            300, 280, 
            text="按Space开始游戏", 
            fill="white", 
            font=("Arial", 20, "bold")
        )
        
        # 显示游戏说明
        self.instruction_text = self.canvas.create_text(
            300, 320,
            text=f"胜利条件：长度达到 {self.win_length}",
            fill="gray",
            font=("Arial", 12)
        )
        
        # 显示分数
        self.score_text = self.canvas.create_text(
            50, 20,
            text="长度: 3",
            fill="white",
            font=("Arial", 12, "bold")
        )
        
        # 绑定按键事件
        self.window.bind('<space>', self.start_game)
        self.window.bind('<Key>', self.change_direction)
        self.window.focus_set()
        
        # 启动窗口
        self.window.mainloop()
        
    def generate_food(self):
        """生成食物位置"""
        while True:
            food = (random.randint(0, self.grid_width - 1), 
                   random.randint(0, self.grid_height - 1))
            # 确保食物不在蛇身上
            if food not in self.snake:
                return food
        
    def start_game(self, event):
        """开始游戏"""
        if not self.game_started:
            self.game_started = True
            # 删除开始提示文本和说明文本
            self.canvas.delete(self.start_text)
            self.canvas.delete(self.instruction_text)
            # 开始游戏循环
            self.game_loop()
            
    def change_direction(self, event):
        """改变蛇的移动方向"""
        key = event.keysym
        # 防止反向移动
        if key == "Up" and self.direction != "Down":
            self.next_direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.next_direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.next_direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.next_direction = "Right"
            
    def game_loop(self):
        """游戏主循环"""
        if self.game_over:
            return
            
        # 更新方向
        self.direction = self.next_direction
        
        # 移动蛇
        head_x, head_y = self.snake[0]
        
        # 根据方向计算新的头部位置
        if self.direction == "Up":
            new_head = (head_x, head_y - 1)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 1)
        elif self.direction == "Left":
            new_head = (head_x - 1, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 1, head_y)
            
        # 检查碰撞边界
        if (new_head[0] < 0 or new_head[0] >= self.grid_width or 
            new_head[1] < 0 or new_head[1] >= self.grid_height):
            self.end_game()
            return
            
        # 检查碰撞自己
        if new_head in self.snake:
            self.end_game()
            return
            
        # 将新头部添加到蛇身
        self.snake.insert(0, new_head)
        
        # 检查是否吃到食物
        if new_head == self.food:
            # 生成新食物
            self.food = self.generate_food()
            # 更新分数显示
            self.canvas.itemconfig(self.score_text, text=f"长度: {len(self.snake)}")
        else:
            # 没吃到食物，移除尾部
            self.snake.pop()
            
        # 检查是否胜利（蛇身达到指定长度）
        if len(self.snake) >= self.win_length:
            self.win_game()
            return
            
        # 重新绘制游戏画面
        self.draw_game()
        
        # 继续游戏循环
        self.window.after(self.speed, self.game_loop)
        
    def draw_game(self):
        """绘制游戏画面"""
        # 清空画布
        self.canvas.delete("all")
        
        # 绘制网格线（提升视觉效果）
        for i in range(0, 600, self.cell_size):
            self.canvas.create_line(i, 0, i, 600, fill="#444444", width=1)
            self.canvas.create_line(0, i, 600, i, fill="#444444", width=1)
        
        # 绘制蛇身
        for i, (x, y) in enumerate(self.snake):
            # 蛇头使用不同颜色
            if i == 0:
                # 蛇头使用亮绿色
                color = "#00FF00"
                outline = "#00CC00"
            else:
                # 蛇身使用渐变绿色
                color_value = max(100, 255 - i * 3)  # 随着身体节段增加逐渐变暗
                color = f"#00{color_value:02x}00"
                outline = f"#00{max(80, color_value - 20):02x}00"
                
            self.canvas.create_rectangle(
                x * self.cell_size, 
                y * self.cell_size,
                (x + 1) * self.cell_size, 
                (y + 1) * self.cell_size,
                fill=color, 
                outline=outline,
                width=2
            )
            
        # 绘制食物（使用更醒目的颜色）
        food_x, food_y = self.food
        self.canvas.create_oval(
            food_x * self.cell_size + 2, 
            food_y * self.cell_size + 2,
            (food_x + 1) * self.cell_size - 2, 
            (food_y + 1) * self.cell_size - 2,
            fill="#FF4500",
            outline="#FF6347",
            width=2
        )
        
        # 绘制分数
        self.canvas.create_text(
            50, 20,
            text=f"长度: {len(self.snake)}",
            fill="white",
            font=("Arial", 12, "bold")
        )
        
    def end_game(self):
        """游戏结束"""
        self.game_over = True
        self.canvas.create_rectangle(150, 200, 450, 300, fill="black", outline="white", width=2)
        self.canvas.create_text(
            300, 240,
            text=f"游戏结束！",
            fill="red",
            font=("Arial", 20, "bold")
        )
        self.canvas.create_text(
            300, 270,
            text=f"最终长度: {len(self.snake)}",
            fill="white",
            font=("Arial", 14)
        )
        # 2秒后重置游戏
        self.window.after(2000, self.reset_game)
        
    def win_game(self):
        """游戏胜利"""
        self.game_over = True
        self.canvas.create_rectangle(150, 200, 450, 300, fill="black", outline="white", width=2)
        self.canvas.create_text(
            300, 240,
            text=f"恭喜！你赢了！",
            fill="yellow",
            font=("Arial", 20, "bold")
        )
        self.canvas.create_text(
            300, 270,
            text=f"最终长度: {len(self.snake)}",
            fill="white",
            font=("Arial", 14)
        )
        # 2秒后重置游戏
        self.window.after(2000, self.reset_game)
        
    def reset_game(self):
        """重置游戏到初始状态"""
        # 重置游戏状态
        self.game_started = False
        self.game_over = False
        self.direction = "Right"
        self.next_direction = "Right"
        
        # 重置蛇的位置
        self.snake = [(5, 15), (4, 15), (3, 15)]
        
        # 生成新食物
        self.food = self.generate_food()
        
        # 清空画布
        self.canvas.delete("all")
        
        # 重新绘制网格线
        for i in range(0, 600, self.cell_size):
            self.canvas.create_line(i, 0, i, 600, fill="#444444", width=1)
            self.canvas.create_line(0, i, 600, i, fill="#444444", width=1)
        
        # 重新显示开始提示
        self.start_text = self.canvas.create_text(
            300, 280, 
            text="按Space开始游戏", 
            fill="white", 
            font=("Arial", 20, "bold")
        )
        
        # 重新显示游戏说明
        self.instruction_text = self.canvas.create_text(
            300, 320,
            text=f"胜利条件：长度达到 {self.win_length}",
            fill="gray",
            font=("Arial", 12)
        )
        
        # 重新显示分数
        self.score_text = self.canvas.create_text(
            50, 20,
            text="长度: 3",
            fill="white",
            font=("Arial", 12, "bold")
        )


if __name__ == "__main__":
    root = tk.Tk()
    # 在创建应用之前隐藏根窗口
    root.withdraw()
    app = AmongUsTools(root)
    # 显示窗口
    root.deiconify()
    root.mainloop()
