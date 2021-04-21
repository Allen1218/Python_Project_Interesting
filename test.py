# import numpy as np
# import matplotlib.pyplot as plt
#
# # Compute the x and y coordinates for points on a sine curve
# x = np.arange(0, 3 * np.pi, 0.1)
# y = np.sin(x)
#
# # Plot the points using matplotlib
# plt.plot(x, y)
# plt.show()  # You must call plt.show() to make graphics appear.


import requests

# url = 'Http://localhost:8888/http-gateway/rulembx/RULEdefault/INT_GetUnitUOP'
# d = {
#       "UNIT_ID": "FN694270DW8KTY2AN",
#       "STEP_NAME": "FDR-EXPORT",
#       "EQP_NAME": "ITKS_E01-2FAP-01_1_WIFI-BT-COND-2"
#     }

url = 'http://localhost:8888/http-gateway/api2mbx35/TXNdefault/FwLotsListTxn'
d={
    "userName":"FwAdmin",
    "password":"FwAdmin"
}
r = requests.get(url)
print(r.content)