import pandas as pd
import statistics as st
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data\medium_data.csv")

claps = df["claps"].tolist()

population_meanOfClaps = st.mean(claps)

ClapsMean = []


for i in range(0, 100):

    spDataOfClaps = []

    for i in range(0, 30):
        randomIndexofClaps = random.randint(0, len(claps)-1)
        Claps_Value = claps[randomIndexofClaps]
        spDataOfClaps.append(Claps_Value)

    Mean_spData_Claps = st.mean(spDataOfClaps)

    ClapsMean.append(Mean_spData_Claps)


SampleClapMean = st.mean(ClapsMean)
SampleClapsSTD = st.stdev(ClapsMean)


print("Population Claps Mean: ", population_meanOfClaps)
print("Sample Claps Mean: ", SampleClapMean)


Std1_Start, Std1_End = SampleClapMean - \
    SampleClapsSTD, SampleClapMean + SampleClapsSTD

Std2_Start, Std2_End = SampleClapMean - 2 * \
    (SampleClapsSTD),  SampleClapMean + 2 * (SampleClapsSTD)

Std3_Start, Std3_End = SampleClapMean - 3 * \
    (SampleClapsSTD),  SampleClapMean + 3 * (SampleClapsSTD)


graph = ff.create_distplot([ClapsMean], ["Claps Mean"], show_hist=False)
graph.add_trace(go.Scatter(x=[SampleClapMean, SampleClapMean],
                           y=[0, 0.003], mode='lines', name=" Sample Mean"))

graph.add_trace(go.Scatter(x=[population_meanOfClaps, population_meanOfClaps],
                           y=[0, 0.003], mode='lines', name="Mean"))

# sd1 Trace
graph.add_trace(go.Scatter(x=[Std1_Start, Std1_Start],
                           y=[0, 0.003], mode='lines', name="Std1 Start"))
graph.add_trace(go.Scatter(x=[Std1_End, Std1_End],
                           y=[0, 0.003], mode='lines', name="Std1 End"))


# sd2 trace
graph.add_trace(go.Scatter(x=[Std2_Start, Std2_Start],
                           y=[0, 0.003], mode='lines', name="Std2 Start"))
graph.add_trace(go.Scatter(x=[Std2_End, Std2_End],
                           y=[0, 0.003], mode='lines', name="Std2 End"))

# sd 3 trace
graph.add_trace(go.Scatter(x=[Std3_Start, Std3_Start],
                           y=[0, 0.003], mode='lines', name="Std3 Start"))
graph.add_trace(go.Scatter(x=[Std3_End, Std3_End],
                           y=[0, 0.003], mode='lines', name="Std3 End"))


# Z Score
z_scoreData = (SampleClapMean - population_meanOfClaps)/st.stdev(claps)
print("Z Score: ",z_scoreData)


graph.show()