from gui import *
def main():

    window = Tk()
    window.resizable(False, False)
    window.title('Bank Of Brian')
    window.geometry('300x300')
    widgets = GUI(window)
    window.mainloop()
if __name__ == '__main__':
    main()