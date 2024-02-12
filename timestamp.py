import os
import mdtraj as md
import zipfile
from google.colab import files  #for google colab


pdb_file = 'path_to_your_pdb_file.pdb'
traj_file = 'path_to_your_trajectory_file.xtc'


u = md.load(pdb_file)
traj = md.load(traj_file, top=pdb_file)


frame_step = 252

output_dir = 'output_files/'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)


for i in range(0, len(traj), frame_step):
    output_file_name = output_dir + 'output_{:06d}.xtc'.format(i)
    md.Trajectory(traj.xyz[i], u.topology).save(output_file_name)


zip_file_name = 'output.zip'
with zipfile.ZipFile(zip_file_name, 'w') as zipf:
    for filename in os.listdir(output_dir):
        zipf.write(os.path.join(output_dir, filename), filename)

files.download(zip_file_name)
