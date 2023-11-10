for i in {1..87}
do 
    python add_ctf.py /home/mj7341/dev/research/00_moml/antibody/dataset/conformational/3d_projected/128/mrcs/1hzh.$i.particles.128.mrcs --ctf-pkl /home/mj7341/dev/research/00_moml/antibody/dataset/conformational/ctfs/1hzh.ctfs.$i.pkl --Apix 3 --s1 0 --s2 0 -o /home/mj7341/dev/research/00_moml/antibody/dataset/conformational/add_ctf/128/mrcs/1hzh.$i.128.mrcs --out-png /home/mj7341/dev/research/00_moml/antibody/dataset/conformational/add_ctf/128/pngs/$i.128_ctf.png
done