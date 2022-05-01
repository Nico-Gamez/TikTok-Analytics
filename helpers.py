#Convert processing code to function
def process_results(data):
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats']
    skip_values = ['challenges', 'duetInfo', 'textExtra', 'stickerOnItem']
    
    #Create blank dictionary
    flattened_data = {}
    #Loop through each video
    for index, value in enumerate(data):
        flattened_data[index] = {}
        #Loop through each property in each video
        for property_index, property_value in value.items():
            #Check if nested
            if property_index in nested_values:
                if property_index in skip_values:
                    pass
                else:
                    #Loop through each nested property
                    for nested_index, nested_value in property_value.items():
                        flattened_data[index][property_index+'_'+nested_index] = nested_value
            #If it's not nested, add it back to the flattened dictionary        
            else:
                flattened_data[index][property_index] = property_value   
                    
    return flattened_data