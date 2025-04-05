from tkinter import *

# for font creation
from tkinter.font import Font

#for messagebox creation
from tkinter import messagebox

import deep_translator
print("deep-translator is available!")

import sys
print(sys.executable)

from deep_translator import GoogleTranslator

translated = GoogleTranslator(source='english', target='french').translate("Hello")
from deep_translator import GoogleTranslator
from tkinter.ttk import Combobox

class LanguageTranslatorGUI:
    def __init__ (self):
        
        # List of supported languages
        self.supported_languages = sorted(
            list({lang.lower() for lang in[
                'english', 'spanish', 'french', 'german', 'italian', 'chinese',
                'arabic', 'hindi', 'japanese', 'russian', 'German','Polish',
                'Spanish','English','Dutch', 'Turkish','French','Italian',
                'Slovak','Romanian','Swahili','Finnish',
                'Afrikaans','Greek','Indonesian','Lithuanian','Catalan',
                'Tagalog','Portuguese','Croatian','Russian','Norwegian',
                'Danish','Slovenian','Welsh','Albanian','Korean','Somali',
                'Czech','Estonian','Swedish','Hungarian','Latvian',
                'Vietnamese','Japanese','Arabic','Thai','Bulgarian', 'Urdu',
                'Farsi', 'Dari', 'Pashto'
                ]}), key=str.lower)

        # Create the main window widget
        self.main_window = Tk()

        # Display a title
        self.main_window.title('Language Translator' )
        #self.main_window.geometry('900x375')

        # Create frames for organizing widgets
        self.first_frame = Frame(self.main_window)
        self.second_frame = Frame(self.main_window)
        self.third_frame = Frame(self.main_window)
        self.fourth_frame = Frame(self.main_window)
        self.fifth_frame = Frame(self.main_window)

        # create the widgets for the first frame
        self.prompt_label1 = Label(self.first_frame,
                                  text = 'Enter the language to translate from: ')
        self.from_lang_entry = Combobox(self.first_frame, values=self.supported_languages, width=37)
        self.from_lang_entry.set("english")  # default value

        # pack first frame's widgets
        self.prompt_label1.pack(side='left')
        self.from_lang_entry.pack(side='left')
        

        # create the widgets for the second frame
        self.prompt_label2 = Label(self.second_frame,
                                  text = 'Enter the language to translate to: ')
        self.to_lang_entry = Combobox(self.second_frame, values=self.supported_languages, width=37)
        self.to_lang_entry.set("spanish")  # default value

        # pack second frame's widgets
        self.prompt_label2.pack(side='left')
        self.to_lang_entry.pack(side='left')
        

        # create the widgets for the third frame
        self.prompt_label3 = Label(self.third_frame,
                                  text = 'Enter the text to translate: ')
        self.text_entry = Entry(self.third_frame,
                                    width=40)
        # pack third frame's widgets
        self.prompt_label3.pack(side='left')
        self.text_entry.pack(side='left')


        # create the widgets for the fourth frame (Output)
        self.prompt_label4 = Label(self.fourth_frame,
                                  text = 'Translated text: ')
        # We need a StringVar object to associate with an output label.
        # Use the object's set method to store a string pf blank characters.
        self.translated_text = StringVar() #Stringvar for output
        # Create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.translated_label = Label(self.fourth_frame,
                                     textvariable=self.translated_text)
        # pack fourth frame's widgets
        self.prompt_label4.pack(side='left')
        self.translated_label.pack(side='left')


##        # Create the button widgets for the fifth_frame. (convert and quit)
        self.translate_button = Button(self.fifth_frame,
                                          text='Convert',
                                          command=self.translate)
        self.quit_button = Button(self.fifth_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
##        # Pack the buttons.
        self.translate_button.pack(side='left')
        self.main_window.bind('<Return>', lambda event: self.translate())

        self.quit_button.pack(side='left')
        self.main_window.bind('<Escape>', lambda event: self.main_window.destroy())

##
        # Pack the frames.
        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.fourth_frame.pack()
        self.fifth_frame.pack()

        # Enter the tkinter main loop.
        mainloop()

    def translate(self):
        from_lang = self.from_lang_entry.get().strip().lower()
        to_lang = self.to_lang_entry.get().strip().lower()
        text = self.text_entry.get().strip()

        if not from_lang or not to_lang or not text:
            messagebox.showwarning("Input Error", "Please fill out all fields.")
            return

        try:
            translated = GoogleTranslator(source=from_lang, target=to_lang).translate(text)
            self.translated_text.set(translated)

        except Exception as e:
            messagebox.showerror("Translation Error", str(e))


# Create an instance of the LanguageTranslatorGUI class
if __name__ == '__main__':
    lang_translate = LanguageTranslatorGUI()
                                  
