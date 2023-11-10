for pdb in 1tjg 4kht 7che 7m6d 8i5i
do
    for i in {1..87}
    do 
        python add_ctf.py /home/mj7341/dev/research/00_moml/antibody/dataset/compositional/3d_projected/128/mrcs/$pdb.$i.vol.128.mrcs --ctf-pkl /scratch/gpfs/ZHONGE/mj7341/research/00_moml/antibody/dataset/compositional/ctfs/$pdb.ctfs.$i.pkl --Apix 3 --s1 0 --s2 0 -o /home/mj7341/dev/research/00_moml/antibody/dataset/compositional/add_ctf/128/mrcs/$pdb.$i.128.mrcs --out-png /home/mj7341/dev/research/00_moml/antibody/dataset/compositional/add_ctf/128/pngs/$i.128_ctf.png
    done
done