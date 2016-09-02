
import os.path
import clr
project_dir = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(os.path.join(project_dir, "..", "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "..", "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName('TestStack.White')
from TestStack.White.UIItems.Finders import *
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput

clr.AddReferenceByName('UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35')
from System.Windows.Automation import ControlType



class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, name):
        modal = self.open_group_editor()
        modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
        modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(name)
        Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)
        self.close_group_editor(modal)

    def count(self):
        self.open_group_editor()
        return len(self.get_group_list())

    def get_group_list(self):
        modal = self.open_group_editor()
        tree = modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root = tree.Nodes[0]
        l = [node.Text for node in root.Nodes]
        self.close_group_editor(modal)
        return l

    def open_group_editor(self):
        main_window = self.app.main_window
        main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
        modal = main_window.ModalWindow("Group editor")
        return modal

    def close_group_editor(self, modal):
        modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()

    def delete_first(self):
        modal = self.open_group_editor()
        tree = modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
        root = tree.Nodes[0]
        root.Nodes[0].Select()
        modal.Get(SearchCriteria.ByAutomationId("uxDeleteAddressButton")).Click()
        modal.Get(SearchCriteria.ByAutomationId("uxOKAddressButton")).Click()
        self.close_group_editor(modal)

