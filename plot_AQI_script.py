import pandas as pd
import matplotlib.pyplot as plt

def avg_data(year):
    temp_i=0
    average=[]
    for rows in pd.read_csv(f"/home/vignesh/mlprojects/Data/AQI/aqi{year}.csv",chunksize=24):
        add_var=0
        data=[]
        
        for index,row in pd.DataFrame(data=rows).iterrows():
            value=row["PM2.5"]
            
            if isinstance(value, (float,int)):
                add_var+=value
            
            elif isinstance(value,str):
                if value not in ["NoData","PwrFail","---","InVld"]:
                    add_var+=float(value)
    
        avg=add_var/24
        temp_i+=1
        average.append(avg)
    return average

if __name__ == "__main__":
    years = range(2013, 2019)
    for year in years:
        lst = avg_data(year)
        plt.plot(range(len(lst)), lst, label=f"{year} data")

    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()