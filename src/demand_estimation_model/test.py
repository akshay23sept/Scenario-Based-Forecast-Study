 #OASyS Project (Nov 2019 to Nov 2020)

  #First Author: Akshay Anand

 #from assumptions import avg_speed_uam, time_to_vertiport, time_board, time_deboard, time_to_destination

# #print(scipy.stats.norm(1, 2).cdf(2) - scipy.stats.norm(1,2).cdf(0.5))
#K = 7

# avg_income = 60000
# xloc = avg_income/(K+1)
# scl = xloc
# args_ppf = [K,xloc,scl]
# x = np.linspace(
# 	scipy.stats.exponnorm.ppf(0.005, *args_ppf), 
# 	200000, 100)
# # print('low: '+str(scipy.stats.exponnorm.ppf(0.001, *args_ppf)))
# # print('high: '+str(scipy.stats.exponnorm.ppf(0.999, *args_ppf)))
# # print('% below 0: '+str(scipy.stats.exponnorm.cdf(0,*args_ppf)))
# # print('mean: '+str(scipy.stats.exponnorm.mean(*args_ppf)))
# # print('median: '+str(scipy.stats.exponnorm.median(*args_ppf)))
# args_pdf = [x,K,xloc,scl]
# plt.plot(x, scipy.stats.exponnorm.pdf(*args_pdf), alpha=0.6, label='exponnorm pdf')
# plt.xlabel('Annual Income (EUR)')
# plt.ylabel('Population Percentage (%)')
# plt.title('Annual Household Income Distribution')
# print((
# 		scipy.stats.exponnorm.cdf(100000, K, avg_income/(K+1), avg_income/(K+1)) 
# 		- scipy.stats.exponnorm.cdf(0, K, avg_income/(K+1), avg_income/(K+1))
# 		))
# plt.show()
#median needs to be 56k

# x = np.linspace(0,40,100)
# plt.plot(x, uniform.pdf(x,loc=10,scale=10), label='uniform pdf')
# plt.xlabel('Trip Distance (km)')
# plt.ylabel('Frequency')
# plt.show()

# avg_inc = 40000
# std_dev = avg_inc/4*2
# x = np.linspace(norm(avg_inc, std_dev).ppf(0.001),norm(avg_inc, std_dev).ppf(0.999),100)
# plt.plot(x, norm(avg_inc, std_dev).pdf(x), label='norm pdf')


### SKEWNORM ####

# parameters
# a = 10
# x_shift = 10
# dist_scale = 30

# print('low: '+str(skewnorm.ppf(0.0001, a, loc = x_shift, scale = dist_scale)))
# print('high: '+str(skewnorm.ppf(0.9999, a, loc = x_shift, scale = dist_scale)))

# x = np.linspace(
# 	0,
# 	skewnorm.ppf(0.9999, a, loc = x_shift, scale = dist_scale), 100)
# # print('mean: '+str(skewnorm.mean(a,x_shift,dist_scale)))
# # print('median: '+str(skewnorm.median(a,x_shift,dist_scale)))
# plt.plot(x, skewnorm.pdf(x, a, loc=x_shift, scale=dist_scale),'r-', alpha=0.6, label='skewnorm pdf')
# plt.xlabel('Trip Distance (km)')
# plt.ylabel('Trip Percentage (%)')
# plt.title('Trip Distance Distribution')
#### BETAPRIME ####

# parameters
# a = 150
# b = 8
# x_shift = 0
# dist_scale = 1

# print('low: '+str(betaprime.ppf(0.0001, a, loc = x_shift, scale = dist_scale)))
# print('high: '+str(betaprime.ppf(0.9999, a, loc = x_shift, scale = dist_scale)))

# print(scipy.stats.betaprime.cdf(50, a, b) - scipy.stats.betaprime.cdf(20, a, b))

# x = np.linspace(
# 	scipy.stats.betaprime.ppf(0.0001, a, b),
# 	scipy.stats.betaprime.ppf(0.9999, a, b), 
# 	100)

# plt.plot(x, scipy.stats.betaprime.pdf(x, a, b),
# 	'r-', alpha=0.6, label='betaprime pdf')


