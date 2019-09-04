#1567157720
ls
#1567157728
exit
#1567159541
sudo yum install -y yum-utils            device-mapper-persistent-data            lvm2
#1567159794
yum install vim
#1567159840
sudo yum-config-manager     --add-repo     https://mirrors.ustc.edu.cn/docker-ce/linux/centos/docker-ce.repo
#1567159847
sudo yum makecache fast
#1567159857
sudo yum install docker-ce
#1567159958
sudo systemctl enable docker
#1567159963
sudo systemctl start docker
#1567159981
docker run hello-world
#1567159992
docker image ls
#1567160002
docker ps -a
#1567160009
docker container prune
#1567160021
docker image rm fce2
#1567160025
docker image ls
#1567160037
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
#1567160068
clear
#1567160083
yum install wget
#1567160104
wget -c "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)"
#1567160175
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
#1567160228
sudo chmod +x /usr/local/bin/docker-compose
#1567160237
nvidia-smi
#1567160262
docker volume ls -q -f driver=nvidia-docker | xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f
#1567160272
sudo yum remove nvidia-docker
#1567160279
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
#1567160285
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo |   sudo tee /etc/yum.repos.d/nvidia-docker.repo
#1567160297
sudo yum install -y nvidia-docker2
#1567160333
sudo pkill -SIGHUP dockerd
#1567160339
docker run --runtime=nvidia --rm nvidia/cuda:9.0-base nvidia-smi
#1567160363
docker ps
#1567160367
docker image ls
#1567160377
docker image rm 1443
#1567160380
ls
#1567160383
df
#1567160459
vim /etc/docker/daemon.json 
#1567160488
sudo systemctl daemon-reload
#1567160494
sudo systemctl restart docker
#1567160495
ls
#1567160522
docker pull cloudac7/deepmd-kit:cuda-9.0-ssh
#1567161137
exit
#1567168507
docker pull cloudac7/cgcnn:cuda-10.0-notebook
#1567168957
docker pull cloudac7/gdynet':cuda-10.0-notebook
#1567168961
docker pull cloudac7/gdynet:cuda-10.0-notebook
#1567170025
docker pulllibatomsquip/quip:py2
#1567170029
docker pull libatomsquip/quip:py2
#1567175052
exit
#1567166134
docker pull cloudac7/deepmd-kit:cuda-9.0-ssh
#1567166865
docker pull cloudac7/dpgen
#1567167336
docker pull cloudac7/cp2k:v6.1
#1567167656
docker pull cloudac7/sisso:notebook
#1567177210
df
#1567177220
docker image ls
#1567179732
ls
#1567180926
cd deepmd-tutorial-20190815/
#1567180926
s
#1567180927
ls
#1567180943
rm -r cp2k_dpgen 
#1567180952
rm -rf cp2k_dpgen.bak
#1567180954
rm -rf cp2k_dpgen.bak-1/
#1567180958
rm -rf cp2k_dpgen.old/
#1567180959
ls
#1567180963
cd cp2k_dpgen
#1567180965
vim param.json 
#1567180983
vim machine_final_all.json 
#1567180987
ls
#1567180989
vim docker-compose.yml 
#1567181019
chmod +x clean.sh 
#1567181021
./clean.sh 
#1567181022
ls
#1567181028
chmod +x command.sh 
#1567181032
vim command.sh 
#1567181037
rm command.sh 
#1567181039
ls
#1567181044
vim exec.sh 
#1567181060
chmod +x exec.sh 
#1567181061
ls
#1567181064
vim param.json 
#1567181120
./exec.sh 
#1567181126
nvidia-smi
#1567181131
ls
#1567181138
tail -f dpgen.log 
#1567182280
ls
#1567182284
cd deepmd-tutorial-20190815/cp2k_dpgen
#1567182285
ls
#1567182295
cd iter.000000/00.train/000/
#1567182299
tail lcurve.out 
#1567182304
vim lcurve.out 
#1567183335
cd ..
#1567183348
tail */lcurve.out
#1567212777
clear
#1567212784
nvidia-smi
#1567212788
ls
#1567212794
cd deepmd-tutorial-20190815/cp2k_dpgen
#1567212795
ls
#1567212826
tail dpgen.log 
#1567212846
df
#1567212903
tail iter.000001/00.train/000/lcurve.out 
#1567212910
tail iter.000001/00.train/00*/lcurve.out 
#1567212921
tail iter.000000/00.train/00*/lcurve.out 
#1567213004
ls
#1567213011
cd iter.000000/02.fp/
#1567213020
wc -l candidate.shuffled.000.out 
#1567213034
cd ..//..
#1567213044
wc -l iter.000001/02.fp/candidate.shuffled.001.out 
#1567213070
wc -l iter.000001/02.fp/*.001.out 
#1567213092
wc -l iter.000000/02.fp/*.001.out 
#1567213097
wc -l iter.000000/02.fp/*.000.out 
#1567213120
exit
#1567217673
clear
#1567217683
ls
#1567217689
cd deepmd-tutorial-20190815/
#1567217690
ls
#1567217695
rm cp2k_dpgen.tgz 
#1567217701
rm -r stored/
#1567217710
rm -rf stored/
#1567217715
ls
#1567217863
cd ybzhuang/
#1567217863
ls
#1567217865
cd cp2k_dpgen/
#1567217866
ls
#1567217869
cd ..
#1567217871
ls
#1567217907
nvidia-smi
#1567217981
exit
#1567218016
ls
#1567218018
rm cp2k_dpgen_1.tgz 
#1567218075
tar -jcvf dp-tut.tar.bz2 deepmd-tutorial-20190815/
#1567218091
ls
#1567218136
yum install zip
#1567218186
ls
#1567218263
docker ps
#1567218267
cd deepmd-tutorial-20190815/cp2k_dpgen/
#1567218270
docker-compose down
#1567218273
ls
#1567218274
cd ..
#1567218275
ls
#1567218278
cd ..
#1567218278
ls
#1567218282
rm dp-tut.tar.bz2 
#1567218291
rm -rf deepmd-tutorial-20190815/
#1567218292
ls
#1567218410
docker ps
#1567218412
docker ps -a
#1567218416
docker image ls
#1567218433
yum install git
#1567218494
wget https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh
#1567219233
wget -c  https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh
#1567219373
docker run -p 8899:8888 --runtime nvidia --rm cgcnn:cuda-10.0-notebook
#1567219382
docker run -p 8899:8888 --runtime nvidia --rm cloudac7/cgcnn:cuda-10.0-notebook
#1567219398
docker run -p 8899:8888 --runtime nvidia -it --rm cloudac7/cgcnn:cuda-10.0-notebook
#1567219434
docker run -p 8899:8888 --runtime nvidia -it --rm cloudac7/cgcnn:cuda-10.0-notebook bash
#1567219453
docker run -p 8899:8888 --runtime nvidia -it --rm cloudac7/gdynet:cuda-10.0-notebook bash
#1567219469
docker ps -a
#1567219471
docker ps
#1567219480
ls
#1567219487
chmod +x Anaconda3-2018.12-Linux-x86_64.sh 
#1567219489
./Anaconda3-2018.12-Linux-x86_64.sh 
#1567219610
ls
#1567219614
rm Anaconda3-2018.12-Linux-x86_64.sh 
#1567219616
ls
#1567219618
ls -al
#1567219620
exit
#1567219628
ls
#1567219637
python
#1567219644
ipython
#1567219652
exit
#1567389568
nvidia-smi
#1567389619
exit
#1567389680
docker image list
#1567389691
exit
#1567389782
ls
#1567389789
pwd
#1567389792
cd .
#1567389794
ls
#1567389796
cd /
#1567389796
ls
#1567389803
cd root/
#1567389803
ls
#1567389872
mkdir gdynet-data
#1567389874
cd gdynet-data/
#1567389879
wget https://archive.materialscloud.org/file/2019.0017/v1/li2s-traj.npz
#1567390258
screen
#1567390260
ls
#1567390270
wget https://archive.materialscloud.org/file/2019.0017/v1/li2s-traj-graph-train.npz
#1567391679
wget https://archive.materialscloud.org/file/2019.0017/v1/li2s-traj-graph-test.npz
#1567391707
wget https://archive.materialscloud.org/file/2019.0017/v1/li2s-traj-graph-val.npz
#1567391925
ls
#1567391928
cd ..
#1567391929
ls
#1567392092
docker run --runtime nvidia -it -v /root:/workplace/gdynet/training cloudac7/gdynet:cuda-10.0-notebook bash
#1567393477
docker run -p 8989:8888 --runtime nvidia -v /root:/workspace/gdynet/training cloudac7/gdynet:cuda-10.0-notebook
#1567393721
ls
#1567394019
exit
#1567399515
ls
#1567399518
docker ps
#1567399704
tar -jxvf dp-tut.tar.bz2 
#1567399744
l
#1567399745
ls
#1567399749
cd deepmd-tutorial-20190815/
#1567399750
ls
#1567399753
cd cp2k_dpgen/
#1567399754
ls
#1567399755
vim param.json 
#1567399773
nvidia-smi
#1567399782
./clean.sh 
#1567399783
ls
#1567399785
./exec.sh 
#1567399798
watch -n 1 nvidia-smi
#1567399825
tail -n dpgen.log 
#1567399830
tail -f dpgen.log 
#1567400379
l
#1567400380
ls
#1567400390
cd iter.000000/00.train/000/
#1567400390
ls
#1567400393
cim lcurve.out 
#1567400396
vim lcurve.out 
#1567400407
cd ..
#1567400455
ls
#1567400455
cd ..
#1567400460
cd deepmd-tutorial-20190815/cp2k_dpgen/
#1567400464
docker-compose down
#1567400470
cd ../..
#1567400470
ls
#1567400475
rm -rf deepmd-tutorial-20190815/
#1567400479
rm -f gdynet-data
#1567400483
rm -f gdynet-data.tgz 
#1567400483
ls
#1567400486
exit
#1567400198
ls
#1567400204
rm dp-tut.tar.bz2 
#1567400206
ls
#1567400238
tar -zcvf gdynet-data.tgz gdynet-data/
#1567516117
ls
#1567516765
yum install libfabric
#1567516881
ls
#1567516946
wget -c http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/15540/l_mkl_2019.4.243.tgz
#1567517177
l
#1567517180
rm l_mkl_2019.4.243.tgz 
#1567517351
ls
#1567517370
rm -f l_mkl_2019.4.243.tgz 
#1567517371
ls
#1567517963
tar -zxvf l_mkl_2019.4.243.tgz 
#1567517984
cd l_mkl_2019.4.243
#1567517985
ls
#1567517988
./install.sh 
#1567518008
ls
#1567518009
cd ..
#1567518010
ls
#1567518218
wget -c http://registrationcenter-download.intel.com/akdlm/irc_nas/tec/15553/l_mpi_2019.4.243.tgz
#1567518223
ls
#1567518226
rm l_mpi_2019.4.243.tgz 
#1567518227
ls
#1567518574
tar -zxvf l_mpi_2019.4.243.tgz 
#1567518585
cd l_mpi_2019.4.243/
#1567518587
./install.sh 
#1567518667
cd ../l_mkl_2019.4.243/
#1567518669
./install
#1567518671
./install.sh 
#1567518812
ls
#1567518814
cd ..
#1567518815
ls
#1567518821
rm -rf l_*
#1567518822
ls
#1567518828
vim .bashrc
#1567518861
source .bashrc
#1567518866
which mpirun
#1567518879
vim hello.c
#1567519003
mpicc hello.c -o intel_hello
#1567519008
mpirun -np 2 /root/intel_hello
#1567519030
echo $LD_LIBRARY_PATH
#1567519044
vim .bashrc
#1567519066
source .bashrc
#1567519072
mpirun -np 2 /root/intel_hello
#1567519087
ls
#1567519098
echo $LD_LIBRARY_PATH
#1567519118
echo $PATH
#1567519124
ls
#1567519126
exit
#1567519141
docker image ls
#1567519143
df
#1567519165
docker pull cloudac7/deepmd-kit:cuda-9.0-ssh-ubuntu16.04
#1567520366
docker pull cloudac7/dpgen
#1567520539
docker image ls
#1567520541
df
#1567520560
docker image rm 189925bcf94b
#1567520578
docker image rm 0bd791a15075
#1567520611
df
#1567520616
docker image ls
#1567520648
exit
#1567521367
yum install unzip
#1567521378
python
#1567521383
exit
#1567521944
ls
#1567521953
tar -zxvf INTER_ac_intel12_61856731171.tgz 
#1567521954
ls
#1567521960
rm hello.c 
#1567521963
rm intel_hello 
#1567521964
ls
#1567521972
tar -zxvf NN_ac_intel12_64960919762.tgz 
#1567521974
ls
#1567521983
tar -zxvf LASP_example\(1\).tgz 
#1567521985
ls
#1567521989
mkdir lasp
#1567521989
ls
#1567522000
rm ./*.tgz
#1567522003
ls
#1567522008
mv INTER_ac2.1.7_intel12_4fg/ lasp/
#1567522013
mv NN_ac2.1.7_intel18/ lasp/
#1567522013
ls
#1567522019
mv LASP_Example/ lasp/
#1567522020
ls
#1567522022
cd lasp/
#1567522023
ls
#1567522025
cd INTER_ac2.1.7_intel12_4fg/
#1567522026
ls
#1567522035
vim README 
#1567522067
ls
#1567522068
cd ..
#1567522069
ls
#1567522070
cd ..
#1567522071
ls
#1567522073
exit
#1567525820
ls
#1567525824
unzip gap-tutorial.zip 
#1567525825
ls
#1567525830
rm gap-tutorial
#1567525833
rm gap-tutorial.zip 
#1567525834
exit
#1567558250
clear
#1567558254
ls
#1567558260
mkdir temp
#1567558263
cd temp
#1567558264
ls
#1567558269
vim Dockerfile
#1567558278
docker image ls
#1567558292
vim Dockerfile
#1567558375
docker build -t libatomsquip/quip:py2-sklearn .
#1567558595
docker image list
#1567585468
ls
#1567585469
exit
#1567584570
ls
#1567584574
cd gap-tutorial/
#1567584575
ll
#1567584576
cd ..
#1567584577
ls
#1567584579
cd lasp
#1567584586
ll
#1567584796
cd ..
#1567584797
ls
#1567584800
cd gap-tutorial/
#1567584801
ll
#1567585290
ls
#1567585372
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
#1567585399
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key
#1567585426
ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key
#1567585446
/etc/init.d/sshd start
#1567585454
locate sshd
#1567586714
ll
#1567586729
mkdir Tutorial
#1567586761
ll
#1567585474
ll
#1567585523
cd lasp/
#1567585524
ll
#1567585528
cd LASP_Example/
#1567585529
ll
#1567585532
cd ..
#1567585532
ls
#1567585533
cd ..
#1567585533
ls
#1567585561
cd lasp/
#1567585562
ls
#1567585564
cd ..
#1567585566
cd gap-tutorial/
#1567585567
ll
#1567585574
cd ..
#1567585575
ls
#1567585618
pwd
#1567585673
ll
#1567586823
cd Tutorial/
#1567586824
ll
#1567586883
cd ..
#1567586884
ls
#1567586906
cp -r gap-tutorial/ Tutorial/
#1567586915
cp -r lasp/ Tutorial/
#1567586916
ll
#1567586932
mkdir TarFiles
#1567586940
tar czf gap-tutorial/
#1567586948
tar czf gap-tutorial.tar.gz gap-tutorial/
#1567586964
tar czf lasp.tar.gz lasp/
#1567586968
ll
#1567586975
mv *.tar.gz TarFiles/
#1567586976
ll
#1567586985
docker run -it --rm -v /root/gap-tutorial/:/root/tutor/ -p 8889:8889 libatomsquip/quip
#1567587417
docker run -it --rm -v /root/gap-tutorial/:/root/tutor/ -p 8889:8899 libatomsquip/quip
#1567587545
ll
#1567587565
cd TarFiles/
#1567587566
ll
#1567587568
ll -h
#1567587572
cd ..
#1567587572
ls
#1567587575
cd NVIDIA_CUDA-9.0_Samples/
#1567587576
ll
#1567587579
cd ..
#1567587580
ls
#1567587593
tar czf NVIDIA_CUDA-9.0_Samples.tar.gz NVIDIA_CUDA-9.0_Samples/
#1567587608
cd gdynet-data/
#1567587608
ll
#1567587611
ll -h
#1567587615
cd ..
#1567587615
ls
#1567587619
ll -h
#1567587631
mv NVIDIA_CUDA-9.0_Samples.tar.gz TarFiles/
#1567587632
ll
#1567587635
cd TarFiles/
#1567587635
ls
#1567587637
pwd
#1567587843
ll
#1567587844
cd ..
#1567587845
ls
#1567587848
cd lasp/
#1567587849
ll
#1567587851
cd LASP_Example/
#1567587852
ll
#1567587855
cd allexamples/
#1567587855
ll
#1567587859
cd ..
#1567587860
ll
#1567587861
cd NN
#1567587862
ll
#1567587871
cd ..
#1567587872
ls
#1567587872
ll
#1567587875
cd VASP/
#1567587875
ll
#1567587877
cd ..
#1567587878
ls
#1567587879
cd ..
#1567587879
ls
#1567587882
cd NN_ac2.1.7_intel18/
#1567587882
ll
#1567587891
cd Examples/
#1567587891
ll
#1567587892
cd ..
#1567587893
ls
#1567587894
cd ..
#1567587894
ls
#1567587895
cd ..
#1567587896
ls
#1567587898
cd ..
#1567587898
ls
#1567587900
cd ..
#1567587900
ls
#1567587903
cd home/
#1567587904
ls
#1567587906
cd ..
#1567587907
cd root/
#1567587908
ls
#1567587911
cd gap-tutorial/
#1567587912
ll
#1567587929
exit
