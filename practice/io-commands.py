#this example was a problem set before to use less packages and more code to do a movement and zip of files.

# directories
source = "/logs"
dest = "/etc"

# extensions considered backup
backup_ext = (".bak", ".backup", ".old", ".bkp")

os = __import__("os")

moved = []

# read files in /logs
for f in os.listdir(source):

    if f.endswith(backup_ext):
        src_path = source + "/" + f
        dst_path = dest + "/" + f

        if os.path.isfile(src_path):
            os.rename(src_path, dst_path)
            moved.append(dst_path)
            print("Moved:", f)

# create tar archive
tar_name = dest + "/backup_files.tar.gz"

cmd = "tar -czf " + tar_name + " " + " ".join(moved)
os.system(cmd)

print("Archive created:", tar_name)