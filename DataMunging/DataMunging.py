"""
Created for Dublin Data Science Beginners Meetup session on 11-Aug-2015

This is an example to showcase the results of Data Munging in Python
with Pandas using wxPython GUI toolkit. The results are shown in a
Grid for easy visualization of data.

@author: Allen Thomas Varghese
@email: allentv4u@gmail.com
"""
import wx
import wx.grid as wg

import os
import pandas as pd


class DataMungingUI(wx.Frame):
    """ Class to create the GUI """
    def __init__(self):
        super(DataMungingUI, self).__init__(
            None, -1, "Data Munging UI", wx.DefaultPosition, wx.Size(800, 600)
        )

        # Constants for positioning controls
        LEFT_MARGIN = 30
        TOP_MARGIN = 30
        DEFAULT_SPACING = 20

        # Parameters: Parent, ID
        panel = wx.Panel(self, -1)

        # Parameters: Parent, ID, title, position
        wx.StaticText(panel, -1, 'Choose CSV file to process:', (LEFT_MARGIN, TOP_MARGIN))

        # Parameters: Parent, ID, placeholder text, position, (width, height)
        self.file_path_ctrl = wx.TextCtrl(panel, -1, '', (LEFT_MARGIN, TOP_MARGIN + DEFAULT_SPACING), (500, -1))

        # Parameters: Parent, ID, label, position
        wx.Button(panel, 9, 'Choose', (LEFT_MARGIN + 520, TOP_MARGIN + DEFAULT_SPACING))

        # Attaching event handler to the 'Choose' button
        # Parameters: Type of event, event handler function, ID of the control
        self.Bind(wx.EVT_BUTTON, self.get_file_path, id=9)

        wx.Button(panel, 10, 'Process File', (LEFT_MARGIN, TOP_MARGIN + 3 * DEFAULT_SPACING))
        # Attaching event handler to the 'Process File' button
        self.Bind(wx.EVT_BUTTON, self.process_csv_file, id=10)

        # Creating the Grid to display information from the CSV file
        self.data_grid = wg.Grid(panel, -1, (LEFT_MARGIN, TOP_MARGIN + 5 * DEFAULT_SPACING), (500, 150))
        # Parameters: rows, columns
        self.data_grid.CreateGrid(5, 5)
        # Disable editing of values in the Grid
        self.data_grid.EnableEditing(False)
        # Set default alignment for all cells
        # Parameters: Horizontal alignment, Vertical alignment
        self.data_grid.SetDefaultCellAlignment(wx.ALIGN_RIGHT, wx.ALIGN_CENTRE)

        self.status_bar = self.CreateStatusBar()
        self.Centre()
        self.Show(True)

    def get_file_path(self, event):
        """ Show the File Dialog """
        wcd = 'All files (*)|*|CSV files (*.csv)|*.csv|Text files (*.txt)|*.txt'
        dir = os.getcwd()
        open_dlg = wx.FileDialog(
            self, message='Choose a file', defaultDir=dir, defaultFile='',
            wildcard=wcd, style=wx.OPEN|wx.CHANGE_DIR
        )
        path = ""
        if open_dlg.ShowModal() == wx.ID_OK:
            path = open_dlg.GetPath()
        open_dlg.Destroy()
        self.file_path_ctrl.SetValue(path)
        self.status_bar.SetStatusText('CSV file path loaded')

    def perform_data_munging(self):
        """ Data Munging happens here. Return a Pandas DataFrame. """
        # TODO: Add file loading code here
        data = {
            'col1': [1, 2, 3, 4, 5],
            'col2': ['v1', 'v2', 'v3', 'v4', 'v5'],
            'col3': [0.01, 0.25, 1.23, 25.03, 100.00]
        }

        # TODO: 
        # Add file processing code here
        # ...
        # ...
        # ...

        # Return only the top 1,000 records to avoid memory problems
        df = pd.DataFrame(data).head(1000)
        return df  # Change the return value based on above code

    def process_csv_file(self, event):
        """ Processing the selected CSV file """
        self.status_bar.SetStatusText('CSV file processing started...')
        df = self.perform_data_munging()
        no_of_rows = len(df)
        no_of_columns = len(df.columns)
        self.data_grid.ClearGrid()  # Clear existing data in the grid
        self.data_grid.DeleteCols(0, self.data_grid.GetNumberCols())  # Delete all the columns
        self.data_grid.DeleteRows(0, self.data_grid.GetNumberRows())  # Delete all the rows
        self.data_grid.InsertCols(0, no_of_columns)  # Add new columns
        self.data_grid.InsertRows(0, no_of_rows)  # Add new rows
        for col_index, col in enumerate(df.columns):
            # Set the column label to match the value for the column in the CSV file
            self.data_grid.SetColLabelValue(col_index, col)
            for row_index, value in enumerate(df[col]):
                self.data_grid.SetCellValue(row_index, col_index, str(value))
        self.status_bar.SetStatusText('CSV file processing completed!')


# Display the GUI
app = wx.App()
DataMungingUI()
app.MainLoop()
