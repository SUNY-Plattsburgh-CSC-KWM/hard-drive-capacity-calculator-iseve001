print("Hard drive code goes here")
platters = int(input("input # of platters - "))
surfaces = int(input("input # of surfaces per platter - "))
tracks = int(input("input # of tracks per surface - "))
sectors = int(input("input # of sectors per track - "))
byte = int(input("input # of bytes - "))
total_bytes = (platters * surfaces * tracks * sectors * byte)
kb = total_bytes / 1024
mb = kb / 1024
gb = mb / 1024
tb = gb / 1024
if tb > 1.0:
    print(f"your drive is {tb:.1f} TB")
elif gb > 1.0:
    print(f"your drive is {gb:.1f} GB")
elif mb > 1.0:
    print(f"your drive is {mb:.1f} MB")
elif kb > 1.0:
    print(f"your drive is {kb:.1f} KB")
else:
    print(f"your drive is {total_bytes} Bytes")
