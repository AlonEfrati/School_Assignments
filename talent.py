import matplotlib.pyplot as plt
type = None
teams = ['WK Men 2021/2022', 'WK Men 2016/2017', 'WK Men 2012/2013', 'WK Men 2008/2009', "Women's team"]
height = []

X = [1, 2, 3, 4]
TICK = ['jan-mar', 'april-june', 'jul-sep', 'oct-dec']

# The different values of the different WK of men, including the total values of the women's team

height1 = [13,10,7,10]
height2 = [24,9,9,11]
height3 = [19,11,11,5]
height4 = [6,7,7,10]
height_women = [52,46,43,42]

total = []
for i in range(len(height1)):
    summed_up = height1[i] + height2[i] + height3[i] + height4[i]
    total.append(summed_up)

type = 'Men'
if type == 'Men':
    figure, axis = plt.subplots(2, 2)
    # For Sine Function
    axis[0, 0].bar(X, height1, tick_label = TICK)
    axis[0, 0].set_title(teams[0])

    # For Cosine Function
    axis[0, 1].bar(X, height2, tick_label = TICK)
    axis[0, 1].set_title(teams[1])

    # For Tangent Function
    axis[1, 0].bar(X, height3, tick_label = TICK)
    axis[1, 0].set_title(teams[2])

    # For Tanh Function
    axis[1, 1].bar(X, height4, tick_label = TICK)
    axis[1, 1].set_title(teams[3])

elif type == 'Men total':
    plt.bar(X, total, tick_label = TICK, width = 0.8,)

elif type == 'Woman':
    plt.bar(X, height_women, tick_label=TICK, width=0.8, )

else:
    print('No type or correct type was given')

# naming the x-axis
plt.xlabel('Birthmonths')
# naming the y-axis
plt.ylabel('Amount of players')

# function to show the plot
plt.show()
