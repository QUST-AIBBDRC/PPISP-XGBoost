
load('A186.mat')
data=[data_shu{1,1}...]
lamdashu=9;
for i=1:M
    fid{i}=data{i,1}
end
c=cell(M,1);
for t=1:M
    clear shu d
shu=fid{t};


[M,N]=size(shu);
shuju=shu(1:9,1:20);
d=[];


 for i=1:9
   for j=1:20
       d(i,j)=1/(1+exp(-shuju(i,j)));
   end
end
c{t}=d(:,:);
end


for i=1:M
[MM,NN]=size(c{i});
 for  j=1:20
   x(i,j)=sum(c{i}(:,j))/MM;
 end
end


xx=[];
sheta=[];
shetaxin=[];


for lamda=1:lamdashu;
for t=1:M
  [MM,NN]=size(c{t});
  clear xx
   for  j=1:20
      for i=1:MM-lamda
       xx(i,j)=(c{t}(i,j)-c{t}(i+lamda,j))^2;
      end
      sheta(t,j)=sum(xx(1:MM-lamda,j))/(MM-lamda);
   end
end
shetaxin=[shetaxin,sheta];
end
  psepssm=[x,shetaxin];

