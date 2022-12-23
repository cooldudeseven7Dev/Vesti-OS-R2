#System Codename: Vesti
print('Imports..............RUNNING')

from tkinter import * #type: ignore
from tkinter import simpledialog,messagebox
print('Imports..............2/2 COMPLETE')
print('DEFINING MAIN SYSTEM AND PREPARING FOR BOOT.........................RUNNING [Priority]')
class System:
    App1_Installed = 0
    App2_Installed = 0
    class kernal:
        def CRASH(root1,errcode): #type: ignore
            root1.destroy() #type: ignore
            print('Crashed.')
            cs = Tk()
            cs.title('~')
            cs.geometry('750x750')
            lt1 = Label(cs,text='Your System Crashed With Message:\n'+errcode+'\n \nError Code:\n0X000') # Ex. KERNAL~CRASH~ERROR: SYSTEMOSMCFKERNAL
            lt1.pack()
            q = Button(cs,text='Quit System [Reboot is NOT availble unless you re-open the runner.]',command=System.core_main.os_UserItems.cmdApp.quit)
            q.pack()
            cs.mainloop()
        class bootmgr:
            def main(): #type: ignore
                mgrw = Tk()
                mgrw.title('kernal ~ bootmgr.exe')
                mgrw.geometry('500x500')
                ML = Label(mgrw,text='kernal ~ boot manager\nversion: '+str(System.kernal.bootmgr.info.version)) #type: ignore
                ML.pack()
                bn = Button(mgrw,
                            text='Boot Normally - Just DESTROY this window',command=mgrw.destroy)
                bn.pack()
                q = Button(mgrw,text='Quit System FULLY',command=System.core_main.os_UserItems.cmdApp.quit)
                q.pack()
                mgrw.mainloop()
            class info:
                version = '0.1.1'
    class Bios_UEFI:
        class framework:
            class info:
                ver = '0.5.incomplete2_GHREPO_0.2'
                build = 'AU~12/GUIU/UIU~RD:12/22/2022:3:16PM' #AU = APPS UPDATE #F/KU = KERNAL/FRAMEWORK UPDATE #GUIU/UIU = GUI USER INTERFACE UPDATE/USER INTERFACE UPDATE #RD = RELEASE DATE #BF = BUG FIX #M GUI/UI C = MINI GUI/UI CJANGE
                updateLog = 'INSTALLING IS NOW A THING! YOU CAN TEST IN VESTI STORE [PreRunning: coming soon]\nPrev Update: App Update, Help Menu Update, Repo Updated'
            class app: # System.Bios_UEFI.framework.app.main_app
                ver = '0.1.7.7'
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
                    hll1=Label(lhbw,text='Help - Login\n-----------\n \nI Dont see my username\nThis may be because the update that comes with your profile has not come out, or you have an outdated version of the OS.\nWhy can i see my password in the code?\n We dont have actual servers and people who check this code can find it. Sorry! [Make sure to use a password that is not common for you when you create an account!]\nSorry! There seems to be no more help articles at this time. ¯\_(ツ)_/¯') #type: ignore
                    hll1.pack()
    class core_main:
        def OS_m_PLS(): #type: ignore #PLS = Passed Login Screen # m = main 
            root = Tk()
            root.title('Vesti OS - Insider Beta - Public')
            root.geometry('800x800')
            qb = Button(root,text='Quit',command=System.core_main.os_UserItems.cmdApp.quit)
            qb.pack()
            fwaiB = Button(root,text='Vesti OS System Information',command=System.Bios_UEFI.framework.app.main_app)
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
                                type = simpledialog.askstring('Window Maker','Type of window (Warning,Error,Info <== SPELLED LIKE THIS)')
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
                            class cmd:
                                def downloadapp1(): #type: ignore
                                    if System.App1_Installed ==0:
                                        i1 = messagebox.askyesno('Install','Are you sure you want to install:\nTest App\nby cooldudeseven7 [Verified]')
                                        if i1 == True:
                                            System.App1_Installed+=1
                                            messagebox.showinfo('Success!','Installed!')
                                    else: 
                                        messagebox.showerror('Error','Already Installed!')
                                def downloadapp2(): #type: ignore
                                    if System.App2_Installed ==0:
                                        i2 = messagebox.askyesno('Install','Are you sure you want to install:\nChat Bot\nby cooldudeseven7 [Verified]')
                                        if i2 == True:
                                            System.App2_Installed+=1
                                            messagebox.showinfo('Success!','Installed!')
                                def rta1(): #type: ignore
                                    if System.App1_Installed==1:
                                        dap1 = Tk()
                                        dap1.title('Test App')
                                        dap1.geometry('500x500')
                                        l1dap1 = Label(dap1,text='This is a app to test INSTALL capabilites on this OS. \n No change was done to your windows or actual running os, It just change VESTI OS STORE.\n ~cooldudeseven7')
                                        l1dap1.pack()
                                        dap1.mainloop()
                                    else:
                                        messagebox.showerror('Error','This app is not installed.')
                                def rta2(): #type: ignore
                                    if System.App2_Installed==1:
                                        dap2 = Tk()
                                        dap2.title('Chat Bot')
                                        dap2.geometry('500x500')
                                        l1dap2 = Label(dap2,text='Running chat bot [close window when prompts stop]\nWE DO NOT SAVE OR COLLECT YOUR DATA!')
                                        l1dap2.pack()
                                        nm1=simpledialog.askstring('Chat Bot','Hi! Whats your name')
                                        simpledialog.askstring('Chat Bot','Hello, '+nm1+' How is your day?') #type:ignore
                                        simpledialog.askstring('Chat Bot','Intresting, '+nm1+' Do you have any pets?') #type: ignore
                                        messagebox.showinfo('Chat Bot','Well, Thats all I have been scripted for. Have a good day!')
                                        dap2.mainloop()
                                    else:
                                        messagebox.showerror('Error','This app is not installed.')
                            class app_info:
                                ver = '0.2.incomplete.aup1fr'
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
                                downloadapp1b = Button(vw,text='Download: Test App',command=System.core_main.os_UserItems.apps.Vesti.store.app.cmd.downloadapp1)
                                runta1 = Button(vw,text='Run: Test App [if you have it]',command=System.core_main.os_UserItems.apps.Vesti.store.app.cmd.rta1)
                                downloadapp1b.pack()
                                runta1.pack()
                                downloadapp2b = Button(vw,text='Download: Chat Bot',command=System.core_main.os_UserItems.apps.Vesti.store.app.cmd.downloadapp2)
                                runa2 = Button(vw,text='Run Chat Bot [if you have it]',command=System.core_main.os_UserItems.apps.Vesti.store.app.cmd.rta2) 
                                downloadapp2b.pack()
                                runa2.pack()
                                messagebox.showinfo('Vesti Store - Message','Welcome to The Vesti Store!\n You have been automatically logged in by VestiSecure\nYou can find apps to download for your Vesti OS.')
                                vw.mainloop()
            class cmdApp:
                def quit(): #type: ignore
                    q = messagebox.askyesno('Quit','Are you sure you you want to quit?')
                    if q==True:
                        quit('System - Quit - UserActivated - Stop Code: UA_NAC_Q1')
print('PREPPED FOR BOOT.')
print('Booting... [LOGIN USING FRESH COMPONENTS]')
lwindow = Tk()
l = Label(lwindow,text='Please Select A User')
u1b = Button(lwindow,text='Guest/Unregistered',command=System.core_main.prepBoot) #u1b = User 1 Button [Use var template]
l2 = Label(lwindow,text='Dont see your username? Click "help!"')
hb = Button(lwindow,text='Help',command=System.Bios_UEFI.framework.lhb.lhb_app) #LHB = Login Help Button
l.pack()
u1b.pack()
l2.pack()
hb.pack()
lwindow.mainloop()