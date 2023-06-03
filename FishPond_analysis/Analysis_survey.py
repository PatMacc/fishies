import pandas as pd
import numpy as np
import math
import random


age = np.random.randint(1,30, size = 250 )
species = ("Karp", "Płotka", "Sum", "Złota Rybka")
species2 = np.random.choice(species, size = 250)
weight = np.random.randint(1,70, size = 250)

data = {
    'Age': age,
    'Species': species2,
    'Weight': weight

}

Pond = pd.DataFrame(data)


karp_pop = Pond[Pond['Species'] == "Karp"] 
płotka_pop = Pond[Pond['Species'] == "Płotka"]
sum_pop = Pond[Pond['Species'] == "Sum"]
goldfish_pop = Pond[Pond['Species'] == "Złota Rybka"]


#Conducting more versatile survey for simple analysis for 'Species' of choice,
#instead of making huge chunk of data while conducting analysis for every 'Species' separately.
# Worth noticing: I,ve generated semirandom data for the sake of testing this alghoritm, so it shouldn't
#be treated as any specific dataset nor scientific analysis. It's purely for fun of exploring :)

def fish_stats(x):
    print("Hi! Im bot conducting analysis of your fish species of choice.\nI know, that raw data can be a bit confusing, so I will interpret the outcomes for you.\n\n")
    number_tot = len(x)
    print( "Total number of chosen species: " , number_tot,)
    print ("1. Statistics for age:\n")

    age_max = x['Age'].max()
    print( "The oldest fish is: ", age_max , "years old" )

    age_min = x['Age'].min()
    print( "The youngest fish is: ", age_min , "years old" )

    age_avg = x['Age'].mean().round(2)
    print( "The averrage age of fish is: ", age_avg, "years old\n"  ) 

    print("There are ",  len(x[x.Age > age_avg]) , " fishes older than averrage") 



    print ("2. Statistics for weight of fishes:\n")

    weight_max = x['Weight'].max()
    print( "The heaviest fish is: ", weight_max , "kg" )

    weight_min = x['Weight'].min()
    print( "The lightest fish is: ", weight_min , "kg" )

    weight_avg = x['Weight'].mean().round(2)
    print( "The averrage weight of fish is: ", weight_avg , "kg" )

    print("There are ",  len(x[x.Weight > weight_avg]) , "fishes heavier than averrage\n")

    print("3. (Maybe) interesting tables:\n\n") 

    
    print("Table 1. This table shows sorted ascending(growing) values of Age and corresponding Weight value( also growing) \n")
    
    fish_sorted = x.sort_values(['Age','Weight'], ascending = [True,True])
    print(fish_sorted )
    

    print("\nTable 2. This table represents averrage Weight for every unique Age group")

    age_groups = x.groupby(['Age'])['Weight'].mean()
    print(age_groups)

    print("\n\n4. Correlation")

    from scipy.stats import shapiro 
    print(shapiro(x['Age']))
    print(shapiro(x['Weight'])) 

    #considering the fact, that the data is randomly generated each session p-values may vary. 
    #In most cases (where the distribution isn't normal) it is recommended to use nonparametrical correlation methods.
    #There are 2 alternative ways to solve this problem:

    #1. Recall Central Limit Theorem, which indicates, that with increasing sample size, sample distribution becomes 
        #more similar to the normal distribution and then use parametrical analysis methods (if the variable is numerical)
    #2. Use nonparametrical analysis method to further explore data. This way is certainly more cautious.

    #Thus, Im going to test the correlation between two variables('Age' and 'Weight) with nonparametrical test, considering
    #at least one of them doesn't have normal distribution.
  
    from scipy.stats import spearmanr
    
    corr_base = x[['Age', 'Weight']]
     
    print(spearmanr (corr_base['Weight'], corr_base['Age']))
    
    p_value = spearmanr (corr_base['Weight'], corr_base['Age']).pvalue 
    
    if p_value <= 0.005: 
        print("\n\n The correlation is statistically significant. Weight and Age of fishes are influenced by eachother. ")
    else:
        print("\n\n The correlation is statistically insignificant. Weight and Age of fishes are not influencing eachother.")
    
    print("\n\nThank You for reading all of this. I hope this analysis is clear, goodbye! :)")
    quit()
        

print("This is The Pond Database, please choose one of the following fish species:\n 1. Karp\n 2. Płotka\n 3.Sum\n 4. ZłotaRybka")
choice =input()

if choice == "1":
    choice = karp_pop 
elif choice == "2":
    choice = płotka_pop
elif choice == "3":
    choice = sum_pop
elif choice == "4":
    choice = goldfish_pop

fish_stats(choice) 
#This is the main function, where all the calculations take place
