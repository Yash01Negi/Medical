import pickle
from winreg import REG_QWORD
from flask import Flask, render_template, redirect, request, url_for
import numpy as np
fileStroke = open("stroke.pkl",'rb')
modelS = pickle.load(fileStroke)

fileHeart = open("heart.pkl", 'rb')
modelD = pickle.load(fileHeart)

fileCirr = open("cirrhosis.pkl", 'rb')
modelC = pickle.load(fileCirr)

filehepa = open("hepatitis.pkl", 'rb')
modelH = pickle.load(filehepa)

app = Flask(__name__)
app.config['SECRET_KEY'] = "Yashnegi@01"

@app.route("/", methods=["GET", "POST"])
def home():        
       
    return render_template("Home.html")

@app.route("/learn", methods=["GET", "POST"])
def learnmore():
    return render_template("learn.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route("/predictS", methods=["Get", "POST"])
def predstoke():
    if(request.method=="POST"):

        age = request.form.get("q17_patientsAge")
        gender = request.form.get("q14_whatIs14")
        ecoder__x0_Female, ecoder__x0_Male, ecoder__x0_Other= 0, 0, 0
        if(gender == "Female"):
                    ecoder__x0_Female, ecoder__x0_Male= 1, 0
        else:
            ecoder__x0_Female, ecoder__x0_Maler= 0, 1
        
        hypertension = request.form.get("q20_doesThe")
        if(hypertension == "Yes"):
                hypertension = 1
        else:
            hypertension = 0    
        hd = request.form.get("q21_doesThe21")
        if(hd == "Yes"):
                hd = 1
        else:
            hd = 0 
        married = request.form.get("q22_everMarried")
        ecoder__x1_No, ecoder__x1_Yes = 0, 0
        if (married == "Yes"):
            ecoder__x1_No, ecoder__x1_Yes = 0, 1
        else:
            ecoder__x1_No, ecoder__x1_Yes = 1, 0
        area = request.form.get("q24_residenceArea")
        ecoder__x3_Rural, ecoder__x3_Urban = 0, 0
        if area == "Urban":
            ecoder__x3_Rural, ecoder__x3_Urban = 0, 1
        else :
            ecoder__x3_Rural, ecoder__x3_Urban = 1, 0
        work = request.form.get("q23_workType")
        ecoder__x2_Govt_job, ecoder__x2_Never_worked, ecoder__x2_Private, ecoder__x2_Self_employed, ecoder__x2_children = 0, 0, 0, 0, 0 
        if work == "Government Job":
            ecoder__x2_Govt_job, ecoder__x2_Never_worked, ecoder__x2_Private, ecoder__x2_Self_employed, ecoder__x2_children = 1, 0, 0, 0, 0
        elif work == "Never worked":
            ecoder__x2_Govt_job, ecoder__x2_Never_worked, ecoder__x2_Private, ecoder__x2_Self_employed, ecoder__x2_children = 0, 1, 0, 0, 0
        elif work == "Private":
            ecoder__x2_Govt_job, ecoder__x2_Never_worked, ecoder__x2_Private, ecoder__x2_Self_employed, ecoder__x2_children = 0, 0, 1, 0, 0
        elif work == "Self-employed":
            ecoder__x2_Govt_job, ecoder__x2_Never_worked, ecoder__x2_Private, ecoder__x2_Self_employed, ecoder__x2_children = 0, 0, 0, 1, 0
        else :
            ecoder__x2_Govt_job, ecoder__x2_Never_worked, ecoder__x2_Private, ecoder__x2_Self_employed, ecoder__x2_children = 0, 0, 0, 0, 1
        
        smoke = request.form.get("q27_smokingStatus")
        ecoder__x4_Unknown, ecoder__x4_formerly_smoked, ecoder__x4_never_smoked, ecoder__x4_smokes = 0, 0, 0, 0
        if smoke == "Formely Smoked":
                ecoder__x4_Unknown, ecoder__x4_formerly_smoked, ecoder__x4_never_smoked, ecoder__x4_smokes = 0, 1, 0, 0
        elif smoke == "Smokes":
            ecoder__x4_Unknown, ecoder__x4_formerly_smoked, ecoder__x4_never_smoked, ecoder__x4_smokes = 0, 0, 0, 1
        elif smoke == "Unknown":
            ecoder__x4_Unknown, ecoder__x4_formerly_smoked, ecoder__x4_never_smoked, ecoder__x4_smokes = 1, 0, 0, 0
        else:
            ecoder__x4_Unknown, ecoder__x4_formerly_smoked, ecoder__x4_never_smoked, ecoder__x4_smokes = 0, 0, 1, 0
        glucose = request.form.get("q25_averageGlucose")
        bmi = request.form.get("q26_bodyMass")
        
        
        predStrokerec = modelS.predict([[ecoder__x0_Female, ecoder__x0_Male, ecoder__x1_No, ecoder__x1_Yes, ecoder__x2_Govt_job, ecoder__x2_Never_worked, ecoder__x2_Private, ecoder__x2_Self_employed, ecoder__x2_children, ecoder__x3_Rural, ecoder__x3_Urban, ecoder__x4_Unknown, ecoder__x4_formerly_smoked, ecoder__x4_never_smoked, ecoder__x4_smokes, age, hypertension, hd, glucose, bmi]])
        
        
        return predStrokerec
        
        # return redirect("/ResultS")
    return render_template("predictS.html", methods=["GET", "POST"])
@app.route("/predictD", methods=["Get", "POST"])
def predheart():
    
    if(request.method=="POST"):
        age = request.form.get("q17_patientsAge")
        
        gender = request.form.get("q14_whatIs14")
        encoder__x0_F,  encoder__x0_M = 0, 0
        if gender =="Male":
            encoder__x0_F,  encoder__x0_M = 0, 1
        else:
            encoder__x0_F,  encoder__x0_M = 1, 0
        pain = request.form.get("q20_typeOf")
        encoder__x1_ASY, encoder__x1_ATA, encoder__x1_NAP, encoder__x1_TA = 0, 0, 0, 0
        if pain == "Asymptomatic":
            encoder__x1_ASY, encoder__x1_ATA, encoder__x1_NAP, encoder__x1_TA = 1, 0, 0, 0
        elif pain == "Atypical Angina":
            encoder__x1_ASY, encoder__x1_ATA, encoder__x1_NAP, encoder__x1_TA = 0, 1, 0, 0
        elif pain == "Non-Anginal":
            encoder__x1_ASY, encoder__x1_ATA, encoder__x1_NAP, encoder__x1_TA = 0, 0, 1, 0
        else :
            encoder__x1_ASY, encoder__x1_ATA, encoder__x1_NAP, encoder__x1_TA = 0, 0, 0, 1
        eia = request.form.get("q21_doesThe21")
        encoder__x3_N, encoder__x3_Y = 0, 0
        if eia =="Yes":
            encoder__x3_N, encoder__x3_Y = 0, 1
        else :
            encoder__x3_N, encoder__x3_Y = 1, 0
        
        slope = request.form.get("q22_slopeOf")
        encoder__x4_Down, encoder__x4_Flat, encoder__x4_Up = 0, 0, 0
        if slope == "Upsloping":
            encoder__x4_Down, encoder__x4_Flat, encoder__x4_Up = 0, 0, 1
        elif slope == "Flat":
            encoder__x4_Down, encoder__x4_Flat, encoder__x4_Up = 0, 1, 0
        else:
            encoder__x4_Down, encoder__x4_Flat, encoder__x4_Up = 1, 0, 0
        
        rer = request.form.get("q31_restingElectrocardiogram")
        encoder__x2_LVH, encoder__x2_Normal, encoder__x2_ST = 0, 0, 0
        if rer == "Having ST-T wave abnorminality":
            encoder__x2_LVH, encoder__x2_Normal, encoder__x2_ST = 0, 0, 1
        elif rer == "Left Ventricular Hypertrophy":
            encoder__x2_LVH, encoder__x2_Normal, encoder__x2_ST = 0, 1, 0
        else:
            encoder__x2_LVH, encoder__x2_Normal, encoder__x2_ST = 1, 0, 0
        
        restingBP = request.form.get("q25_restingBp")
        cholestrol = request.form.get("q26_cholesterol")
        FastingBloodSugar = request.form.get("q28_fastingBlood")
        maxheartrate = request.form.get("q32_maximumHeart")
        oldppeak = request.form.get("q33_oldpeak")
        pdisease = modelD.predict([[encoder__x0_F,  encoder__x0_M, encoder__x1_ASY, encoder__x1_ATA, encoder__x1_NAP, encoder__x1_TA,
        encoder__x2_LVH, encoder__x2_Normal, encoder__x2_ST, encoder__x3_N, encoder__x3_Y, encoder__x4_Down,
        encoder__x4_Flat, encoder__x4_Up, age ,restingBP, cholestrol, FastingBloodSugar,maxheartrate, oldppeak]])
        
        return str(pdisease[0])
    return render_template("predictD.html")

@app.route("/predictH", methods=["GET", "POST"])
def predhepatitis():
    if request.method=="POST":
        age = request.form.get("q17_patientsAge")
        gender = request.form.get("q14_whatIs14")
        encoder__x0_f, encoder__x0_m = 0,0
        if gender == "Male":
            encoder__x0_f, encoder__x0_m = 0, 1
        else:
            encoder__x0_f, encoder__x0_m = 1, 0
        ALB = request.form.get("q25_albuminAnd")
        ALP = request.form.get("q26_alkalinePhosphatase")
        ALT = request.form.get("q28_alanineTransaminase")
        AST = request.form.get("q32_aspartateAminotransferase")
        BIL  = request.form.get("q33_bilateral")
        CHE = request.form.get("q35_number35")
        CHOL = request.form.get("q34_chol")
        CREA = request.form.get("q36_creatinine")
        GGT = request.form.get("q37_gammaglutamylTransferase")
        PROT = request.form.get("q38_prot")
        predHH = modelH.predict([[encoder__x0_f, encoder__x0_m, age, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT]])     
        
        return str(predHH[0])
        
    return render_template("predictH.html")

@app.route("/predictC", methods=["GET", "POST"])
def predhcirrhosis():
    # ['encoder__x0_D-penicillamine', 'encoder__x0_Placebo', 'encoder__x1_F', 'encoder__x1_M', 'encoder__x2_N', 'encoder__x2_Y', 'encoder__x3_N', 'encoder__x3_Y', 
    # 'encoder__x4_N', 'encoder__x4_Y', 'encoder__x5_N', 'encoder__x5_S', 'encoder__x5_Y', 'x0', 'x2', 'x8', 'x9', 'x10', 'x11', 'x12', 'x13', 'x14', 'x15', 'x16', 'x17']
    if request.method=="POST":
        age = request.form.get("q17_patientsAge")
        gender = request.form.get("q14_whatIs14")
        ascites = request.form.get("q45_presenceOf45")
        encoder__x2_N, encoder__x2_Y = 0, 0
        if ascites == "Yes":
            encoder__x2_N, encoder__x2_Y = 0, 1
        else:
            encoder__x2_N, encoder__x2_Y = 1, 0
        encoder__x1_F, encoder__x1_M =0, 0
        if gender == "Male":
            encoder__x1_F, encoder__x1_M =0, 1
        else:
            encoder__x1_F, encoder__x1_M =1, 0 
        
        ndays = request.form.get("q39_numberOf")
        status = request.form.get("q44_statusOf")
        
        if status == "Censored":
            status = 1
        elif status == "Death":
            status = 0
        else: 
            status = 2
        drug = request.form.get("q40_typeOf")
        encoder__x0_D_penicillamine, encoder__x0_Placebo = 0, 0
        if drug == "D-penicillamine":
            encoder__x0_D_penicillamine, encoder__x0_Placebo = 1, 0
        else:
            encoder__x0_D_penicillamine, encoder__x0_Placebo = 0, 1
        hepta = request.form.get("q41_presenceOf")
        encoder__x3_N, encoder__x3_Y = 0, 0
        if hepta == "Yes":
            encoder__x3_N, encoder__x3_Y = 0, 1
        else:
            encoder__x3_N, encoder__x3_Y = 1, 0
        
        spiders = request.form.get("q42_presenceOf42")
        encoder__x4_N, encoder__x4_Y = 0, 0
        if spiders == "Yes":
            encoder__x4_N, encoder__x4_Y = 0, 1
        else:
            encoder__x4_N, encoder__x4_Y = 1, 0
        
        edema = request.form.get("q43_presenceOf43")
        encoder__x5_N, encoder__x5_S, encoder__x5_Y = 0, 0, 0
        if edema == "No edema and no diuretic therapy for edema":
           encoder__x5_N, encoder__x5_S, encoder__x5_Y = 1, 0, 0 
        elif edema == "Edema present without diuretics, or edema resolved by diuretics":
            encoder__x5_N, encoder__x5_S, encoder__x5_Y = 0, 1, 0
        else:
            encoder__x5_N, encoder__x5_S, encoder__x5_Y = 0, 0, 1
            
        bilirubin = request.form.get("q25_serumBilirubin")
        cholestrol = request.form.get("q26_serumCholesterol")
        albuminum = request.form.get("q28_albuminIn")
        copper = request.form.get("q32_urineCopper")
        akp = request.form.get("q33_alkalinePhosphatase")
        sgot = request.form.get("q36_sgotIn")
        trig = request.form.get("q37_trigliceridesIn")
        platelets = request.form.get("q34_plateletsPer")
        proth = request.form.get("q35_number35")
        predCC = modelC.predict([[encoder__x0_D_penicillamine, encoder__x0_Placebo,encoder__x1_F, encoder__x1_M, encoder__x2_N, encoder__x2_Y, encoder__x3_N, encoder__x3_Y, 
        encoder__x4_N, encoder__x4_Y, encoder__x5_N, encoder__x5_S, encoder__x5_Y, ndays, age, bilirubin, cholestrol, albuminum, copper, akp, sgot, trig, platelets, proth, status]])
        return predCC[0]
    return render_template("predictC.html")
@app.route("/ResultS", methods=["GET", "POST"])
def finalS():
    statement = ""
    if predstoke() == 1:
        statement = "You are likely to suffer from a Stroke!"
    else:
        statement = "Dont worry, we could not find anything wrong with you."
    return render_template("ResultS.html", a = statement)
@app.route("/ResultD", methods=["GET", "POST"])
def finalD():
    statement = ""
    if predheart() == "1":
        statement = "You are likely to be suffering from a heart disease!"
    else:
        statement = "Dont worry, we could not find anything wrong with you."
    return render_template("ResultD.html", a = statement)
@app.route("/ResultC", methods=["GET", "POST"])
def finalC():
    statement = ""
    if predhcirrhosis() == 1:
        statement = "You are likely to be in stage 1, also called Steatosis!"
    elif predhcirrhosis() == 2:
        statement = "You are likely to be in stage 2, also called Fibrosis!"
    elif predhcirrhosis() == 3:
        statement = "You are likely to be suffering from Cirrhosis!"
    else:
        statement = "You might be suffering from Hepatitis."
    return render_template("ResultC.html", a = statement)
@app.route("/ResultH", methods=["GET", "POST"])
def finalH():
    statement = ""
    if predhepatitis() == "0":
        statement = "We are assuming that you are a blood donor."
        
    else:
        statement = "You are likely to be suffering from a Hepatitis!"
    return render_template("ResultH.html", a = statement)
    
if __name__ == "__main__":
    app.run(debug=True)