for i in {1..87}
do 
    python add_noise.py /home/mj7341/dev/research/00_moml/antibody/dataset/conformational/add_ctf/128/mrcs/1hzh.$i.128.mrcs -o /home/mj7341/dev/research/00_moml/antibody/dataset/conformational/add_noise/mrcs/1hzh.$i.128.noised.mrcs --snr .1 --out-png /home/mj7341/dev/research/00_moml/antibody/dataset/conformational/add_noise/pngs/$i.128.noised.png
done