#### SKEWNORM INCOME ####
# avg_inc = 40000
# std_dev = avg_inc*4
# a = 5
# avg_inc = avg_inc-avg_inc/a*5

# print('low: '+str(skewnorm.ppf(0.0001, a, avg_inc, std_dev)))
# print('high: '+str(skewnorm.ppf(0.9999, a, avg_inc, std_dev)))
# print('pct less than 0: '+str(skewnorm.cdf(0, a, avg_inc, std_dev)))
# print('stats: '+str(skewnorm.stats(a, avg_inc, std_dev, moments='mv')))

# x = np.linspace(
# 	skewnorm.ppf(0.0001, a, avg_inc, std_dev),
# 	skewnorm.ppf(0.9999, a, avg_inc, std_dev),
# 	100)
# plt.plot(x, skewnorm.pdf(x, a, avg_inc, std_dev), label='skewnorm pdf')
# plt.xlabel('Annual Income ($)')
# plt.ylabel('Population Percentage (%)')
# plt.title('Annual Income Distribution')

### sum of norms ####
# avg_inc_1 = 40000
# std_dev_1 = avg_inc_1/4
# print('low: '+str(norm.ppf(0.0001, avg_inc_1, std_dev_1)))
# a = 15
# avg_inc_2 = 20000
# std_dev_2 = avg_inc_2*5
# print('low: '+str(skewnorm.ppf(0.0001, a, avg_inc_2, std_dev_2)))
# print('high: '+str(skewnorm.ppf(0.9999, a, avg_inc_2, std_dev_2)))
# # quit()
# # print('low: '+str(skewnorm.ppf(0.0001, a, avg_inc, std_dev)))
# # print('high: '+str(skewnorm.ppf(0.9999, a, avg_inc, std_dev)))
# # print('pct less than 0: '+str(skewnorm.cdf(0, a, avg_inc, std_dev)))
# # print('stats: '+str(skewnorm.stats(a, avg_inc, std_dev, moments='mv')))

# x = np.linspace(
# 	norm.ppf(0.0001, avg_inc_1, std_dev_1),
# 	skewnorm.ppf(0.9999, a, avg_inc_2, std_dev_2),
# 	100)
# plt.plot(x, norm.pdf(x, avg_inc_1, std_dev_1)+skewnorm.pdf(x, a, avg_inc_2, std_dev_2), label='norm pdf')


# a = 20
# x_shift = 7
# dist_scale = 30

# td_step_1 = scipy.stats.skewnorm.ppf(0.9999, a, x_shift, dist_scale)
# n = 20
# td_low = np.linspace(0, td_step_1-td_step_1/n, n)
# td_high = np.linspace(td_step_1/n, td_step_1, n)

# x = np.linspace(
# 	skewnorm.ppf(0.0001, a, x_shift, dist_scale),
# 	skewnorm.ppf(0.9999, a, x_shift, dist_scale),
# 	100)
# plt.plot(x, skewnorm.pdf(x, a, x_shift, dist_scale), label='skewnorm pdf')
# plt.xlabel('Trip Distance (km)')
# plt.ylabel('Trip Percentage (%)')
# plt.title('Personal Vehicle Trip Distance Distribution')

# print(td_step_1)
# print(td_low)
# print(td_high)

# cluster 5:
# mu = 1.39822241945866
# sigma = 1.54893530212703
# x = np.linspace(
# 	scipy.stats.lognorm.ppf(0.0001, sigma), 
# 	scipy.stats.lognorm.ppf(0.999, sigma),
# 	100)
# plt.plot(x, scipy.stats.exponnorm.pdf(x,sigma,scale=math.exp(mu)))

# mu = 1.52033688356149
# sigma = 1.61484214170438
# x = np.linspace(
# 	scipy.stats.lognorm.ppf(0.0001, sigma), 
# 	scipy.stats.lognorm.ppf(0.995, sigma),
# 	100)
# plt.plot(x, scipy.stats.exponnorm.pdf(x,sigma,scale=math.exp(mu)))

# mu = 2.58584772700958
# sigma = 1.64631611020817
# x = np.linspace(
# 	scipy.stats.lognorm.ppf(0.0001, sigma), 
# 	scipy.stats.lognorm.ppf(0.999, sigma),
# 	100)
# plt.plot(x, scipy.stats.exponnorm.pdf(x,sigma,scale=math.exp(mu)))

