b=True
while b:
    s=input("Enter the question you want to test:")
    i=-1
    if s.find("who")==0 or s.find("Who")==0:
        i=0
    elif s.find("what")==0 or s.find("What")==0:
        i=1
    elif s.find("when")==0 or s.find("When")==0:
        i=2
    elif s[0:2]=="is" or s[0:2]=="Is":
        i=3
    else:
        i=4
    import pandas as pd
    df=pd.DataFrame([i])
    import pickle as p
    model=p.load(open("final_quest.pickle",'rb'))
    import numpy as np
    st=np.array2string(model.predict(df))
    print(st.split("'")[1].strip())
    s1=input("enter exit() to exit:")
    if s1=="exit()":
        b=False
        
    
