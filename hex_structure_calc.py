# Calculator for sides of hex shade structure

import math

theta = math.radians(60.)

horiz = 10/math.tan(theta)
print "Horizontal distance out from structure: %d ft" % horiz

ext = horiz * math.tan(math.radians(60))
print "Bottom edge: %d ft" % (ext*2 + 8)


ext_diag = ext/math.sin(math.radians(60))
print "Horizontal length of diagonal: %d ft" % ext_diag

diag = math.sqrt(100 + ext_diag**2)
print "Diagonal length: %d ft" % diag

angle = math.degrees(math.asin(10/diag))
print "Angle from bottom: %d degrees" % angle

# Fabric View: 
#                      8'
#               /--------------\
#              /                \ 
#   diag = 15'/                  \
#            /                    \
#           /                      \
#          --------------------------  <- angle = 40 degrees
#               (ext*2 + 8) = 28'
                              
# Side view:
# 
#       |\
#       | \ 
#   10' |  \
#       |   \
#       |    \
#       -------  <- 60 degrees  
#      horiz = 5'
          
# Top View: 
#                          8'
#                   /--------------\
#                  /                \ 
#   ext_diag = 11'/                  \
#                /                    \
#               /                      \
#              --------------------------  <- theta = 60 degrees
#                   (ext*2 + 8) = 28'