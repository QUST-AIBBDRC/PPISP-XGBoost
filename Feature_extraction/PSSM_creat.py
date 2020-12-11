

import os
import re

def command_pssm(content, output_file,pssm_file):

    os.chdir(r'D:\blast2.2.27+\bin')
    os.system('psiblast \
              -in_msa %s \
              -db swissprot \
              -num_threads 10 \
              -num_iterations 3 \
              -evalue 0.001 \
              -out %s \
              -out_ascii_pssm %s '%(content,output_file,pssm_file))

#对每个序列进行PSSM打分
def pssm(proseq,outdir):
    inputfile = open(proseq,'r')
    content = ''
    input_file = '' 
    output_file = ''
    pssm_file = ''
    chain_name = []
    for eachline in inputfile:
        if '>' in eachline:
            if len(content):
                temp_file = open(outdir + '\\fasta\\' + chain_name,'w')
                temp_file.write(content)
                temp_file.close()
                input_file = outdir + '\\fasta\\' + chain_name
                output_file = outdir + '\\out\\' + chain_name + '.out'
                pssm_file = outdir + '\\pssm\\' + chain_name + '.pssm'                
                command_pssm(input_file, output_file,pssm_file)
            content = ''
            chain_name = eachline.strip()[1:]
        content +=  ''.join(eachline)


    if len(content):
        temp_file = open(outdir + '\\fasta\\' + chain_name,'w')
        temp_file.write(content)
        temp_file.close()
        input_file = outdir + '\\fasta\\' + chain_name
        output_file = outdir + '\\out\\' + chain_name + '.out'
        pssm_file = outdir + '\\pssm\\' + chain_name + '.pssm'


        command_pssm(input_file, output_file,pssm_file)  
        
    inputfile.close()       


def formateachline(eachline):


    col = re.split('\s+',eachline.strip())[:22]
    column = []
    for c in col:
        column.append(c)


    return column

def simplifypssm(pssmdir,newdir):
    listfile = os.listdir(pssmdir)
    for eachfile in listfile:
        if os.path.isfile(pssmdir+'/'+eachfile)and eachfile.endswith('.pssm'):
            with open(pssmdir + '/' + eachfile,'r') as inputpssm:
                with open(newdir + '/' + eachfile,'w') as outfile:
                    count = 0
                    for eachline in inputpssm:
                        count +=1
                        if count <= 3:
                            continue
                        if not len(eachline.strip()):
                            break
                        oneline = formateachline(eachline)
                        for one in oneline[:-1]:
                            outfile.write(one+'\t')
                        outfile.write(oneline[-1]+'\n')
        elif os.path.isdir(pssmdir+'/'+eachfile):
            if not os.path.exists(newdir+'/'+eachfile):
                os.mkdir(newdir+'/'+eachfile)
            simplifypssm(pssmdir+'/'+eachfile,newdir+'/'+eachfile)
                    


def standardPSSM(window_size,pssmdir,outdir):
    listfile = os.listdir(pssmdir)
    for eachfile in listfile:
        outfile = open(outdir + '/' + eachfile, 'w') 
        with open(pssmdir + '/' + eachfile, 'r') as inputf:
            inputfile = inputf.readlines()
            for linenum in range(len(inputfile)):
                content = []
                first = [];second = [];third=[];last=[]
                if linenum < window_size/2:
                    for i in range((window_size/2 - linenum)*20):
                        second.append('\t0')
                if window_size/2 - linenum > 0:
                    countline = window_size - (window_size/2 - linenum)
                else:
                    countline = window_size  #get needed line count

                linetemp = 0
                for eachline in inputfile:
                    if linetemp < linenum-window_size/2:
                        linetemp += 1
                        continue
                    if linetemp == linenum:
                        thisline = eachline.split('\t')
                        for j in range(0,2):
                            if j>0:
                                first.append('\t')
                            first.append(thisline[j].strip())
                    if countline > 0:
                        oneline = eachline.split('\t')
                        for j in range(2,len(oneline)):
                            third.append('\t' + oneline[j].strip())
                        countline -=1
                    else:
                        break
                    linetemp += 1
                while countline:
                    for i in range(20):
                        last.append('\t0')
                    countline -=1
                content += first + second + third + last
                outfile.write(''.join(content) + '\n')
        outfile.close()
        


def computedPSSM(window_size,pssmdir,outdir):
    listfile = os.listdir(pssmdir)
    for eachfile in listfile:
        outfile = open(outdir + '/' + eachfile, 'w') 
        with open(pssmdir + '/' + eachfile, 'r') as inputf:
            inputfile = inputf.readlines()
            for linenum in range(len(inputfile)):
                content = []
                first = [];second = []
                if window_size/2 - linenum > 0:
                    countline = window_size - (window_size/2 - linenum)
                else:
                    countline = window_size  #get needed line count

                linetemp = 0
                for eachline in inputfile:
                    if linetemp < linenum-window_size/2:
                        linetemp += 1
                        continue
                    if linetemp == linenum:
                        thisline = eachline.split('\t')
                        for j in range(0,2):
                            if j>0:first.append('\t')
                            first.append(thisline[j].strip())
                    if countline > 0: 
                        oneline = eachline.split('\t')[2:len(eachline)]
                        tline = []
                        for i in range(len(oneline)):
                            tline.append(int(oneline[i]))
                        if len(second)==0:
                            second += tline
                        else:
                            second = list(map(lambda x: x[0]+x[1], zip(second, tline)))
                        countline -=1 
                    else:
                        break 
                    linetemp += 1 
                format_second = []
                for i in range(len(second)):
                    format_second.append('\t' + str(second[i]))
                content += first + format_second 
                outfile.write(''.join(content) + '\n')
        outfile.close()

def smoothedPSSM(window_size,pssmdir,outdir):
    standardPSSM(window_size,pssmdir, outdir)




proseq=r' '
outdir=r' '
PSSMmaker.pssm(proseq,outdir)