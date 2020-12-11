    load('r');
for i=1:186
    sign=num2str(i);
    path=[sign,'.pssm'];
    A{i}=importdata(path);    
    data_pssm=A{i}.data; 
    positive=obtain_positive{i};
    negative=obtain_negative{i};
    number=max([positive(end),negative(end)]);
    
    h_sign=[];
    for h=1:length(positive)
        if positive(h)>number-4
            h_sign=[h_sign,h];
        end
    end
    positive(h_sign)=[];
    if positive (4)<5
        H=positive (:,5:end);
    elseif positive (3)<5
        H=positive (:,4:end);
    elseif positive (2)<5
        H=positive (:,3:end);
    elseif positive (1)<5
        H=positive (:,2:end);
    else
        H=positive ;
    end
    
    for h=1:length(positive)
        for m=1:length(H)
        H1=H(m)-4;
        H2=H(m)+4;
        data=data_pssm(H1:H2,1:20);
        data_pssm_positive{m,1}=data;
    end
   
end
        data_shu{i}=data_pssm_positive;
        clear data_pssm_positive
        
    h_sign=[];
    for k=1:length(negative)
        if negative(k)>number-4
            h_sign=[h_sign,k];
        end
    end
    negative(h_sign)=[];
    if negative(4)<5
        H=negative(:,5:end);
    elseif negative(3)<5
        H=negative(:,4:end);
    elseif negative(2)<5
        H=negative(:,3:end);
    elseif negative(1)<5
        H=negative(:,2:end);
    else
        H=negative;
    end
    
    for b=1:length(H)
        H1=H(b)-4;
        H2=H(b)+4;
        data2=data_pssm(H1:H2,1:20);
        data_pssm_negative{b,1}=data2;
    end
        
        data_shu1{i}=data_pssm_negative;
        clear data_pssm_negative
end

save A186.mat data_shu data_shu1





