'''
                  LEGEND
                  
                  Network Functions
========================================================
(0) S   : Source
(1) NAT : Network Address Translation
(2) FW  : Firewall
(3) TM  : Traffic Monitor
(4) WOC : WAN Optimization Controller
(5) VOC : Video Optimization Controller
(6) IDS : Intrusion Detection System
(7) D   : Destiny


# id = Function Identifier 
# cf = CPU Capacity Required by Function 
# bf = Traffic Processin Capacity (Function) in Mb/s (200Mb/s = 200000Kb/s) 
# df = Processing Delay (ms)

                  Services
========================================================
(0) wb  : Web Service
(1) vip : VoIP
(2) vs  : Video Streaming
(3) og  : Online Game

'''

def euclidean_distance_function(point1, point2):
    '''
    Calculate the Euclidean distance between two points in a 2D space.

    Parameters:
      point1 (tuple): A tuple representing the coordinates of the first point in the format (x, y).
      point2 (tuple): A tuple representing the coordinates of the second point in the format (x, y).

    Returns:
      float: The Euclidean distance between point1 and point2.

    The Euclidean distance is a measure of the straight-line distance between two points in a 2D space. 
    It is calculated as the square root of the sum of the squared differences of the coordinates in each 
    dimension.

    Example:
    >>> euclidean_distance_function((1, 2), (4, 6))
    5.0
    '''

    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

# A very large number
bigM = 999999999999999999999999999999

# ===============================================================#
#                      Topology Information                      # 
# ===============================================================#

total_nodes = 16 # [0, 1, 2, ..., 15]


position_nodes = { 
                  0 :     [ 237.0, 338.0 ],
                  1 :     [ 130.0, 207.0 ],
                  2 :     [ 126.0, 531.0 ],
                  3 :     [ 209.0, 523.0 ],
                  4 :     [ 345.0, 232.0 ],
                  5 :     [ 95.0, 350.0 ],
                  6 :     [ 302.0, 404.0 ],
                  7 :     [ 161.0, 454.0 ],
                  8 :     [ 394.0, 499.0 ],
                  9 :     [ 389.0, 656.0 ],
                  10 :    [ 237.0, 645.0 ],
                  11 :    [ 277.0, 70.0 ],
                  12 :    [ 540.0, 147.0 ],
                  13 :    [ 592.0, 503.0 ],
                  14 :    [ 490.0, 349.0 ],
                  15 :    [ 463.0, 543.0 ],  }

