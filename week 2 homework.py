import matplotlib.pyplot as plot
# set up your lists
numlist = [8, 6, 5, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['purple', 'green', 'pink', 'yellow' ]
explodelist = [0.0, 0.5, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.0f%%', colors=colorlist,
    	explode = explodelist, startangle = 30)
plot.axis('equal')
plot.savefig('piechart.png')