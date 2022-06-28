from django.shortcuts import render
import pickle
import numpy
import sklearn

model=pickle.load(open('model.pkl','rb+'))
scale = pickle.load(open("scaler.pkl",'rb+'))
 
def home(request):
    return render(request, 'form.html')
 
def new_page(request):
    cs = request.GET["CreditScore"]
    fthb = request.GET["FTHB"]
    MSA = request.GET["MSA"]
    MIP = request.GET["MIP"]
    Units = request.GET["Units"]
    Occupancy = request.GET["Occupancy"]
    DTI = request.GET["DTI"]
    OrigUPB = request.GET["OrigUPB"]
    LTV = request.GET["LTV"]
    OrigInterestRate = request.GET["OrigInterestRate"]
    Channel = request.GET["Channel"]
    PropertyType = request.GET["PropertyType"]
    LoanPurpose = request.GET["LoanPurpose"]
    OrigLoanTerm =request.GET["OrigLoanTerm"]
    NumBorrowers = request.GET["NumBorrowers"]
    EverDelinquent = request.GET["EverDelinquent"]
    MonthsInRepayment = request.GET["MonthsInRepayment"]

    final_features = [cs, fthb, MSA, MIP, Units, Occupancy, DTI, OrigUPB, LTV, OrigInterestRate, Channel, PropertyType, LoanPurpose, OrigLoanTerm, NumBorrowers, EverDelinquent, MonthsInRepayment ]
    array = numpy.array(final_features)
    scaled_feature = scale.transform(array.reshape(1, -1))
    y_pred = model.predict(scaled_feature)

    if y_pred == 1:
        data = 'High chance of prepayment'
    else:
        data ='Low chance of prepayment'

    return render(request, 'newpage.html', {'data':data})