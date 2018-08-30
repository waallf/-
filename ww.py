n,m = list(map(int,input().strip().split()))

all_data = []
for i in range(n):
    temp_list = []
    temp_str = input().strip()
    for j in range(m):
        temp_list.append(temp_str[j] ) 
    all_data.append(temp_list)

for j in range(m):
    x_start=-1
    x_index=n-1
    while(x_index>=0):
        if all_data[x_index][j] =='x':
            x_start = x_index  
        #elif all_data[x_index][j] =='.':
            #continue
        elif all_data[x_index][j] =='o' :
            if x_start == -1:
                all_data[x_index][j] ='.'
            else:
                all_data[x_index][j] ='.'
                all_data[x_start-1][j] = 'o'
                x_start = x_start-1
        x_index = x_index-1        
            
for i in range(n):
    str_temp = ''
    for j in range(m):
        str_temp = str_temp+str(all_data[i][j])
    print(str_temp)
