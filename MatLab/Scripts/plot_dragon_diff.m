clear all
close all
% load dragon output
address='/Users/mac/Documents/Stage_EPFL/MatLab/';
%outname='CASEA_1L';
outname='2C_2L';
%load([address outname '.mat']);
%ref=pow; clear pow
%outname='CASEA_ALEX';
load([address outname '.mat']);
% load pinpower mask
mask_assA;
% fill mask
MAT=zeros(17,17);
for i=1:length(pow)
    MAT(find(mask==i))=(pow(i)-ref(i))/ref(i)*100;
    %MAT(find(mask==i))=pow(i);
    %disp(pow(i));
end
figure();
[M,N]=size(MAT);
h2=imagesc(MAT); 
colormap(b2r(-1,1)); 
%caxis([0.9 1.1]);colorbar;% plot the matrix
caxis([-8.0 8.0]);colorbar;% plot the matrix
hold on
for k = 1:M+1
    x = [k k]-0.5;
    y = [1 N+1]-0.5;
    plot(x,y,'Color','k','LineStyle','-','LineWidth',1);
    plot(y,x,'Color','k','LineStyle','-','LineWidth',1);
end 

alphabet={'A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'K' 'L'  'M' 'N' 'O' 'P' 'Q' 'R' 'S'};
ax = gca; % handle of current axes
Xlbl=[1:NX];
Ylbl=alphabet(1:NY);
set(ax, 'XTick', 1:length(Xlbl),'TickLength',[0.001,0.01]); % center x-axis ticks on bins
set(ax, 'YTick', 1:length(Ylbl)); % center y-axis ticks on bins
set(ax, 'XTickLabel', Xlbl); % set x-axis labels
set(ax, 'YTickLabel', flip(Ylbl)); % set y-axis label
%set(gca, 'FontSize',24); % set y-axis label
saveas(h2,[address outname '_pinpowerDiff'],'png')