# Bidirectional Graph
physical_topology = {
     
      (0, 1)   : euclidean_distance_function(position_nodes[0], position_nodes[1]), 
      (0, 4)   : euclidean_distance_function(position_nodes[0], position_nodes[4]), 
      (0, 5)   : euclidean_distance_function(position_nodes[0], position_nodes[5]), 
      (0, 6)   : euclidean_distance_function(position_nodes[0], position_nodes[6]),
      (0, 7)   : euclidean_distance_function(position_nodes[0], position_nodes[7]), 
      (0, 11)  : euclidean_distance_function(position_nodes[0], position_nodes[11]), 
      (0, 12)  : euclidean_distance_function(position_nodes[0], position_nodes[12]), 
      (0, 14)  : euclidean_distance_function(position_nodes[0], position_nodes[14]), 
      (1, 4)   : euclidean_distance_function(position_nodes[1], position_nodes[4]), 
      (1, 5)   : euclidean_distance_function(position_nodes[1], position_nodes[5]), 
      (1, 11)  : euclidean_distance_function(position_nodes[1], position_nodes[11]), 
      (1, 12)  : euclidean_distance_function(position_nodes[1], position_nodes[12]), 
      (1, 14)  : euclidean_distance_function(position_nodes[1], position_nodes[14]), 
      (2, 3)   : euclidean_distance_function(position_nodes[2], position_nodes[3]), 
      (2, 5)   : euclidean_distance_function(position_nodes[2], position_nodes[5]), 
      (2, 6)   : euclidean_distance_function(position_nodes[2], position_nodes[6]), 
      (2, 7)   : euclidean_distance_function(position_nodes[2], position_nodes[7]), 
      (2, 10)  : euclidean_distance_function(position_nodes[2], position_nodes[10]), 
      (3, 6)   : euclidean_distance_function(position_nodes[3], position_nodes[6]), 
      (3, 7)   : euclidean_distance_function(position_nodes[3], position_nodes[7]), 
      (3, 8)   : euclidean_distance_function(position_nodes[3], position_nodes[8]), 
      (3, 9)  : euclidean_distance_function(position_nodes[3], position_nodes[9]), 
      (3, 10)  : euclidean_distance_function(position_nodes[3], position_nodes[10]), 
      (4, 11)  : euclidean_distance_function(position_nodes[4], position_nodes[11]), 
      (4, 12)  : euclidean_distance_function(position_nodes[4], position_nodes[12]), 
      (4, 14)  : euclidean_distance_function(position_nodes[4], position_nodes[14]), 
      (5, 6)   : euclidean_distance_function(position_nodes[5], position_nodes[6]), 
      (5, 7)   : euclidean_distance_function(position_nodes[5], position_nodes[7]), 
      (6, 7)   : euclidean_distance_function(position_nodes[6], position_nodes[7]), 
      (6, 8)   : euclidean_distance_function(position_nodes[6], position_nodes[8]), 
      (6, 9)  : euclidean_distance_function(position_nodes[6], position_nodes[9]), 
      (6, 11)  : euclidean_distance_function(position_nodes[6], position_nodes[10]), 
      (6, 12)  : euclidean_distance_function(position_nodes[6], position_nodes[12]), 
      (6, 13)  : euclidean_distance_function(position_nodes[6], position_nodes[13]), 
      (6, 14)  : euclidean_distance_function(position_nodes[6], position_nodes[14]), 
      (8, 9)  : euclidean_distance_function(position_nodes[8], position_nodes[9]), 
      (8, 10)  : euclidean_distance_function(position_nodes[8], position_nodes[10]), 
      (8, 13)  : euclidean_distance_function(position_nodes[8], position_nodes[13]), 
      (8, 14)  : euclidean_distance_function(position_nodes[8], position_nodes[14]), 
      (8, 15)  : euclidean_distance_function(position_nodes[8], position_nodes[15]), 
      (9, 10) : euclidean_distance_function(position_nodes[9], position_nodes[10]), 
      (9, 13) : euclidean_distance_function(position_nodes[9], position_nodes[13]), 
      (9, 14) : euclidean_distance_function(position_nodes[9], position_nodes[14]), 
      (11, 12) : euclidean_distance_function(position_nodes[11], position_nodes[12]), 
      (11, 14) : euclidean_distance_function(position_nodes[11], position_nodes[14]), 
      (12, 13) : euclidean_distance_function(position_nodes[12], position_nodes[13]), 
      (12, 14) : euclidean_distance_function(position_nodes[12], position_nodes[14]), 
      (13, 14) : euclidean_distance_function(position_nodes[13], position_nodes[13]), 
      (13, 15) : euclidean_distance_function(position_nodes[13], position_nodes[15]), 
} 


# Fiber propagation delay per km [2]
link_delay = 0.01 # (s/km)

# 1Gbps link capacity (1000000 Kbps) [2]
bl  = 1000000


# Energy Consumption [1]
pss = 130   # Switch Power (W)
pp = 1      # Link Power (W)
psm = 150   # Static PM Power (W)
pmm = 250   # Maximum PM Power (W)


# CPU (Core), Memory (GB - 8000000 Kb), and Storage (TB - 8000000000Kb) [1]
# ===         ======                        =======
total_resources = 3

resource_capacity = {
                  'CPU' : 16,
                  'Memory' : 4398080000, # (512 GB)
                  'Storage' : 800000000000 # (100 TB)
                    }


# ===============================================================#
#                     Functions Information                      # 
# ===============================================================#

# [1 / 2]
total_functions = 6 + 2 # [0, 1, 2, ..., 7]


# Set of Functions
#            (id, cf, bf, df) 
functions = [
             (0, 0, bigM, 0),
             (1, 4, 200000, 10),
             (2, 4, 200000, 10),
             (3, 4, 200000, 10),
             (4, 4, 200000, 10),
             (5, 4, 200000, 10),
             (6, 4, 200000, 10),
             (7, 0, bigM, 0),
            ]   


# ===============================================================#
#                    Services Information [1]                    # 
# ===============================================================#


wbf = [1, 1, 1, 1, 1, 0, 1, 1]
      #0  1  2  3  4  5  6  7
wb = [[0, 1, 0, 0, 0, 0, 0, 0], # 0
      [0, 0, 1, 0, 0, 0, 0, 0], # 1
      [0, 0, 0, 1, 0, 0, 0, 0], # 2
      [0, 0, 0, 0, 1, 0, 0, 0], # 3
      [0, 0, 0, 0, 0, 0, 1, 0], # 4
      [0, 0, 0, 0, 0, 0, 0, 0], # 5
      [0, 0, 0, 0, 0, 0, 0, 1], # 6
      [0, 0, 0, 0, 0, 0, 0, 0]] # 7


