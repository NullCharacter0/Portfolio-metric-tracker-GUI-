from tkinter import E, VERTICAL, X, Canvas, Frame, IntVar, Label, LabelFrame, Scrollbar, StringVar, Tk,W
from tkinter.ttk import Treeview
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk # type: ignore
from matplotlib.patches import Circle, Polygon, Wedge
from  Data import Products   # type: ignore
# library
import matplotlib.pyplot as plt

from GUI_Modules import SingleDataFrameViewer, createCanvasFromMatPlt

class GUI(Tk):

    def __init__(self) -> None:
        super().__init__()
        size_of_groups=[1,1,1,1,1]
        labels = ["f" for i in size_of_groups]

        # Products().list_tradable_products()        
        # Figures First
        top_frame = Frame(self)
        top_frame.grid(row=0, column=0 ) # self.top_frame
        pie_frame = Frame(top_frame)
        pie_frame.grid(row=0, column=0,sticky="n" ) # top_frame.pie
        graph_frame = Frame(top_frame)
        graph_frame.grid(row=1, column=0 ) # top_frame.graph
        
        stats_canvas =  Canvas(master=top_frame, bg="blue", )
        stats_canvas.grid(row=0, column=1,sticky="NSEW") 
        stats_frame = Frame(stats_canvas,height=200,)
        stats_frame.grid(row=0, column=0 ,rowspan=3,sticky="NS")
        # stats_scroll_bar = Scrollbar( stats_frame,width=50,orient= VERTICAL, command=stats_canvas.yview,)
        # stats_scroll_bar.grid(row=0,column=0,sticky="NEWS")

        # This is my first indexed figure Starting at 99 descending 
        pieFig = plt.figure(num=99) 
        pieAxis = pieFig.add_subplot(1,1,1)
        
        performanceFigure  = plt.figure(num=98,layout='compressed')
        performanceAxis = performanceFigure.add_subplot(1,1,1)
        
        performanceFigure.set_size_inches(3.4,1.2, forward=True)
        pieFig.set_size_inches(3.4, 3, forward=True)
        
        pieAxis.pie(size_of_groups,radius=1.2,labels=labels,autopct='%1.1f%%',
                pctdistance=1.25,wedgeprops=dict(width=.6), labeldistance=.6)
        pieAxis.text(-.55, -.05, 'Open positions', fontsize=10)



        # stats_frame.pack(side="top")
        

        canvas1, asd = createCanvasFromMatPlt(pieFig,pie_frame, )
        canvas2, asd = createCanvasFromMatPlt(performanceFigure,pie_frame, )
        canvas1.get_tk_widget().pack(side="top")
        canvas2.get_tk_widget().pack(side="top")
        
        
        grid_row_cfg = 0 
        label_grid_row_cfg = 0 
        metric_label_grid_column_cfg = 0 
        metric_value_grid_column_cfg = metric_label_grid_column_cfg + 1 
        
        
        pmv = PortfolioMetricsValues(stats_frame)
        pmv.grid(row=0,column=5)
        # print(pmv.allMetrics)
        ifra_column = 0 
        for k1,v1 in  pmv.allMetrics.items():
            print(k1)
            ifra = LabelFrame(pmv, name=k1,text=k1 + " :",width=300,height=10)
            
            ifra.grid(row=label_grid_row_cfg, column=0 )
            for k2,v2   in v1.items():
                k2 = k2.lower()
                # ifra = LabelFrame(ifra, name=k2,text=k2 + " :",width=300,height=10)
                ifra.grid(row=label_grid_row_cfg, column=0,sticky=W )
                label_grid_row_cfg += 1 
                Label(ifra,name=k2.lower(),text=k2 + " :").grid(row=grid_row_cfg,column=metric_label_grid_column_cfg,sticky=W)
                Label(ifra,name=k2.lower()+'value',text=str(v2.get())).grid(row=grid_row_cfg,column=metric_value_grid_column_cfg,sticky=W)
                grid_row_cfg += 1 
        # self.geometry("500x450")

class PortfolioMetricsValues(LabelFrame):
    

    def __init__(self,master, **kwargs):
        super().__init__(master = master, text = " Portfolio Metrics ")
            
        self.ytd = {
            "Realized": IntVar(  name =  "Realized") , 
            "Dividends":  IntVar(  name =  "Dividends") , 
            "Interests":  IntVar(  name =  "Interests") , 
        }
        
        
        self.all_time = {
            "Change": IntVar(  name =  "Change") , 
            "Change %": IntVar(  name =  "Change %") , 
            "Annualized XIRR": IntVar(  name =  "Annualized XIRR") , 
            "Unannualized XIRR": IntVar(  name =  "Unannualized XIRR") , 
            "Unannualized 2Y": IntVar(  name =  "Unannualized 2Y") , 
            "Unannualized 5Y": IntVar(  name =  "Unannualized 5Y") , 
            "Unannualized 10Y": IntVar(  name =  "Unannualized 10Y") , 
            "Value": IntVar(  name =  "Value") , 
            "Cost Basis": IntVar(  name =  "Cost Basis") , 
            "Dividends": IntVar(  name =  "Dividends") , 
            "Interests": IntVar(  name =  "Interests") , 
            "Commissions": IntVar(  name =  "Commissions") , 
        }
        
        self.realized = {
            "Change": IntVar(  name =  "Change") , 
            "Value": IntVar(  name =  "Value") , 
            "Cost Basis": IntVar(  name =  "Cost Basis") , 
        }

        
        self.unrealized = {
            "Change": IntVar(  name =  "Change") , 
            "Value": IntVar(  name =  "Value") , 
            "Cost Basis": IntVar(  name =  "Cost Basis") , 
            "Shares": IntVar(  name =  "Shares") , 
            "Cost Per Share": IntVar(  name =  "Cost Per Share") , 
        }


        self.allMetrics = { "ytd": self.ytd,
                        "all_time": self.all_time ,
                        "realized": self.realized ,
                        "unrealized": self.unrealized} 

        

class PortfolioHoldings:
    wallet = {
        "USD" : 0
    }


GUI().mainloop()







