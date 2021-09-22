import sys
import os
#Script returning a value of KEFF for T_F, T_M, AtomDensity_M, Library 

#uses and modifies a template file to be used as input for dragon
def modifyTemplate(T_F, T_M, MD, L):
    #open template file for rdragon5 
    f = open("templateFileWIMS.x2m", "r")
    list_of_lines = f.readlines()
    f.close()
    #Update fuel temperature
    #list_of_lines[44] = "  MIX 1 " + T_F + "\n"
    list_of_lines[37] = "  MIX 1 " + T_F + "\n"    
    #Update cladding temperature
    #list_of_lines[52] = "  MIX 2 " + T_M + "\n"
    list_of_lines[43] = "  MIX 2 " + T_M + "\n"
    #Update moderator temperature
    #list_of_lines[82] = "  MIX 3 " + T_M + "\n"
    list_of_lines[73] = "  MIX 3 " + T_M + "\n"
    #calculate and modify atom density
    #volumetric weight of Boron from conc. (PPM) and moderator density
    MD = float(MD)
    B_vw = MD * 0.0013
    #taking isotopic fractions of B_10, B_11 as 0.119, 0.801 resp.
    #AD_B10 = B_vw * 0.24844E-25*6.022E23
    AD_B10 = MD *  1.44105E-5
    AD_B10 = str(AD_B10)
    AD_B10 = AD_B10.replace("e", "E")
    #AD_B11 = B_vw * 0.75156E-25*6.022E23
    AD_B11 = MD * 5.80042E-5
    AD_B11 = str(AD_B11)
    AD_B11 = AD_B11.replace("e", "E")
    #volumetric weight of O, H from that of Boron and moderator density
    O_vw = (MD - B_vw)/18
    H_vw = (MD - B_vw)/9
    AD_O = O_vw * 6.022E-1
    AD_H = H_vw * 6.022E-1
    AD_O = str(AD_O)
    AD_H = str(AD_H) 
    #Update resp. Atom Densities
    #list_of_lines[83] = "    H1H2O    = 'H1_H2O'   " + AD_H + "\n"
    #list_of_lines[84] = "    O16H2O   = 'O16'   " + AD_O + "\n"
    #list_of_lines[85] = "    B10      = 'B10'   " + AD_B10 + "\n"
    #list_of_lines[86] = "    B11      = 'B11'   " + AD_B11 + "\n"
    #Update library
    #list_of_lines[42] = "  DEPL LIB: DRAGON FIL: " + L + "\n"
    #list_of_lines[43] = "  MIXS LIB: DRAGON FIL: " + L + "\n"
    #Update resp. Atom Densities
    list_of_lines[74] = "    H1H2O    = '3001'   " + AD_H + "\n"
    list_of_lines[75] = "    O16H2O   = '6016'   " + AD_O + "\n"
    list_of_lines[76] = "    B10      = '510'   " + AD_B10 + "\n"
    list_of_lines[77] = "    B11      = '511'   " + AD_B11 + "\n"
    #Update library
    list_of_lines[35] = "  DEPL LIB: WIMSD4 FIL: " + L + "\n"
    list_of_lines[36] = "  MIXS LIB: WIMSD4 FIL: " + L + "\n"
    f = open("templateFileWIMS.x2m", "w")
    f.writelines(list_of_lines)
    f.close()

def getKEFF(): 
    with open('templateFileWIMS.result','r') as file:   
        # reading each line    
        for line in file:
            # reading each word        
            for word in line.split():
                if word.startswith("KEFF=") and (word.endswith("=")==False):
                    # display KEFF           
                    #return (word + " PRECISION=" + str(line.split()[-1]))
		    return(word[5:])

def PCM(getKEFF, k_theory):
    #isolate KEFF from output
    #KEFF=float(getKEFF.split()[0][5:])    
    #calculate PCM
    PCM = (float(getKEFF)-float(k_theory))*(100000/float(k_theory))
    return (str(PCM))

def main(T_F, T_M, MD, L, KEFF_T):
    modifyTemplate(T_F, T_M, MD, L)
    os.system('rdragon5 templateFileWIMS.x2m')
    #return one line with all input and output info
    return [T_F, T_M, MD, L, KEFF_T, getKEFF(), PCM(getKEFF(), KEFF_T)]

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
