import csv
import pandas as pd
import matplotlib.pyplot as plt

# changes format of .flow file so Midas can process it (tokenizes ips and time)

def modify_format(input_file):
    filename = input_file.split('.')[0] # to be used to maintain naming consistency with other functions
    index = []
    data = []
    vals = []
    times = []
    i = 0
    sources = {} # will hold source ips and corresponding tokens
    token = 1 # token counter 
    dests = {} # will hold dest ips and corresponding tokens
    
    with open (input_file, 'r') as f:
        while True:         
            line = f.readline()
            if line == '': # loop through until EOF is reached 
                break
            words = line.split(' ')
            # gets rid of the excess spaces between values
            while '' in words:
                words.remove('')
                        
            for num in range(len(words)): 
                if (words[num].isdigit() == False) and ('.' in words[num]): # i.e. if words[num] is source/dest ip or start/end time only
                    data.append(words[num]) 
                           
            if len(data) != 0: # data = [] for the header 
                vals.append(data[:-1]) # end time is not needed 
                temp = vals[i].pop(-1)
                temp = temp.split('.')
                temp = temp[0][0:5] # time format changed from 05:04:23.241037 to 05.04
                times.append(temp)
                # vals now holds only addrs, times are in separate list 
                
                if vals[i][0] in sources:
                    vals[i][0] = sources[vals[i][0]] # tokenizes if address has already appeared 
                if vals[i][1] in dests:
                    vals[i][1] = dests[vals[i][1]]
                
                if vals[i][0] not in sources:
                    sources[vals[i][0]] = token 
                    vals[i][0] = token
                    token += 1 # at the end, token will represent the number of unique addresses 
                if vals[i][1] not in dests:
                    dests[vals[i][1]] = token 
                    vals[i][1] = token 
                    token += 1
                
                data = [] # clears data so next line can be stored here by itself in the next iteration 
                i += 1
   
        if len(vals) != 0:    
            time = times[0]
            count = 1
            for t in range(len(times[:])):
                if times[:][t] == time: # changes time format to 1, 1, 1, 2, 3 (consecutive same times = same num)
                    times[t]  = count 
                    
                else:
                    count += 1
                    time = times[t]
                    times[t] = count 
            
                vals[t].append(times[t]) # adds times back into vals so it's [source_ip, dest_ip, time]
    output_file = f"{filename}.csv"       
    with open(output_file, 'w', newline='') as out: # newline='' prevents additional rows in-between lines
        writer = csv.writer(out) 
        writer.writerows(vals)
    return filename
    

#modify_format('rbot.flow', 'rbot.csv')

###############################################################

# used after running Midas with data formatted by modify_format function
# converts the values in Score.txt to float type and normalizes them  

def norm(input_file, output_file):
    with open(input_file, 'r') as inp:
        contents = inp.read()
        nums = contents.split()
    
    for n in range(len(nums)):
        nums[n] = float(nums[n])
    
    maximum = max(nums)
    
    with open(output_file, 'w') as out:
        out.write(f"Max is {maximum}\n") # used for reference, will not be used in add_data function
        for n in range(len(nums)):
            nums[n] = f"{(nums[n])/maximum:.6f}\n" # normalizing by dividing by max in data set
            out.write(nums[n]) 
            
#norm('rbot_anomaly_score.txt', 'normalized_rbot_anomaly_score.txt')

###############################################################

# after norm function normalizes the data, add_data function adds it to the csv to produce the final scores

def add_data(data, scores, output_file):
    with open(scores, 'r') as sc: # nums contains the scores from the appropriate Score.txt file 
        contents = sc.read()
        nums = contents.split()
        nums = nums[3:] # ignoring the "Max is __" line 
    
    values = [] # will hold the contents of input file (i.e. 2 ips and time)
    with open(data, 'r') as da: 
        reader = csv.reader(da)
        for row in reader:
            values.append(row)
    
    for val in range(len(values)): # adds each score to its corresponding 2 ips and time
        values[val].append(nums[val])
    
    with open(output_file, 'w', newline='') as out: # newline='' prevents additional rows in-between lines
        writer = csv.writer(out) 
        writer.writerows(values)

#add_data('rbot.csv', 'normalized_rbot_anomaly_score.txt', 'rbot_modified.csv')

###############################################################

# uses output_file from add_data function to make a graph of seconds vs. score to observe analyzed data

def graph_data(input_file):
    df = pd.read_csv(input_file)
    df.columns = ['Source', 'Dest', 'Seconds','Score']
    x = df['Seconds']
    y = df['Score']
    plt.scatter(x,y)
    plt.title("Seconds vs. Score")
    plt.xlabel("Seconds") 
    plt.ylabel("Score")
    plt.show()
    
#graph_data('botnet_modified.csv')
#graph_data('rbot_modified.csv')
    