vipf = [1, 2, 2, 1, 0, 0, 0, 1]
       #0  1  2  3  4  5  6  7
vip = [[0, 1, 0, 0, 0, 0, 0, 0], # 0
       [0, 0, 1, 0, 0, 0, 0, 1], # 1
       [0, 1, 0, 1, 0, 0, 0, 0], # 2
       [0, 0, 1, 0, 0, 0, 0, 0], # 3
       [0, 0, 0, 0, 0, 0, 0, 0], # 4
       [0, 0, 0, 0, 0, 0, 0, 0], # 5
       [0, 0, 0, 0, 0, 0, 0, 0], # 6
       [0, 0, 0, 0, 0, 0, 0, 0]] # 7

vsf = [1, 1, 1, 1, 0, 1, 1, 1]
      #0  1  2  3  4  5  6  7
vs = [[0, 1, 0, 0, 0, 0, 0, 0], # 0
      [0, 0, 1, 0, 0, 0, 0, 0], # 1
      [0, 0, 0, 1, 0, 0, 0, 0], # 2
      [0, 0, 0, 0, 0, 1, 0, 0], # 3
      [0, 0, 0, 0, 0, 0, 0, 0], # 4
      [0, 0, 0, 0, 0, 0, 1, 0], # 5
      [0, 0, 0, 0, 0, 0, 0, 1], # 6
      [0, 0, 0, 0, 0, 0, 0, 0]] # 7

ogf = [1, 1, 1, 0, 1, 1, 1, 1]
      #0  1  2  3  4  5  6  7
og = [[0, 1, 0, 0, 0, 0, 0, 0], # 0
      [0, 0, 1, 0, 0, 0, 0, 0], # 1
      [0, 0, 0, 0, 0, 1, 0, 0], # 2
      [0, 0, 0, 0, 0, 0, 0, 0], # 3
      [0, 0, 0, 0, 0, 0, 1, 0], # 4
      [0, 0, 0, 0, 1, 0, 0, 0], # 5
      [0, 0, 0, 0, 0, 0, 0, 1], # 6
      [0, 0, 0, 0, 0, 0, 0, 0]] # 7


# [Bandwidth (kbps), Delay (ms), functions, SFC]

services = {'wb' : {    'bandwidth' : 100,
                        'delay' : 100,
                        'functions' : wbf,
                        'sfc' : wb},
# ----------------------------------------------   
            'vip' : {   'bandwidth' : 64,
                        'delay' : 100,
                        'functions' : vipf,
                        'sfc' : vip},
# ----------------------------------------------   
            'vs' : {    'bandwidth' : 4000,
                        'delay' : 100,
                        'functions' : vsf,
                        'sfc' : vs},
# ----------------------------------------------   
            'og' : {    'bandwidth' : 50,
                        'delay' : 60,
                        'functions' : ogf,
                        'sfc' : og},
# ----------------------------------------------   
            }

# ===============================================================#
#                       Demand Information                       # 
# ===============================================================#


# Alterar o número de demandas para realizar os testes
total_demands = 8

# Set of demands
# Demand Identifier, Source, Destiny, Service
demands = [ {     'id' : 0, 
                  'source' : 0, 
                  'destiny' : 1, 
                  'service' : services['wb']},

            {     'id' : 1, 
                  'source' : 0, 
                  'destiny' : 4, 
                  'service' : services['wb']},

            {     'id' : 2, 
                  'source' : 1, 
                  'destiny' : 5, 
                  'service' : services['wb']},

            {     'id' : 3, 
                  'source' : 4, 
                  'destiny' : 11, 
                  'service' : services['wb']},

            {     'id' : 4, 
                  'source' : 5, 
                  'destiny' : 7, 
                  'service' : services['wb']},

            {     'id' : 5, 
                  'source' : 11, 
                  'destiny' : 12, 
                  'service' : services['wb']},

            {     'id' : 6, 
                  'source' : 12, 
                  'destiny' : 13, 
                  'service' : services['wb']},

            {     'id' : 7, 
                  'source' : 13, 
                  'destiny' : 15, 
                  'service' : services['wb']},

            {     'id' : 8, 
                  'source' : 0, 
                  'destiny' : 4, 
                  'service' : services['wb']},
            ]
