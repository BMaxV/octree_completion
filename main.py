import random
import pandas as pd

class cell:
    def __init__(self,pos,size):
        self.contents= {}
        self.pos=pos
        l=[0.5,1,1]
        self.status_a=random.choice(l)

def main():
    
    big_cells={}
    write_to_dict(big_cells)
    
    for key in big_cells:
        cell_object=big_cells[key]
        write_to_dict(cell_object.contents,size="small")
    output_small={}
    y_labels=[]
    all_row_keys=[]
    for key in big_cells:
        print(key)
        for key_small in big_cells[key].contents:
            print("   ",key_small)
            x1=big_cells[key].pos[0]
            x2=big_cells[key].contents[key_small].pos[0]
            y1=big_cells[key].pos[1]
            y2=big_cells[key].contents[key_small].pos[1]
            
            column_key=str(y1)+str(y2)
            if column_key not in y_labels:
                y_labels.append(column_key)
                
            row_key=str(x1)+str(x2)
            if row_key not in output_small:
                output_small[row_key]=[]
            if row_key not in all_row_keys:
                all_row_keys.append(row_key)
            
            output_small[row_key].append(big_cells[key].contents[key_small])
    
    #sum up
    for key in big_cells:
        ob=big_cells[key]
        big_status=0
        #print(key)
        statuses=[]
        for small_key in ob.contents:
            big_status+=ob.contents[small_key].status_a
            statuses.append(ob.contents[small_key].status_a)
        statuses.sort()
        #for el in statuses:
        #    print("  ",el)
        
        big_status=big_status/len(ob.contents)
        #print(big_status)
        #input("ok?")
        ob.status_a=big_status
    
    #output_small
    
    all_row_keys.sort()
    
    with open("test.csv","w") as f:
        f.write(";")
        for y_label in y_labels:
            f.write(y_label+";")
        f.write("\n")
        for row_key in all_row_keys:
            f.write(row_key+";")
            for ob in output_small[row_key]:
                f.write(str(ob.status_a)+";")
            f.write("\n")
    
    with open("big_test.csv","w") as f:
        f.write(";1;2;3;\n")
        y=0
        while y < 3:
            f.write(str(y)+";")
            x=0
            while x < 3:
                f.write(str(big_cells[str((x,y))].status_a)+";")
                x+=1
            y+=1
            f.write("\n")
    
    df2=pd.read_csv("big_test.csv",delimiter=";")
    df=pd.read_csv("test.csv",delimiter=";")
    
    with open("test.html","w") as f:
        f.write(df.to_html(index=False))
        f.write(df2.to_html(index=False))
    

def write_to_dict(big_cells,size="big"):
    y=0
    while y < 3:
        x=0
        while x < 3:
            big_cells[str((x,y))]=cell(pos=(x,y),size="big")
            x+=1
        y+=1
    
if __name__=="__main__":
    main()
