import wx
from os import chdir
from os import listdir
from os import getcwd
class ListPanel(wx.Panel):
	"""Panel with list"""
	def __init__(self, parent, *args, **kwargs):
		"""Create panel with list."""
		wx.Panel.__init__(self, parent, *args, **kwargs)
		self.index = 0
		self.dataList = []
		self.parent = parent
		self.listOfFile = wx.ListCtrl(self,style=wx.LC_REPORT)
		self.listOfFile.InsertColumn(0, 'name')
		self.listOfFile.InsertItem(self.index,'..')
		self.dataList.append('..')
		self.index+=1
		sizerV = wx.BoxSizer(wx.VERTICAL)
		sizerV.Add(self.listOfFile, 1, wx.ALL|wx.EXPAND, 5)
		self.SetSizer(sizerV)
		self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.doubleclick)
		self.dir = getcwd()
		self.resetItem()
		
	def AddItem(self,name):
		self.listOfFile.InsertItem(self.index,name)
		self.dataList.append(name)
		self.index += 1
	
	def resetItem(self):
		self.index = 0
		self.listOfFile.DeleteAllItems()
		self.dataList = [] 
		self.AddItem('..')
		for name in listdir(self.dir):
			self.AddItem(name)
		
	def doubleclick(self,event):
		SelectedItem= self.listOfFile.GetFirstSelected(self)
		chdir(self.dir)
		self.dir = getcwd()
		self.dir = self.dir+'\\'+self.dataList[SelectedItem]
		self.resetItem()
		
class MainFrame(wx.Frame):
	"""Main Frame holding all stuff"""
	def __init__(self, *args, **kwargs):
		"""Create the freeMKD"""
		super(MainFrame,self).__init__(*args, **kwargs)
		#Build menu bar
		MenuBar = wx.MenuBar()
		#define FileSubmenu 
		FileMenu = wx.Menu()
		#define item for File submenu
		FileItemQuit = FileMenu.Append(wx.ID_EXIT, "&Quit")
		self.Bind(wx.EVT_MENU,self.OnQuit, FileItemQuit)
		
		MenuBar.Append(FileMenu,"&File")
		self.SetMenuBar(MenuBar)
		#add widget to panel
		box = wx.BoxSizer(wx.HORIZONTAL)
		LeftList = ListPanel(self)
		RightList = ListPanel(self)
		box.Add(LeftList,1,wx.EXPAND)
		box.Add(RightList,1,wx.EXPAND)
		
		self.SetSizer(box)
		#self.Fit()
	def OnQuit(self, event = None):
		"""Exit application."""
		self.Close()
def main():
	app = wx.App()
	MF = MainFrame(None)
	MF.Show()
	app.MainLoop()
	
if __name__=='__main__':
	main()