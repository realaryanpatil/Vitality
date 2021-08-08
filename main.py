from tkinter import *
import tkinter.font as font

def submit():
    global entry1
    global entry2
    global entry4
    global entry5
    global entry6
    global entry8
    global entry9
    global entry10
    global entry12

    ans1 = entry1.get()
    ans2 = entry2.get()
    ans3 = Var1.get()
    ans4 = entry4.get()
    ans5 = entry5.get()
    ans6 = entry6.get()
    ans7 = Var2.get()
    ans8 = entry8.get()
    ans9 = entry9.get()
    ans10 = entry10.get()
    ans11 = Var3.get()
    ans12 = entry12.get()
    ans13 = Var4.get()
    
    r1 = int(ans1)
    if ans2 == 'M' or ans2 == 'm' or ans2 == 'Male' or ans2 == 'male' or ans2 == 'MALE':
        r2 = 1
    else:
        r2 = 0
    r3 = int(ans3)
    r4 = int(ans4)
    r5 = int(ans5)
    ans6 = int(ans6)
    if ans6 > 120:
        r6 = 1
    else:
        r6 = 0
    r7 = int(ans7)
    r8 = int(ans8)
    if ans9 == 'Yes' or ans9 == 'y' or ans9 == 'Y':
        r9 = 1
    else:
        r9 = 0
    rs10 = float(ans10)
    r10 = int(rs10)
    r11 = int(ans11)
    r12 = int(ans12)
    r13 = int(ans13)
    
    import pandas as pd
    dataset = pd.read_csv('data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    from sklearn.neighbors import KNeighborsClassifier
    classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
    classifier.fit(X_train, y_train)

    resultval = classifier.predict(sc.transform([[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13]]))
    resultval2 = int(resultval)
    if resultval2 == 0:
        resultvalx = "Patient is displaying a low risk of heart disease."
    elif resultval2 == 1:
        resultvalx = "Patient is displaying a high risk of heart disease."
    else:
        resultvalx = "Patient is displaying a medium risk of heart disease."
    resultlabel.configure(text = resultvalx)
    resultlabel['font'] = myFont

root = Tk(className= 'Vitality')
root.geometry("1000x525")
root.configure(bg= '#020063' )
Var1 = IntVar()
Var2 = IntVar()
Var3 = IntVar()
Var4 = IntVar()
myFont = font.Font(family='Helvetica', size=10, weight='bold')

label = Label(text= 'Welcome to Vitality, an AI algorithm to predict heart disease. Please answer the questions below.')
label.configure(background='#020063', foreground= 'white')
label.grid(row = 0, column = 0, sticky = W)
labelx = Label(text= "")
labelx.configure(background='#020063', foreground= 'white')
labelx.grid(row= 1, column= 0)

#==============================================================================================
label1 = Label(text= "Age (in years)")
label1.configure(background='#020063', foreground= 'white')
label1.grid(row = 2, column = 2, sticky = W)

entry1 = Entry(root, width= 20)
entry1.configure(background='#020063', foreground= 'white')
entry1.grid(row = 2, column = 3, sticky = W)

#===============================================================================================
label2 = Label(text = """Gender (M/F)                                  """)
label2.configure(background='#020063', foreground= 'white')
label2.grid(row = 3, column = 2, sticky = W, pady = 2)

entry2 = Entry(root, width= 20)
entry2.configure(background='#020063', foreground= 'white')
entry2.grid(row = 3, column = 3, sticky = W, pady = 2)

#===============================================================================================
label3 = Label(text ="""Is the patient suffering from any forms of Angina?""")
label3.configure(background='#020063', foreground= 'white')
label3.grid(row = 2, column = 0, sticky = W, pady = 2)

Rb1 = Radiobutton(root, text ="Typical Angina", variable= 'Var1', value=1)
Rb1.grid(row = 3, column = 0, sticky = W, pady = 2)
Rb2 = Radiobutton(root, text ="Atypical Angina", variable= 'Var1', value=2)
Rb2.grid(row = 4, column = 0, sticky = W, pady = 2)
Rb3 = Radiobutton(root, text ="Non-anginal pain", variable= 'Var1', value=3)
Rb3.grid(row = 5, column = 0, sticky = W, pady = 2)
Rb4 = Radiobutton(root, text ="Asymtomatic", variable= 'Var1', value=4)
Rb4.grid(row = 6, column = 0, sticky = W, pady = 2)

#==============================================================================================
label4 = Label(text ="Resting Blood Pressure (in mm Hg)")
label4.configure(background='#020063', foreground= 'white')
label4.grid(row = 4, column = 2, sticky = W, pady = 2)

entry4 = Entry(root, width= 20)
entry4.configure(background='#020063', foreground= 'white')
entry4.grid(row = 4, column = 3, sticky = W, pady = 2)

#==============================================================================================
label5 = Label(text ="Serum Cholesterol (in mg/dl)")
label5.configure(background='#020063', foreground= 'white')
label5.grid(row = 5, column = 2, sticky = W, pady = 2)

entry5 = Entry(root, width= 20)
entry5.configure(background='#020063', foreground= 'white')
entry5.grid(row = 5, column = 3, sticky = W, pady = 2)

#==============================================================================================
label6 = Label(text ="Fasting Blood Sugar (in mg/dl)")
label6.configure(background='#020063', foreground= 'white')
label6.grid(row = 6, column = 2, sticky = W, pady = 2)

entry6 = Entry(root, width= 20)
entry6.configure(background='#020063', foreground= 'white')
entry6.grid(row = 6, column = 3, sticky = W, pady = 2)

#==============================================================================================
label7 = Label(text ="Resting ECG Result")
label7.configure(background='#020063', foreground= 'white')
label7.grid(row = 7, column = 0, sticky = W, pady = 2)

Rx1 = Radiobutton(root, text ="ST-T wave abnormality", variable= 'Var2', value=1)
Rx1.grid(row = 8, column = 0, sticky = W, pady = 2)
Rx2 = Radiobutton(root, text ="Probable or definite left ventricular hypertrophy", variable= 'Var2', value=2)
Rx2.grid(row = 9, column = 0, sticky = W, pady = 2)
Rx3 = Radiobutton(root, text ="Normal", variable= 'Var2', value=0)
Rx3.grid(row = 10, column = 0, sticky = W, pady = 2)

#=============================================================================================
label8 = Label(text="Maximum heart rate achieved during exercise")
label8.configure(background='#020063', foreground= 'white')
label8.grid(row = 7, column = 2, sticky = W, pady = 2)

entry8 = Entry(root, width= 20)
entry8.configure(background='#020063', foreground= 'white')
entry8.grid(row = 7, column = 3, sticky = W, pady = 2)

#=============================================================================================
label9 = Label(text="Is the patient suffering from exercise induced angina? (y/n)")
label9.configure(background='#020063', foreground= 'white')
label9.grid(row = 8, column = 2, sticky = W, pady = 2)

entry9 = Entry(root, width= 20)
entry9.configure(background='#020063', foreground= 'white')
entry9.grid(row = 8, column = 3, sticky = W, pady = 2)

#==============================================================================================
label10 = Label(text="ST depression induced by exercise relative to rest (in mm)")
label10.configure(background='#020063', foreground= 'white')
label10.grid(row = 9, column = 2, sticky = W, pady = 2)

entry10 = Entry(root, width= 20)
entry10.configure(background='#020063', foreground= 'white')
entry10.grid(row = 9, column = 3, sticky = W, pady = 2)

#==============================================================================================
label11 = Label(text ="The slope of the peak exercise ST segment")
label11.configure(background='#020063', foreground= 'white')
label11.grid(row = 11, column = 0, sticky = W, pady = 2)

Ra1 = Radiobutton(root, text ="Upsloping", variable= 'Var3', value=1)
Ra1.grid(row = 12, column = 0, sticky = W, pady = 2)
Ra2 = Radiobutton(root, text ="Flat", variable= 'Var3', value=2)
Ra2.grid(row = 13, column = 0, sticky = W, pady = 2)
Ra3 = Radiobutton(root, text ="Downsloping", variable= 'Var3', value=0)
Ra3.grid(row = 14, column = 0, sticky = W, pady = 2)

#===============================================================================================
label12 = Label(text='Major Blood Vessels coloured by Floroscopy')
label12.configure(background='#020063', foreground= 'white')
label12.grid(row = 10, column = 2, sticky = W, pady = 2)

entry12 = Entry(root, width= 20)
entry12.configure(background='#020063', foreground= 'white')
entry12.grid(row = 10, column = 3, sticky = W, pady = 2)

#===============================================================================================
label13 = Label(text = 'Results from Thallium test')
label13.configure(background='#020063', foreground= 'white')
label13.grid(row = 15, column = 0, sticky = W, pady = 2)

Rc1 = Radiobutton(root, text ="Fixed defect", variable= 'Var4', value=1)
Rc1.grid(row = 16, column = 0, sticky = W, pady = 2)
Rc2 = Radiobutton(root, text ="Reversible defect", variable= 'Var4', value=2)
Rc2.grid(row = 17, column = 0, sticky = W, pady = 2)
Rc3 = Radiobutton(root, text ="No defect", variable= 'Var4', value=0)
Rc3.grid(row = 18, column = 0, sticky = W, pady = 2)

#===============================================================================================
Button1 = Button(root, text = "Predict", command = submit)
Button1.grid(row = 13, column= 2, sticky = W, pady = 2)

resultlabel = Label(text="")
resultlabel.configure(background='#020063', foreground= 'white')
resultlabel.grid(row = 14, column = 2, sticky = W, pady = 2)

githublabel = Label(text='https://github.com/realaryanpatil/Vitality')
githublabel.configure(background='#020063', foreground= 'white')
githublabel.grid(row = 18, column = 2, sticky = W, pady = 2)                                   

root.mainloop()