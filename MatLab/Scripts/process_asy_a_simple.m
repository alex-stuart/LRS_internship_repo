clc
clear
%address='C:\Users\mhursin\Desktop\Review\Alex\summary\';
address='/Users/mac/Documents/Stage_EPFL/MatLab/';
filename='ASSBLY_CASEA_ALEX_2C_corr.txt';
outdata='2D_simple';
%define ref
refFile =  csvread([address 'refPinPowerMaps.csv'],1,0);
lineNum = double(filename(20))-64;
ref = refFile(lineNum,:);
nmix = 161;
ngrpd = 2;
nbnus = 4;
% correspondance between mixtures number and fuel rods
fr_to_mix = [ ...
    0, 0, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 3, 3, 3, 3, ...
    4, 4, 4, 4, 5, 5, 5, 5, 0, 6, 6, 6, 6, ...
    7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, ...
    11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14, ...
    15, 15, 15, 15, ...
    16, 16, 16, 16, 17, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 19, ...
    20, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, ...
    23, 23, 23, 23, 24, 24, 24, 24, 25, 25, 25, 25, 26, 26, 26, 26, ...
    27, 27, 27, 27, 28, 28, 28, 28, 29, 29, 29, 29, 30, 30, 30, 30, ...
    31, 31, 31, 31, ...
    32, 32, 32, 32, 33, 33, 33, 33, 34, 34, 34, 34, 35, 35, 35, 35, ...
    36, 36, 36, 36, 37, 37, 37, 37, 38, 38, 38, 38, 39, 39, 39, 39, ...
    ];
mix_to_cell=zeros(nmix,1);
mix_to_cell([3 4 5 6])=1;
mix_to_cell([9 10 11 12])=2;
mix_to_cell([114 115 116 117])=3;
mix_to_cell([94 95 96 97])=4;
mix_to_cell([122 123 124 125])=5;
mix_to_cell([126 127 128 129])=6;
mix_to_cell([154 155 156 157])=7;
mix_to_cell([158 159 160 161])=8;
cell_to_fr=[  1,1,  1,1,  4,6, ...
              2,2,1,2,2,1,2,6,...
                2,1,2,2,1,2,6,...
                    1,1,  4,6,...
                    2,1,1,2,6,...
                        1,3,6,...
                        2,3,6,...
                          5,7,...
                            8];
[nfmd, ngmd, prod, nfall_d, ngall_d, nftot_d_1g, ngtot_d_1g, volume] = ...
         parse_dragon(nmix, ngrpd, nbnus, [address filename]);
mat_filename = [address outdata '.mat'];
% reaction rate per unit volume
nftot_d_1g_vol=nftot_d_1g./volume';
processed_nftot_d_1g_vol=zeros(nmix,1);
indx=zeros(nmix,1);
for i=1:length(cell_to_fr)
    processed_nftot_d_1g_vol(find(fr_to_mix==i))=nftot_d_1g_vol(find(mix_to_cell==cell_to_fr(i)));
    indx(find(fr_to_mix==i))=find(mix_to_cell==cell_to_fr(i));
end



tot_pow=sum(processed_nftot_d_1g_vol)/max(fr_to_mix);
for i=1:max(fr_to_mix)
    pow(i)=sum(processed_nftot_d_1g_vol(find(fr_to_mix==i)))./tot_pow;
end
save(mat_filename, 'nfmd', 'ngmd', 'prod', 'nfall_d', 'ngall_d', 'nftot_d_1g', 'ngtot_d_1g','volume','pow','ref', '-v7');


