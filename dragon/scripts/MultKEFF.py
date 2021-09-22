import sys
import os
#Script returning a value of KEFF for T_F, T_M, AtomDensity_M, Library 

#uses and modifies all template files to be used as input for dragon
def modifyTemplate(T_F, T_M, MD, LibType, L, Desc):
    #open template file for rdragon5 
    f = open("templateASSBLY.x2m", "r")
    fLines = f.readlines()
    
    #Update library
    #templateASSBLY_2L
    #fLines[20] = "STRING Library := " + '"' +  L + '"' + " ;" + "\n" 
    #templateASSBLY_1L
    fLines[26] = "STRING Library := " + '"' +  L + '"' + " ;" + "\n" 
    #templateASSBLY_Simple
    #fLines[22] = "STRING Library := " + '"' +  L + '"' + " ;" + "\n" 

    f = open("templateASSBLY.x2m", "w")
    f.writelines(fLines)
    f.close()
   
    #UPDATE GEOMETRIES  
    
    if Desc == "NP":
        os.system('cp Geo_SSNP.c2m Geo_SS.c2m')
        os.system('cp Geo_N1NP.c2m Geo_N1.c2m')
        os.system('cp Geo_N2NP.c2m Geo_N2.c2m')
        os.system('cp Geo_SSNP_1L.c2m Geo_SS_1L.c2m')
        os.system('cp Mix_UOX_NP.c2m Mix_UOX.c2m')
        os.system('cp Mix_UOX_1L_NP.c2m Mix_UOX_1L.c2m')
    elif Desc == "12P":
        os.system('cp Geo_SS12P.c2m Geo_SS.c2m')
        os.system('cp Geo_N112P.c2m Geo_N1.c2m')
        os.system('cp Geo_N212P.c2m Geo_N2.c2m')
        os.system('cp Geo_SS12P_1L.c2m Geo_SS_1L.c2m')
    elif Desc == "24P":  
	os.system('cp Geo_SS24P.c2m Geo_SS.c2m')
        os.system('cp Geo_N124P.c2m Geo_N1.c2m')
        os.system('cp Geo_N224P.c2m Geo_N2.c2m')
        os.system('cp Geo_SS24P_1L.c2m Geo_SS_1L.c2m')
    elif Desc == "AIC":
        os.system('cp Geo_SSA.c2m Geo_SS.c2m')
        os.system('cp Geo_N1A.c2m Geo_N1.c2m')
        os.system('cp Geo_N2A.c2m Geo_N2.c2m')
        os.system('cp Geo_SSA_1L.c2m Geo_SS_1L.c2m')
    elif Desc == "B4C":
        os.system('cp Geo_SSB.c2m Geo_SS.c2m')
        os.system('cp Geo_N1B.c2m Geo_N1.c2m')
        os.system('cp Geo_N2B.c2m Geo_N2.c2m')
        os.system('cp Geo_SSB_1L.c2m Geo_SS_1L.c2m')
    elif Desc == "IT":
        os.system('cp Geo_SSIT.c2m Geo_SS.c2m')
        os.system('cp Geo_N1IT.c2m Geo_N1.c2m')
        os.system('cp Geo_N2IT.c2m Geo_N2.c2m')
        os.system('cp Geo_SSIT_1L.c2m Geo_SS_1L.c2m')
    elif Desc == "12G":
        os.system('cp Geo_SS12G.c2m Geo_SS.c2m')
        os.system('cp Geo_N112G.c2m Geo_N1.c2m')
        os.system('cp Geo_N212G.c2m Geo_N2.c2m')
        os.system('cp Geo_SS12G_1L.c2m Geo_SS_1L.c2m')
    elif Desc == "24G":
        os.system('cp Geo_SS24G.c2m Geo_SS.c2m')
        os.system('cp Geo_N124G.c2m Geo_N1.c2m')
        os.system('cp Geo_N224G.c2m Geo_N2.c2m')
        os.system('cp Geo_SS24G_1L.c2m Geo_SS_1L.c2m')
    elif Desc == "80IFBA":
        os.system('cp Geo_SS80IFBA.c2m Geo_SS.c2m')
        os.system('cp Geo_N180IFBA.c2m Geo_N1.c2m')
        os.system('cp Geo_N280IFBA.c2m Geo_N2.c2m')
        os.system('cp Geo_SS80IFBA_1L.c2m Geo_SS_1L.c2m')

    #UPDATE MIX
    #if LibType == "WIMS":
    #	   os.system('cp Mix_UOX_WIMS.c2m Mix_UOX.c2m')
    #if LibType == "DLIB":
    #    os.system('cp Mix_UOX_Drag.c2m Mix_UOX.c2m')
    
    mix2 = open("Mix_UOX.c2m", "r")
    mix2Lines = mix2.readlines()
    
    mix1 = open("Mix_UOX_1L.c2m", "r")
    mix1Lines = mix1.readlines()
    
    #Update fuel temperature
    #list_of_lines[26] = "MIX 1 " + sys.argv[1] + "\n"
    mix2Lines[79] = "MIX 3 " + T_F + "\n"
    mix1Lines[86] = "MIX 3 " + T_F + "\n"
    #Update cladding temperature
    mix2Lines[46] = "MIX 2 " + T_M +  "\n"
    mix1Lines[51] = "MIX 2 " + T_M +  "\n"
    mix2Lines[97] = "MIX 8 " + T_M +  "\n"
    mix1Lines[109] = "MIX 8 " + T_M +  "\n"
    #Update mo6erator temperature
    mix2Lines[39] = "MIX 1 " + T_M + "\n"
    mix1Lines[42] = "MIX 1 " + T_M + "\n"
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
    if LibType == "WIMS":
        mix2Lines[40] = "   H1H2O    = '3001'   " + AD_H + "\n"
        mix2Lines[41] = "   O16H2O   = '6016'   " + AD_O + "\n"
        mix2Lines[42] = "   B10      = '10'   " + AD_B10 + "\n"
        mix2Lines[43] = "   B11      = '11'   " + AD_B11 + "\n"
        mix2Lines[33] = "  DEPL LIB: WIMSD4 FIL: <<Library>>" + "\n"
        mix2Lines[36] = "  MIXS LIB: WIMSD4 FIL: <<Library>>" + "\n"

    elif LibType == "DLIB":
        mix2Lines[40] = "   H1H2O    = 'H1_H2O'   " + AD_H + "\n"
        mix2Lines[41] = "   O16H2O   = 'O16'   " + AD_O + "\n"
        mix2Lines[42] = "   B10      = 'B10'   " + AD_B10 + "\n"
        mix2Lines[43] = "   B11      = 'B11'   " + AD_B11 + "\n"
        mix2Lines[33] = "  DEPL LIB: DRAGON FIL: <<Library>>" + "\n"
        mix2Lines[36] = "  MIXS LIB: DRAGON FIL: <<Library>>" + "\n"
        mix1Lines[43] = "   H1H2O    = 'H1_H2O'   " + AD_H + "\n"
        mix1Lines[44] = "   O16H2O   = 'O16'   " + AD_O + "\n"
        mix1Lines[45] = "   B10      = 'B10'   " + AD_B10 + "\n"
        mix1Lines[46] = "   B11      = 'B11'   " + AD_B11 + "\n"
        mix1Lines[34] = "  DEPL LIB: DRAGON FIL: <<Library>>" + "\n"
        mix1Lines[37] = "  MIXS LIB: DRAGON FIL: <<Library>>" + "\n"

    mix2 = open("Mix_UOX.c2m", "w")
    mix2.writelines(mix2Lines)
    mix2.close()

    mix1 = open("Mix_UOX_1L.c2m", "w")
    mix1.writelines(mix1Lines)
    mix1.close()
    

def getKEFF(): 
    with open('templateASSBLY.result','r') as file:   
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

def main(T_F, T_M, MD, Libtype, L, Desc, KEFF_T):
    modifyTemplate(T_F, T_M, MD,Libtype, L, Desc)
    os.system('rdragon6 templateASSBLY.x2m')
    #return one line with all input and output info
    return [T_F, T_M, MD, Libtype, L, Desc, KEFF_T, getKEFF(), PCM(getKEFF(), KEFF_T)]

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
