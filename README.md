# Plot-pie-chart-using-Matplotlib
A Pie Chart is a circular statistical plot that can display only one series of data. The area of the chart is the total percentage of the given data. The area of slices of the pie represents the percentage of the parts of the data. The slices of pie are called wedges. The area of the wedge is determined by the length of the arc of the wedge. The area of a wedge represents the relative percentage of that part with respect to whole data. Pie charts are commonly used in business presentations like sales, operations, survey results, resources, etc as they provide a quick summary.

# Creating Pie Chart
Matplotlib API has pie() function in its pyplot module which create a pie chart representing the data in an array.

Syntax: matplotlib.pyplot.pie(data, explode=None, labels=None, colors=None, autopct=None, shadow=False)

Parameters:
data represents the array of data values to be plotted, the fractional area of each slice is represented by data/sum(data). If sum(data)<1, then the data values returns the fractional area directly, thus resulting pie will have empty wedge of size 1-sum(data).
labels is a list of sequence of strings which sets the label of each wedge.
color attribute is used to provide color to the wedges.
autopct is a string used to label the wedge with their numerical value.
shadow is used to create shadow of wedge.
