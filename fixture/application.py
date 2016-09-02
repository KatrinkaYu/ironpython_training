from fixture.group import GroupHelper

import os.path
import clr
project_dir = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(os.path.join(project_dir, "..", "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "..", "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName('TestStack.White')
from TestStack.White import Application
from TestStack.White.UIItems.Finders import *

class Applications:
    def  __init__(self, base_address):
        self.group = GroupHelper(self)
        application = Application.Launch(base_address)
        self.main_window = application.GetWindow("Free Address Book")


    def destroy (self):
        self.main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()