# mu = 1.708491274857
# sigma = 1.63874146496014
# x = np.linspace(
# 	scipy.stats.lognorm.ppf(0.0001, sigma), 
# 	scipy.stats.lognorm.ppf(0.999, sigma),
# 	100)
# plt.plot(x, scipy.stats.exponnorm.pdf(x,sigma,scale=math.exp(mu)))


# plt.xlabel('Trip Distance (km)')
# plt.ylabel('Population Percentage (%)')
# plt.title('Trip Distance Distribution for Mexico City')


# x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 12]
# y_150 = (
# 	[6355, 2313, 1207, 708, 437, 287, 196, 131, 94, 69, 49, 37, 2.1])
# y_300 = (
# 	[2645, 1065, 541, 306,182,119, 77, 52, 36, 26, 18, 14, 0.7])
# y_450 = (
# 	[1607,635, 327, 185, 112, 71, 47, 31, 22, 16,12, 8, 0.4])
# plt.plot(x,y_150,'.-',x,y_300,'.-',x,y_450,'.-')
# # plt.yscale('log')
# plt.legend(['150 $km^2$/vertiport','300 $km^2$/vertiport','450 $km^2$/vertiport'])
# plt.xlabel('UAM Ticket Cost ($/passenger mile)')
# plt.ylabel('Passenger Trips (Million)')
# plt.title('Annual UAM Passenger Trips vs UAM Ticket Cost')

# x = [150,300,450]
# y1 = [6355,2645,1607]
# y2 = [2313,1065,635]
# # y3 = [1207,541,327]
# y4 = [708,306,185]
# # y5 = [437,182,112]
# y6 = [287,119,71]
# # y7 = [196,77,47]
# y8 = [131,52,31]
# # y9 = [94,36,22]
# y10 = [69,26,16]
# # y11 = [49,18,12]
# y12 = [37,14,8]
# y13 = [2.1,0.7,0.4]


# # plt.plot(x,y1,'.-',x,y2,'.-',x,y3,'.-',x,y4,'.-',x,y5,'.-',x,y6,'.-',x,y7,'.-',x,y8,'.-',x,y9,'.-',x,y10,'.-',x,y11,'.-',x,y12,'.-',x,y13,'.-')
# plt.plot(x,y1,'.-',x,y2,'.-',x,y4,'.-',x,y6,'.-',x,y8,'.-',x,y10,'.-',x,y12,'.-',x,y13,'.-')
# # plt.yscale('log')
# # plt.legend(['$0.50','$1.00','$1.50','$2.00','$2.50','$3.00','$3.50','$4.00','$4.50','$5.00','$5.50','$6.00','$12.00'], bbox_to_anchor=(1.04, 1.0), loc='upper left')
# # plt.legend(['$0.50','$1.00','$2.00','$3.00','$4.00','$5.00','$6.00','$12.00'], bbox_to_anchor=(1.04, 1.0), loc='upper left')
# plt.legend(['$0.50','$1.00','$2.00','$3.00','$4.00','$5.00','$6.00','$12.00'])
# # plt.subplots_adjust(right=0.7)
# plt.xlabel('Vertiport Density ($km^2$/vertiport)')
# plt.ylabel('Passenger Trips (Million)')
# plt.title('Annual UAM Passenger Trips vs Vertiport Density')

# # ## Show all plots ####
# plt.show()

# input_data = pd.read_excel('31_cities.xlsx')
# input_data = input_data.iloc[[20],:]
# print(input_data['pv_speed_reg_coeff_a'])
# if input_data['pv_speed_reg_coeff_a'].isna().iloc[0]:
# 	print(input_data['pv_speed_reg_coeff_a'].isna().iloc[0])
# else:
# 	print(input_data['pv_speed_reg_coeff_a'].isna().iloc[0])

# print(n_steps)
# cases_list = pd.read_excel('cases_list.xlsx')
# costs = list(cases_list['uam ticket cost'])
# densities = list(cases_list['vertiport density'])
# print(costs)
# for case in cases_list:
# 	print(case)