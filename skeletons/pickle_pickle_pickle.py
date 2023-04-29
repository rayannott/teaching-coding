import pickle
import os
import math
from datetime import datetime
from dataclasses import dataclass


@dataclass
class SensorData:
    '''
    A main object storing one recording datum.
    
    time_stamp: Unix timestamp
    temperature: local air temperature in Celsius
    location: location as (latitude, longitude)
    '''
    time_stamp: float
    temperature: float
    location: tuple[float, float]
    
    def __lt__(self, other: 'SensorData') -> bool:
        return self.time_stamp < other.time_stamp

    def __str__(self) -> str:
        return f'({datetime.fromtimestamp(self.time_stamp)}) {self.temperature:.1f}C at lat={self.location[0]} lon={self.location[1]}'


SensorDataList = list[SensorData]

def load_all_sensor_data():
    '''
    Load a pickled object from a file and return it.
    '''
    FOLDER_NAME = 'files'; FILE_NAME = 'pickle_data.pickle'
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---

def sort_by_time(sensor_data_list: SensorDataList):
    '''
    Sort a list of SensorData objects by timestamps (early - first)
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---

def coordinates_of_first_recording(sensor_data_list: SensorDataList) -> tuple[float, float]:
    '''
    Return a coordinate tuple of the earliest recording in the list.
    Note: suppose the list is already sorted.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---
    
def get_filtered_temperatures(sensor_data_list: SensorDataList) -> SensorDataList:
    '''
    Return a list of SensorData objects with temperatures in range (20.0, 25.0).
    Keep the original order.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---

def distance(loc1: tuple[float, float], loc2: tuple[float, float]) -> float:
    '''
    Return a Euclidian distance between two points on the plane.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---

def find_closest_sd(location: tuple[float, float], sensor_data_list: SensorDataList) -> SensorData:
    '''
    Return a SensorData object recorded closest to a given coordinate point.
    '''
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---

def save_sensor_data(sensor_data_list: SensorDataList):
    '''
    Pickle the sorted and filtered list of SensorData objects 
    '''
    SAVE_TO = 'sorted_sd.wtf'
    # --- YOUR CODE HERE ---
    
    # --- END OF YOUR CODE ---


'''
Uncomment this to run the code
'''
# sd_list = load_all_sensor_data()
# sort_by_time(sd_list)
# first_rec_location = coordinates_of_first_recording(sd_list)
# print('first recording location:', first_rec_location)
# sd_list_filtered = get_filtered_temperatures(sd_list)
# LOC = (55.7557, 37.6419)
# closest_sd = find_closest_sd(location=LOC, sensor_data_list=sd_list_filtered)
# print(f'closest to {LOC} is {closest_sd}')
# save_sensor_data(sd_list_filtered)
