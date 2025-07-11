import os
import customtkinter as ctk

from PIL import Image

# Path to app/img folder, in order to get image files 
IMG_FOLDER_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "img") # We take the directory name of the parent directory where this file is located + img directory


class TitleBar(ctk.CTkFrame):

    ## CONSTRUCTOR --------------------------------------------------------------------------------------------------------- ##
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Defining Title label
        self.lblTitle = ctk.CTkLabel(self, text="SolarActivid", font=ctk.CTkFont(size=20, weight="bold"))
        self.lblTitle.pack(pady=10, side="left", expand=True)