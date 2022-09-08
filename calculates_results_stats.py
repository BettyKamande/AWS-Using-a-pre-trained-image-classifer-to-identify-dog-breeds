#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:BETTY KAMANDE
# DATE CREATED: 16.08.2022                                 
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """   
    results_stats_dic = dict()
    #Z
    num_of_images = len(results_dic)
    #A
    num_dog_match = 0
    for key, values in results_dic.items():
        if values[3] == 1 and values[4] == 1:
            num_dog_match += 1
            #print("Number of correct dog matches is {}".format(num_dog_match))
    #C
    num_notdog_match = 0
    for key, values in results_dic.items():
        if values[3] ==0 and values[4] == 0:
            num_notdog_match += 1
            #print("Number of correct Non-dog matches is {}".format(num_notdog_match))
    #B / D
    num_dog_images = 0
    num_notdog_images = 0
    for key, labels in results_dic.items():
        if labels[3] == 1:
            num_dog_images += 1
            #print("Number of dog images is {}".format(num_dog_images))
        else:
            num_notdog_images += 1
            #print("Number of Not dog images is {}".format(num_notdog_images))
    #E
    num_breed_match = 0
    for key, labels in results_dic.items():
        if labels[3] == 1 and labels[2] == 1:
            num_breed_match += 1
            #print("Number of correct breed matches is {}".format(num_breed_match))
    #Y
    num_label_match = 0
    for key, labels in results_dic.items():
        if labels[2] == 1:
            num_label_match += 1
            #print("Number of label matches is {}".format(num_label_match))
    #A/B
    pct_dog_image = num_dog_match / num_dog_images * 100
    
    #C/D
    if num_notdog_images > 0:
        pct_notdog_image = num_notdog_match / num_notdog_images * 100
    else:
        print("0")
    #E/B
    pct_dog_breed = num_breed_match / num_dog_images * 100
    
    #Y/Z
    pct_label_match = num_label_match / num_of_images * 100
    #Add key-value to the results_stats_dic dictionary
    key = ('n_correct_dogs', 'pct_correct_dogs', 'n_correct_breed', 'pct_correct_breed')
    value = (num_dog_match, pct_dog_image, num_breed_match, pct_dog_breed)
    results_stats_dic['n_correct_dogs'] = num_dog_match
    results_stats_dic['pct_correct_dogs'] = pct_dog_image
    results_stats_dic['n_correct_breed'] = num_breed_match
    results_stats_dic['pct_correct_breed'] = pct_dog_breed
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_dogs_img'] = num_dog_images
    results_stats_dic['n_notdogs_img'] = num_notdog_images
    results_stats_dic['pct_correct_notdogs'] = pct_notdog_image
    
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    print(results_stats_dic)
    return results_stats_dic
