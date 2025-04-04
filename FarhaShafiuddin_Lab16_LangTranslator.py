from tkinter import *

# for font creation
from tkinter.font import Font

#for messagebox creation
from tkinter import messagebox

class LanguageTranslatorGUI:
    def __init__ (self):

        # Create the main window widget
        self.main_window = Tk()

        # Display a title
        self.main_window.title('Language Translator' )
        #self.main_window.geometry('900x375')

        # Create 5 frames to group widgets.
        self.first_frame = Frame()
        self.second_frame = Frame()
        self.third_frame = Frame()
        self.fourth_frame = Frame()
        self.fifth_frame = Frame()

        # create the widgets for the first frame
        self.prompt_label1 = Label(self.first_frame,
                                  text = 'Enter the language to translate from: ')
        self.from_lang_entry = Entry(self.first_frame,
                                    width=40)
        # pack first frame's widgets
        self.prompt_label1.pack(side='left')
        self.from_lang_entry.pack(side='left')
        

        # create the widgets for the second frame
        self.prompt_label2 = Label(self.second_frame,
                                  text = 'Enter the language to translate to: ')
        self.from_lang_entry = Entry(self.second_frame,
                                    width=10)
        # pack second frame's widgets
        self.prompt_label2.pack(side='left')
        self.from_lang_entry.pack(side='left')
        

        # create the widgets for the third frame
        self.prompt_label3 = Label(self.third_frame,
                                  text = 'Enter the text to translate: ')
        self.from_lang_entry = Entry(self.third_frame,
                                    width=10)
        # pack third frame's widgets
        self.prompt_label3.pack(side='left')
        self.from_lang_entry.pack(side='left')


        # create the widgets for the fourth frame
        self.prompt_label3 = Label(self.fourth_frame,
                                  text = 'translated to: ')
        # We need a StringVar object to associate with an output label.
        # Use the object's set method to store a string pf blank characters.
        self.value = StringVar()

        # Create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.from_lang_entry = Label(self.fourth_frame,
                                     textvariable=self.value)
        


        # pack fourth frame's widgets
        self.prompt_label3.pack(side='left')
        self.from_lang_entry.pack(side='left')


##        # Create the button widgets for the fifth_frame.
        self.translate_button = Button(self.fifth_frame,
                                          text='Convert',
                                          command=self.translate)
        self.quit_button = Button(self.fifth_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
##
##        # Pack the buttons.
        self.translate_button.pack(side='left')
        self.quit_button.pack(side='left')
##
        # Pack the frames.
        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.fourth_frame.pack()
        self.fifth_frame.pack()

        # Enter the tkinter main loop.
        mainloop()

##    def translate(self):
##        # Get the value entered by the user into the
##        # translate_entry widget.
##        try:
##            kilo = float(self.translate_entry.get())
##
##            # Convert kilometers to miles.
##            miles = kilo * 0.6214
##            miles_str = "{:.4f}".format(miles)
##
##            # Convert miles to a string and store it
##            # in the StringVar object. This will automatically
##            # update the miles_label widget.
##            self.value.set(miles_str)
##        except ValueError:
##            # Display error message and change label color to pink
##            self.value.set("Invalid input")
##            self.miles_label.config(bg="red", font="bold")
##
##        # Create a label and associate it with the StringVar object. Any value
##        # stored in the StringVar object will automatically be displayed in the
##        # label.
##        self.enter_text_label = Label(self.mid_frame, textvariable=self.value)
##
# Create an instance of the LanguageTranslatorGUI class
if __name__ == '__main__':
    lang_translate = LanguageTranslatorGUI()
                                  
