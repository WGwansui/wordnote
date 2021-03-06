import wx

class MainFrame(wx.Frame):
    def __init__(self):

        '''
        whole class parameters:
            main_panel
            recite_panel
            main_new_word_text
            all_word
            number
        '''

        wx.Frame.__init__(self,None,title='WordNote',size=(300,300),style=wx.CLOSE_BOX | wx.MINIMIZE_BOX)

        self.init_menu()
        self.init_main_panel()
        self.main_panel.Show(True)
        self.init_recite_panel()
        self.recite_panel.Show(False)



        self.Show(True)
        self.Centre()

    def init_menu(self):
        menubar = wx.MenuBar()
        file_menu = wx.Menu()
        file_item = wx.MenuItem(file_menu, id=wx.ID_ANY, text='See All')
        file_menu.Append(file_item)
        menubar.Append(file_menu, 'Word')
        self.SetMenuBar(menubar)

    def init_main_panel(self):
        self.main_panel=wx.Panel(self,size=(300,300))

    #button
        main_button_panel=wx.Panel(self.main_panel,pos=(0,0),size=(300,300))
        button_add=wx.Button(main_button_panel,label='Add',pos=(192,156))
        button_recite=wx.Button(main_button_panel,label='Recite',pos=(25,230))
        button_evaluate=wx.Button(main_button_panel,label='Evaluate',pos=(192,230))
        main_button_panel.Bind(wx.EVT_BUTTON,self.main_react_button_add,button_add)
        main_button_panel.Bind(wx.EVT_BUTTON,self.main_react_button_recite,button_recite)
        main_button_panel.Bind(wx.EVT_BUTTON,self.main_react_button_evaluate,button_evaluate)
    #enter text
        self.main_new_word_text=wx.TextCtrl(self.main_panel,size=(150,25),pos=(22,154))
    #read data
        with open('data.txt','r') as data:
            self.all_word=data.readlines()
            print(self.all_word)
    #other
        bmp=wx.Bitmap('heading.png',wx.BITMAP_TYPE_ANY)
        bmp.SetSize((350,150))
        heading=wx.StaticBitmap(self.main_panel,-1,bmp)
        heading.Center(dir=wx.HORIZONTAL)

        wx.StaticLine(self.main_panel,pos=(10,120),size=(280,10))
        panel=wx.Panel(self,-1)
        panel.Bind(wx.EVT_KEY_UP,self.reicite_react_key)


    def main_react_button_add(self,event):
        new_word=self.main_new_word_text.GetLineText(0).strip().lower()
        if new_word.isalpha() and new_word+'\n' not in self.all_word:
            print(new_word+' is added')
            self.all_word.append(new_word+'\n')
            with open('data.txt','w') as data:
                data.writelines(self.all_word)
            print(self.all_word)

    def main_react_button_recite(self,event):
        self.main_panel.Show(False)
        self.recite_panel.Show(True)

    def main_react_button_evaluate(self,event):
        print('evaluate')

    def init_recite_panel(self):
        self.recite_panel=wx.Panel(self,size=(300,300))
    #button
        recite_button_panel=wx.Panel(self.recite_panel,size=(300,300))
        button_no=wx.Button(recite_button_panel,label='No',pos=(30,190))
        button_yes=wx.Button(recite_button_panel,label='Yes',pos=(192,190))
        recite_button_panel.Bind(wx.EVT_BUTTON,self.recite_react_button_no,button_no)
        recite_button_panel.Bind(wx.EVT_BUTTON,self.recite_react_button_yes,button_yes)
        wx.StaticLine(self.recite_panel,pos=(10,120),size=(280,10))
        self.recite_panel.Bind(wx.EVT_KEY_UP,self.reicite_react_key)
    #word
        word_panel=wx.Panel(self.recite_panel,size=(300,180))
        #word_panel.SetBackgroundColour('black')
        recite_font=wx.Font(45,wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL)
        self.number=0
        self.word=wx.StaticText(word_panel,label=self.all_word[self.number])
        self.word.SetForegroundColour((120,120,120))
        self.word.SetFont(recite_font)
        self.word.CenterOnParent()

    def reicite_react_key(self,event):
        #print(event)
        print(event.GetKeyCode())
        if event.GetKeyCode()==27:
            self.recite_panel.Show(False)
            self.main_panel.Show(True)

    def recite_react_button_no(self,event):
        self.number+=1
        if self.number>=len(self.all_word):
            self.number=0
        self.word.SetLabel(self.all_word[self.number])
        self.word.CenterOnParent()

    def recite_react_button_yes(self,event):
        self.number+=1
        if self.number>=len(self.all_word):
            self.number=0
        self.word.SetLabel(self.all_word[self.number])
        self.word.CenterOnParent()

    def recite_react_button_spell(self,event):
        print('spell')