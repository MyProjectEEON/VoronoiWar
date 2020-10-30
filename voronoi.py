from tkinter import *
import random
from math import*
import rn2
import time
import randomname as rn
import latin

root=Tk()
root.title("Voronoi")
C=Canvas(root,bg="#ffffff",width=1400,height=int(1000*22.5),xscrollincrement=1,yscrollincrement=1,scrollregion=(0,0,500,int(1000*22.5)))
root.geometry("1400x750")
vbar=Scrollbar(root,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=C.yview)
C.config(yscrollcommand=vbar.set)
C.pack()

gradient=["#FF0000",
          "#FF1000",
          "#FF2000",
          "#FF3000",
          "#FF4000",
          "#FF5000",
          "#FF6000",
          "#FF7000",
          "#FF8000",
          "#FF9000",
          "#FFA000",
          "#FFB000",
          "#FFC000",
          "#FFD000",
          "#FFE000",
          "#FFF000",
          "#FFFF00",
          "#F0FF00",
          "#E0FF00",
          "#D0FF00",
          "#C0FF00",
          "#B0FF00",
          "#A0FF00",
          "#90FF00",
          "#80FF00",
          "#70FF00",
          "#60FF00",
          "#50FF00",
          "#40FF00",
          "#30FF00",
          "#20FF00",
          "#10FF00"]

def random_color_1():
    return(random.choice(['#ff0000','#ff8000','#ffff00','#80ff00','#00aa00',
                          '#00ffff','#0000ff','#8000ff','#ff00ff','#808080']))

def random_color():
    r=lambda:random.randint(0,255)
    return("#%02x%02x%02x"%(r(),r(),r()))

def midcirc(oval):
    s=abs(C.coords(oval)[2]-C.coords(oval)[0])
    return C.create_oval(C.coords(oval)[0]+s/2-7,C.coords(oval)[1]+s/2-7,C.coords(oval)[2]-s/2+7,C.coords(oval)[3]-s/2+7)

def city(x,y,scl):
    l=[]
    for i in range(10):
        rx=random.randint(x-scl,x+scl)
        ry=random.randint(y-scl,y+scl)
        rr=random.randint(1,4)
        l.append(C.create_rectangle(rx+rr,ry+rr,rx-rr,ry-rr,fill="#ffaa88",outline=rn2.darken_color("#ffaa88")))

