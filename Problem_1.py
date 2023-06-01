def problem_1(data, W):
    n = len(data)
    t = [[0 for _ in range(W+1)] for _ in range(n+1)]
    i = 1
    while(i<n+1):
        j = 1
        while(j<W+1):
            if data[i-1]["weight"] <= j:
                t[i][j] = max(data[i-1]["value"] + t[i-1][j-data[i-1]["weight"]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j];
            j += 1
        i += 1
    return t[n][W]

# print(problem_1([{ "name":"map", "weight":9, "value":150 },
#                  { "name":"compass", "weight":13, "value":35 }, 
#                  { "name":"water", "weight":153, "value":200 }, 
#                  { "name":"sandwich", "weight":50, "value":160 }, 
#                  { "name":"glucose", "weight":15, "value":60 }, 
#                  { "name":"tin", "weight":68, "value":45 },
#                  { "name":"banana", "weight":27, "value":60 },
#                  { "name":"apple", "weight":39, "value":40 }], 100) )

data = []
n = input("Enter the number of items: ")
for i in range(int(n)):
    input_dict={}
    input_dict["name"] = input("Enter name of item: ")
    input_dict["weight"] = int(input("Enter the weight of that item: "))
    input_dict["value"] = int(input("Enter the cost of that item: "))
    data.append(input_dict)
max_wt = int(input("Enter Maximum Weight: "))
print(problem_1(data, max_wt))

