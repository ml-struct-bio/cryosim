for pdb in 1tjg 4kht 7che 7m6d 8i5i
do
    for i in {1..87}
    do 
    python add_noise.py /home/mj7341/dev/research/00_moml/antibody/dataset/compositional/add_ctf/128/mrcs/$pdb.$i.128.mrcs -o /home/mj7341/dev/research/00_moml/antibody/dataset/compositional/add_noise/mrcs/$pdb.$i.128.noised.mrcs --snr .1 --out-png /home/mj7341/dev/research/00_moml/antibody/dataset/compositional/add_noise/pngs/$pdb.$i.128.noised.png
    done
done