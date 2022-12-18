#System Codename: Vesti
from tkinter import * #type: ignore
from tkinter import simpledialog,messagebox
class System:
    class kernal:
        def CRASH(root1,errcode): #type: ignore
            root1.destroy() #type: ignore
            print('-Sys~Crsh')
            cs = Tk()
            cs.title('~')
            cs.geometry('750x750')
            lt1 = Label(cs,text='Your System Crashed With Message:\n'+errcode+'\n \nError Code:\n0X000') # Ex. KERNAL~CRASH~ERROR: SYSTEMOSMCFKERNAL
            lt1.pack()
            q = Button(cs,text='Quit System',command=System.core_main.os_UserItems.cmdApp.quit)
            q.pack()
            cs.mainloop()
        class bootmgr:
            def main(): #type: ignore
                mgrw = Tk()
                mgrw.title('kernal ~ bootmgr.exe')
                mgrw.geometry('500x500')
                ML = Label(mgrw,text='kernal ~ boot manager\nversion: '+str(System.kernal.bootmgr.info.version)) #type: ignore
                ML.pack()
                bn = Button(mgrw,text='Boot Normally',command=mgrw.destroy)
                bn.pack()
                q = Button(mgrw,text='Quit System FULLY',command=System.core_main.os_UserItems.cmdApp.quit)
                q.pack()
                mgrw.mainloop()
            class info:
                version = 0.1
    class Bios_UEFI:
        class framework:
            class info:
                ver = '0.4.2'
                build = 'KU-FU-AU-RD~12/18/2022:10:53AM' #AU = APPS UPDATE #F/KU = KERNAL/FRAMEWORK UPDATE #GUIU/UIU = GUI USER INTERFACE UPDATE/USER INTERFACE UPDATE #RD = RELEASE DATE #BF = BUG FIX #M GUI/UI C = MINI GUI/UI CJANGE
                updateLog = '\nBoot Manager Added\n Crash Added Incase of unknown actions.'
            class app: # System.Bios_UEFI.framework.app.main_app
                ver = '0.1.7.5'
                def main_app(): #type: ignore
                    root_fwai = Tk()
                    root_fwai.geometry('500x500')
                    root_fwai.title('FW - System Info')
                    tl = Label(root_fwai,text='System Info')
                    ad = Label(root_fwai,text='App Version: '+System.Bios_UEFI.framework.app.ver)  # type: ignore
                    tladsl = Label(root_fwai,text='-----------------------')
                    v = Label(root_fwai,text='System Version: '+System.Bios_UEFI.framework.info.ver)
                    b = Label(root_fwai,text='System Build: '+System.Bios_UEFI.framework.info.build)
                    bv = Label(root_fwai,text='Update Log: '+System.Bios_UEFI.framework.info.updateLog)
                    tl.pack()
                    ad.pack()
                    tladsl.pack()
                    v.pack()
                    b.pack()
                    bv.pack()
                    root_fwai.mainloop()
            class lhb:
                def lhb_app(): #type: ignore
                    lhbw = Tk()
                    lhbw.title('Help - Login')
                    hll1=Label(lhbw,text='Help - Login\n-----------\n \nI Dont see my username\nThis may be because the update that comes with your profile has not come out, or you have an outdated version of the OS.\nSorry! There seems to be no more help articles at this time. ¯\_(ツ)_/¯') #type: ignore
                    hll1.pack()
    class core_main:
        def OS_m_PLS(): #type: ignore #PLS = Passed Login Screen # m = main 
            root = Tk()
            root.title('Vesti OS - Insider Beta - Public')
            root.geometry('800x800')
            qb = Button(root,text='Quit',command=System.core_main.os_UserItems.cmdApp.quit)
            qb.pack()
            fwaiB = Button(root,text='System Information',command=System.Bios_UEFI.framework.app.main_app)
            fwaiB.pack()
            wm = Button(root,text='Window Maker',command=System.core_main.os_UserItems.apps.WindowMaker.app.main_app.WindowMaker)
            wm.pack()
            vs = Button(root,text='Vesti Store',command=System.core_main.os_UserItems.apps.Vesti.store.app.main)
            vs.pack()
            # Write Above
            root.mainloop()
        def prepBoot(): #type: ignore
            lwindow.destroy()
            System.kernal.bootmgr.main()
            messagebox.showinfo('Message','Its okay to be a guest, But get your own account and password [People can inspect code and see the password. Please, dont use a common password. Dont worry, Everybody has the same apps in their user accounts. Check github repo for more information on this topic.]')
            System.core_main.OS_m_PLS()
        class os_UserItems:
            class apps:
                class WindowMaker:
                    class app:
                        class data:
                            ver = '0.1'
                        class main_app:
                            def WindowMaker(): #type: ignore
                                wmroot=Tk() #wmroot=window maker root
                                wmLabel = Label(wmroot,text='Window Maker '+System.core_main.os_UserItems.apps.WindowMaker.app.data.ver+'\n------\n \nPlease enter the prompts displayed to make a window.')  # type: ignore
                                wmLabel.pack()
                                type = simpledialog.askstring('Window Maker','Type of window (Warning,Error,Info)')
                                title = simpledialog.askstring('Window Maker','Title Bar Text')
                                text = simpledialog.askstring('Window Maker','Enter the text you want to display on the window.')
                                if type=='Error':
                                    messagebox.showerror(title,text)
                                if type=='Warning':
                                    messagebox.showwarning(title,text)
                                if type=='Info':
                                    messagebox.showinfo(title,text)
                                if not type == 'Error' and not type=='Info' and not type=='Warning':
                                    messagebox.showerror('Invalid - Window Maker','You didnt have a correct message type.')
                                wmroot.destroy()
                                wmroot.mainloop()
                class Vesti:
                    class store:
                        class app:
                            class app_info:
                                ver = '0.1'
                            def main_info_app(): #type: ignore
                                vwi = Tk()
                                vwi.geometry('500x500')
                                vwi.title('About Vesti Store')
                                vwiv = Label(vwi,text='Version: '+System.core_main.os_UserItems.apps.Vesti.store.app.app_info.ver)
                                vwiv.pack()
                                vwi.mainloop()
                            def main(): #type: ignore
                                vw = Tk()
                                vw.geometry('750x750')
                                vw.title('Vesti Store')
                                vwib = Button(vw,text='About Vesti Store',command=System.core_main.os_UserItems.apps.Vesti.store.app.main_info_app)
                                vwib.pack()
                                messagebox.showinfo('Vesti Store - Message','Welcome to The Vesti Store!\n You have been automatically logged in by VestiSecure\nYou can find apps to download for your Vesti OS.')
                                vw.mainloop()
            class cmdApp:
                def quit(): #type: ignore
                    q = messagebox.askyesno('Quit','Are you sure you you want to quit?')
                    if q==True:
                        quit('System - Quit - UserActivated - Stop Code: U-A_Q1')
lwindow = Tk()
l = Label(lwindow,text='Please Select A User')
u1b = Button(lwindow,text='Guest/Unregistered',command=System.core_main.prepBoot) #u1b = User 1 Button [Use var template]
l2 = Label(lwindow,text='Dont see your username? Click "help!"')
hb = Button(lwindow,text='Help',command=System.Bios_UEFI.framework.lhb.lhb_app) #LHB = Login Help Button
l.pack()
u1b.pack()
l2.pack()
hb.pack()
lwindow.mainloop() #123 Lines '>'        <====See the face?
#                              o         <====See the face?