def n2c(f,h):
    return[f%h,f//h]

def distance(a,b):
    return sqrt(((C.coords(Dk2i[a])[0]+2*scale/6)-(C.coords(Dk2i[b])[0]+2*scale/6))**2+((C.coords(Dk2i[a])[1]+2*scale/6)-(C.coords(Dk2i[b])[1]+2*scale/6))**2)

def battle(m1,m2,flag1,flag2,line):
    C3.create_text(40,line*22+10,text=str(m1))
    rn2.print_flag(C3.create_oval(76,line*22+3,90,line*22+17),flag1,C3)
    C3.create_text(100,line*22+10,text="VS")
    rn2.print_flag(C3.create_oval(110,line*22+3,124,line*22+17),flag2,C3)
    C3.create_text(160,line*22+10,text=str(m2))
    C3.update()
    return line+1

def scroll(event):
    C3.yview_scroll(int(-1*(event.delta/10)),"units")
    C3.update()

def troop_density():
    C.delete("dense")
    for i in Do2c["#ffffff"]:
        if int(len(gradient)/(population*1.5/(Dc2u[i][0]+0.00000001)))<len(gradient):
            C.create_rectangle(C.coords(Dk2i[i])[0]-2*scale/3,C.coords(Dk2i[i])[1]-2*scale/3,C.coords(Dk2i[i])[2]+2*scale/3,C.coords(Dk2i[i])[3]+2*scale/3,
                               fill=gradient[(len(gradient)-int(len(gradient)/(population*1.5/(Dc2u[i][0]+0.00000001))))-1],tag="dense",outline="")
        else:
            C.create_rectangle(C.coords(Dk2i[i])[0]-2*scale/3,C.coords(Dk2i[i])[1]-2*scale/3,C.coords(Dk2i[i])[2]+2*scale/3,C.coords(Dk2i[i])[3]+2*scale/3,
                               fill=gradient[0],tag="dense",outline="")

def troop_density2():
    C.delete("dense")
    for j in Do2c:
        for i in Do2c[j]:
            try:
                C.create_rectangle(C.coords(Dk2i[i])[0]-2*scale/3,C.coords(Dk2i[i])[1]-2*scale/3,C.coords(Dk2i[i])[2]+2*scale/3,C.coords(Dk2i[i])[3]+2*scale/3,
                                   fill=gradient[len(gradient)-int(len(gradient)/(population*1.5/Dc2u[i][0]))],tag="dense",outline="")
            except:
                """C.create_rectangle(C.coords(Dk2i[i])[0]-2*scale/3,C.coords(Dk2i[i])[1]-2*scale/3,C.coords(Dk2i[i])[2]+2*scale/3,C.coords(Dk2i[i])[3]+2*scale/3,
                                   fill=gradient[-1],tag="dense",outline="")"""

def run():
    global Chronik,Summary,C3,Lbat
    Lbat=[]
    s2c=random.choice(list(Dc2o.keys()))
    s2o=Dc2o[s2c]
    sbattles=0
    skills=0
    salive=1
    #sname=rn.random_name()+" "+latin.latin()
    line=0
    story=Tk()
    story.title("the greatest battles")
    story.geometry("400x400")
    C3=Canvas(story,yscrollincrement=1,height=40000,bg="#ffffff",scrollregion=(0,0,500,40000))
    C3.pack(side="left")
    vbar2=Scrollbar(story,orient=VERTICAL)
    vbar2.pack(side="right",fill=Y)
    vbar2.config(command=C3.yview)
    C3.config(yscrollcommand=vbar2.set)
    story.bind("<MouseWheel>",scroll)
    game=1
    while game:
        time.sleep(0)
        for i in Do2c:
            if i=="#fffff":
                if Do2c[i]:
                    ln=[]
                    gomain=0
                    for j in Do2c[i]:
                        if j in Dnei:
                            for k in Dnei[j]:
                                if Dc2u[j][0]>Dc2u[k][0]:
                                    if Dmain[Dk2i[k]]:
                                        line=move(j,k,Dc2u[j][0],line)
                                        if Dmain[Dk2i[j]]:
                                            goto=[j,1]
                                        gomain=1
                                    else:
                                        ln.append([j,k])
                    move_l=0
                    if not gomain:
                        for j in ln.copy():
                            li=[]
                            for k in range(0,int(len(list(Dc2o.keys()))/4),4):
                                if Dc2o[list(Dc2o.keys())[k]]!=Dc2o[j[0]]:
                                    li.append(distance(list(Dc2o.keys())[k],j[0]))
                            if Dmain[Dk2i[j[0]]]and min(li)<scale*4:
                                if Dc2u[j[0]][0]<=population*2:
                                    ln.remove(j)
                                else:
                                    move_l=Dc2u[j[0]][0]-population*2
                        if ln:
                            r=random.choice(ln)
                            if Dmain[Dk2i[r[0]]]and move_l:
                                amount=move_l
                            else:
                                amount=int((Dc2u[r[0]][0]-Dc2u[r[1]][0])/2)
                            line=move(r[0],r[1],amount,line)
                            if Dmain[Dk2i[r[0]]]:
                                goto=[r[0],2]
                        else:
                            s=random.choice(Do2c[i])
                            t=0
                            while(Dc2u[s][0]<=0 or Dmain[Dk2i[s]])and t<100:
                                t+=1
                                s=random.choice(Do2c[i])
                            d=random.choice(Dnei[s])
                            try:
                                line=move(s,d,random.randint(0,Dc2u[s][0]),line)
                                goto=[s,3]
                            except:
                                pass
##                            t=0
##                            test=1
##                            while test and t<100:
##                                t+=1
##                                d=random.choice(Dnei[s])
##                                if distance(s,get_front(s))<distance(d,get_front(d))and Dc2o[d][0]!=Dc2o[s][0]:
##                                    test=0
##                            try:
##                                line=move(s,d,Dc2u[s][0],line)
##                            except:
##                                pass
                    try:
                        if Dmain[Dk2i[goto[0]]]:
                            print("ALERT",goto[1])
                    except:
                        pass
            else:
                if Do2c[i]:
                    s=random.choice(Do2c[i])
                    t=0
                    while Dc2u[s][0]<=0 and t<100:
                        t+=1
                        s=random.choice(Do2c[i])
                    try:
                        line=move(s,random.choice(Dnei[s]),random.randint(0,Dc2u[s][0]-0),line)
                    except:
                        pass
        for i in Dc2u:
            Dc2u[i][0]+=0
        #troop_density()
        handle_counter()
        C.tag_raise("arrow")
        C.update()

def get_front2(s):
    li=[]
    l2=[]
    for k in range(0,int(len(list(Dc2o.keys()))/4),4):
        if Dc2o[list(Dc2o.keys())[k]]!=Dc2o[s]:
            li.append(distance(list(Dc2o.keys())[k],s))
            l2.append(list(Dc2o.keys())[k])
    return(l2[li.index(min(li))])

def get_front(s):
    li=[]
    l2=[]
    for k in Dc2o:
        if Dc2o[k]!=Dc2o[s]:
            li.append(distance(k,s))
            l2.append(k)
    try:
        C.create_line(C.coords(Dk2i[s])[0],C.coords(Dk2i[s])[1],C.coords(Dk2i[l2[li.index(min(li))]])[0],C.coords(Dk2i[l2[li.index(min(li))]])[1],width=6,fill="black",arrow=LAST,tag="arrow")
    except Exception as a:
        print(a)
    return(l2[li.index(min(li))])

def move(s,d,a,line):
    ex=Dc2o[d][0]
    ex_men=Dc2u[d][0]
    Dc2u[s][0]-=a
    if Dc2o[s][0]==Dc2o[d][0]:
        Dc2u[d][0]+=a
    else:
        if Dc2u[d][0]>=a:
            Dc2u[d][0]-=a
        else:
            Dc2u[d][0]=a-Dc2u[d][0]
            Dc2o[d][0]=Dc2o[s][0]
            Do2c[Dc2o[s][0]].append(d)
            Do2c[ex].remove(d)
            for j in C.find_overlapping(*C.coords(Dk2i[d])):
                if j!=Dk2i[d]:
                    if not(j in C.find_withtag("street")or j in C.find_withtag("capital")or j in C.find_withtag("square")):
                        C.delete(j)
            try:
                rn2.print_flag(midcirc(Dk2i[d]),Dc2f[Dc2o[s][0]],C)
            except:
                pass
            if Dmain[Dk2i[d]]:
                line=battle(a,ex_men,Dc2f[Dc2o[s][0]],Dc2f[ex],line)
                C.itemconfig("B"+str(Dc2p[d]),fill=Dc2o[s][0])
                for i in Dp2c[Dc2p[d]]:
                    Dc2o[i][0]=Dc2o[s][0]
                    for j in Do2c:
                        if i in Do2c[j]:
                            Do2c[j].remove(i)
                    Do2c[Dc2o[s][0]].append(i)
                    try:
                        rn2.print_flag(midcirc(Dk2i[i]),Dc2f[Dc2o[s][0]],C)
                    except:
                        pass
    return line
            

def voronoi(pro,width,height,scl):
    global lx,ly,ld,lc,lx2,ly2,ld2,lx3,ly3,l,Dmain,Lct,Lsq,Dnei,Do2c,Dc2f,Dc2u,Dp2c,Dc2o,Dc2p,Di2k,Dk2i,C2,population
    check=1
    while check:
        population=100000
        lx,ly,ld,lc=[],[],{},[]
        lx2,ly2,ld2=[],[],{}
        lx3,ly3=[],[]
        Lsq=[]
        #color2flag
        Dc2f={}
        #city2units on it, returns list oredered same like Dc2o
        Dc2u={}
        #city2province
        Dc2p={}
        #province2city
        Dp2c={}
        #city2occupation, returns list of occupants ordered same like Dc2u (occupant as color)
        Dc2o={}
        #occupant2city, returns list of cities occupied by him (occupant as color)
        Do2c={}
        #id to map key
        Di2k={}
        #map key to id
        Dk2i={}
        #city2connected cities, returns list of cities connected with it
        Dnei={}
        for i in range(int(width/scl)*int(height/scl)+int(height/scl)):
            Lsq.append(0)
        Lct,Dmain,Dflag=[],{},{}
        for i in range(pro):
            Lct.append([])
            lx.append(random.randint(0,width-0))
            ly.append(random.randint(0,height-0))
            sf=rn2.save_flag()
            c=sf[1]
            Dflag[i]=sf[0]
            while c in lc:
                sf=rn2.save_flag_1(random_color())
                c=sf[1]
                Dflag[i]=sf[0]
            lc.append(c)
            Dc2f[c]=Dflag[i]
        for i in range(pro):
            for j in range(4):
                lx2.append(random.randint(0,width-0))
                ly2.append(random.randint(0,height-0))
        for i in range(len(lx2)):
            l=[]
            for k in range(pro):
                l.append(sqrt((lx2[i]-lx[k])**2+(ly2[i]-ly[k])**2))
            ld2[i]=l.index(min(l))
        for i in range(len(lx2)):
            C.create_oval(lx2[i]-2,ly2[i]-2,lx2[i]+2,ly2[i]+2,fill=lc[ld2[i]],outline=lc[ld2[i]])
            
        for x in range(int(width/scl)):
            for y in range(int(height/scl)):
                l=[]
                for i in range(len(lx2)):
                    l.append(sqrt((lx2[i]-x*scl)**2+(ly2[i]-y*scl)**2))
                cc="#cccccc"
                if((x*scl+scl/2)-width/2)**2/(width/2)**2+((y*scl+scl/2)-height/2)**2/(height/2)**2<=1:
                    cc=lc[ld2[l.index(min(l))]]
                    if not x%2 and y%2 and random.randint(0,3):
                        if(((x-1)*scl+scl/2)-width/2)**2/(width/2)**2+((y*scl+scl/2)-height/2)**2/(height/2)**2<=1 and(((x+1)*scl+scl/2)-width/2)**2/(width/2)**2+((y*scl+scl/2)-height/2)**2/(height/2)**2<=1:
                            C.create_rectangle(x*scl-scl/2,y*scl+scl/3,x*scl+scl*1.5,y*scl+scl/3*2,fill="#ffffff",width=2,tag="street")
                            if(x-1):
                                try:
                                    Dnei[(x-1)*int(height/scl)+y].append((x+1)*int(height/scl)+y)
                                except:
                                    Dnei[(x-1)*int(height/scl)+y]=[(x+1)*int(height/scl)+y]
                            if(x+1)in range(int(width/scl)):
                                try:
                                    Dnei[(x+1)*int(height/scl)+y].append((x-1)*int(height/scl)+y)
                                except:
                                    Dnei[(x+1)*int(height/scl)+y]=[(x-1)*int(height/scl)+y]
                    elif x%2 and not y%2 and random.randint(0,3):
                        if((x*scl+scl/2)-width/2)**2/(width/2)**2+(((y-1)*scl+scl/2)-height/2)**2/(height/2)**2<=1 and((x*scl+scl/2)-width/2)**2/(width/2)**2+(((y+1)*scl+scl/2)-height/2)**2/(height/2)**2<=1:
                            C.create_rectangle(x*scl+scl/3,y*scl-scl/2,x*scl+scl/3*2,y*scl+scl*1.5,fill="#ffffff",width=2,tag="street")
                            if(y-1):
                                try:
                                    Dnei[x*int(height/scl)+(y-1)].append(x*int(height/scl)+(y+1))
                                except:
                                    Dnei[x*int(height/scl)+(y-1)]=[(x*int(height/scl)+(y+1))]
                            if(y+1)in range(int(height/scl)):
                                try:
                                    Dnei[x*int(height/scl)+(y+1)].append(x*int(height/scl)+(y-1))
                                except:
                                    Dnei[x*int(height/scl)+(y+1)]=[(x*int(height/scl)+(y-1))]
                    elif x%2 and y%2:
                        Lct[ld2[l.index(min(l))]].append(C.create_oval(x*scl+scl/6,y*scl+scl/6,x*scl+scl/6*5,y*scl+scl/6*5,fill="#ffffff",outline="#000000",width=2,tag="city"))
                        ID=x*int(height/scl)+y
                        Dmain[Lct[ld2[l.index(min(l))]][-1]]=0
                        Dk2i[ID]=Lct[ld2[l.index(min(l))]][-1]
                        Di2k[Lct[ld2[l.index(min(l))]][-1]]=ID
                        rn2.print_flag(midcirc(Lct[ld2[l.index(min(l))]][-1]),Dflag[ld2[l.index(min(l))]],C)
                        Dc2u[ID]=[population]
                        Dc2p[ID]=ld2[l.index(min(l))]
                        try:
                            Dp2c[ld2[l.index(min(l))]].append(ID)
                        except:
                            Dp2c[ld2[l.index(min(l))]]=[ID]
                        Dc2o[ID]=[cc]
                        try:
                            Do2c[cc].append(ID)
                        except:
                            Do2c[cc]=[ID]
                try:
                    Lsq[x*int(height/scl)+y]=C.create_rectangle(x*scl,y*scl,x*scl+scl,y*scl+scl,fill=cc,outline="",tag=("B"+str(lc.index(cc)),"square"))
                except:
                    Lsq[x*int(height/scl)+y]=C.create_rectangle(x*scl,y*scl,x*scl+scl,y*scl+scl,fill=cc,outline="",tag="square")
                try:
                    if color!=cc:
                        C.create_line(x*scl,y*scl,x*scl+scl,y*scl,width=2)
                except:
                    pass
                try:
                    if C.itemcget(Lsq[(x-1)*int(height/scl)+y],"fill")!=cc and C.itemcget(Lsq[(x-1)*int(height/scl)+y],"fill"):
                        C.create_line(x*scl,y*scl,x*scl,y*scl+scl,width=2)
                except:
                    pass
                color=cc
        for i in Lct:
            if i:
                o=random.choice(i)
                s=28
                Dmain[o]=C.create_oval(C.coords(o)[0]-s/4,C.coords(o)[1]-s/4,C.coords(o)[2]+s/4,C.coords(o)[3]+s/4,fill="#ffffff",width=2,tag="capital")
        C.tag_raise("street")
        C.tag_raise("capital")
        C.tag_raise("city")
        C.tag_raise("flag")
        """for i in Dc2o:
            if not i in Dnei:
                C.create_rectangle(n2c(i,width)[0]-15,n2c(i,width)[1]-15,n2c(i,width)[0]+15,n2c(i,width)[1]+15,fill="red")
                Dnei[i]=i+2
                try:
                    Dnei[i+2].append(i)
                except:
                    Dnei[i+2]=[i]"""
        check=0
    root2=Tk()
    C2=Canvas(root2,width=200,height=22*len(list(Dp2c.keys()))+40)
    C2.pack()
    C2.create_oval(2,0+2,16,0+16)
    u=0
    for i in Dc2u:
        u+=Dc2u[i][0]
    C2.create_text(40,9,text=str(u),tag="total")
    p=0
    for i in Do2c:
        ov=C2.create_oval(2,p*22+2+22,16,p*22+16+22,tag="F"+str(p))
        rn2.print_flag(ov,Dc2f[i],C2)
        u=0
        for j in Do2c[i]:
            u+=Dc2u[j][0]
        C2.create_text(40,p*22+9+22,text=str(u),tag="T"+str(p))
        p+=1
    run()

def handle_counter():
    u=0
    for i in Dc2u:
        u+=Dc2u[i][0]
    C2.itemconfig("total",text=str(u))
    li=[]
    di={}
    for i in Do2c:
        di[len(li)]=i
        u=0
        for j in Do2c[i]:
            u+=Dc2u[j][0]
        u+=0.00001*len(li)
        li.append(u)
    li2=li.copy()
    li2.sort(reverse=True)
    p=0
    for i in Do2c:
        for j in C2.find_overlapping(*C2.coords("F"+str(p))):
            if not j in C2.find_withtag("F"+str(p)):
                C2.delete(j)
        rn2.print_flag(C2.find_withtag("F"+str(p))[0],Dc2f[di[li.index(li2[p])]],C2)
        C2.itemconfig("T"+str(p),text=str(int(li2[p])))
        p+=1
    C2.update()
    
scale=20
voronoi(35,1400,750,scale)
            
