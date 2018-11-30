class XpPerMinDeltas:
    N_0_to_10 = 0
    N_10_to_20 = 0
    N_20_to_30 = 0
    N_30_to_end = 0

    def __init__(self, dict_info={}):
        if "0-10" in dict_info.keys():
            self.N_0_to_10 = dict_info["0-10"]
        if "10-20" in dict_info.keys():
            self.N_10_to_20 = dict_info["10-20"]
        if "20-30" in dict_info.keys():
            self.N_20_to_30 = dict_info["20-30"]
        if "30-end" in dict_info.keys():
            self.N_30_to_end = dict_info["30-end"]

    def __str__(self):
        cad = ""
        cad += "0-10: " + str(self.N_0_to_10) + "\n"
        cad += "10-20: " + str(self.N_10_to_20) + "\n"
        cad += "20-30: " + str(self.N_20_to_30) + "\n"
        cad += "30-end: " + str(self.N_30_to_end)
        return cad
