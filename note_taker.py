import wx
import json
app = wx.App()
the_title = wx.Frame(None, title = "note taker")
panel = wx.Panel(the_title)
size = wx.BoxSizer(wx.VERTICAL)
def read_file():
    with open("english.json", "r", encoding="utf-8") as english0:
        global english
        english = json.load(english0)
    with open("persian.json", "r", encoding="utf-8") as persian0:
        global persian
        persian = json.load(persian0)
read_file()
def english_language():
    guide_label0 = wx.StaticText(panel, label = english["note taker input"])
    size.Add(guide_label0, 0, wx.ALL, 5)
    user_input0 = wx.TextCtrl(panel, style = wx.TE_MULTILINE)
    size.Add(user_input0, 1, wx.ALL | wx.EXPAND, 5)
    button2 = wx.Button(panel, label = english["confirm input"])
    size.Add(button2, 0, wx.ALL, 5)
    def value1(event):
        global user_data0
        user_data0 = user_input0.GetValue()
    button2.Bind(wx.EVT_BUTTON, value1)
    button3 = wx.Button(panel, label = english["save"])
    size.Add(button3, 0, wx.ALL, 5)
    def file_name(event):
        label_file_name = wx.StaticText(panel, label = english["file name"])
        size.Add(label_file_name, 0, wx.ALL, 5)
        user_input1 = wx.TextCtrl(panel)
        size.Add(user_input1, 0, wx.ALL, 5)
        button4 = wx.Button(panel, label = english["save"])
        size.Add(button4, 0, wx.ALL, 5)
        def user_value(event):
            global user_data1
            user_data1 = user_input1.GetValue()
        button4.Bind(wx.EVT_BUTTON, user_value)
        with open(f"{user_data1}.txt", "w", encoding = "utf-8") as file:
            file_write = file.write(user_data0)
            wx.MessageBox(english["save success"])
    button3.Bind(wx.EVT_BUTTON, file_name)
def persian_language():
    guide_label0 = wx.StaticText(panel, label = persian["note taker input"])
    size.Add(guide_label0, 0, wx.ALL, 5)
    user_input0 = wx.TextCtrl(panel, style = wx.TE_MULTILINE)
    size.Add(user_input0, 1, wx.ALL | wx.EXPAND, 5)
    button2 = wx.Button(panel, label = persian["confirm input"])
    size.Add(button2, 0, wx.ALL, 5)
    def value1(event):
        global user_data0
        user_data0 = user_input0.GetValue()
    button2.Bind(wx.EVT_BUTTON, value1)
    button3 = wx.Button(panel, label = persian["save"])
    size.Add(button3, 0, wx.ALL, 5)
    def file_name(event):
        label_file_name = wx.StaticText(panel, label = persian["file name"])
        size.Add(label_file_name, 0, wx.ALL, 5)
        user_input1 = wx.TextCtrl(panel)
        size.Add(user_input1, 0, wx.ALL, 5)
        button4 = wx.Button(panel, label = persian["save"])
        size.Add(button4, 0, wx.ALL, 5)
        def user_value(event):
            global user_data1
            user_data1 = user_input1.GetValue()
        button4.Bind(wx.EVT_BUTTON, user_value)
        with open(f"{user_data1}.txt", "w", encoding = "utf-8") as file:
            file_write = file.write(user_data0)
            wx.MessageBox(persian["save success"])
    button3.Bind(wx.EVT_BUTTON, file_name)
def language_selecter(english, persian):
    guide_label = wx.StaticText(panel, label = "please select a language, type en or english for english, pe or persian for persian")
    size.Add(guide_label, 0, wx.ALL, 5)
    user_input = wx.TextCtrl(panel)
    size.Add(user_input, 0, wx.ALL, 5)
    button1 = wx.Button(panel, label = "confirm language")
    size.Add(button1, 0, wx.ALL, 5)
    def value(event):
        user_data = user_input.GetValue()
        if user_data.lower().strip() == "en" or user_data.lower().strip() == "english":
            wx.MessageBox(english["success"])
            english_language()
        elif user_data.lower().strip() == "pe" or user_data.lower().strip() == "persian":
            wx.MessageBox(persian["success"])
            persian_language()
    button1.Bind(wx.EVT_BUTTON, value)
language_selecter(english, persian)
panel.SetSizer(size)
panel.Layout()
the_title.Show()
app.MainLoop()