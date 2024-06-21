#Rivers for RDR2

rdr2_rivers = {
    'beartooth Beck': 'ambarino',
    'kamassa': 'bayou nwa',
    'little creek': 'big valley',
}

for rivers in rdr2_rivers:
    territory = rdr2_rivers[rivers]
    print(f"\n The {rivers.title()} from RDR2 is in: {territory.title()}")

print("\nRDR2 rivers:")
for rivers in rdr2_rivers.keys():
    print(f"\n{rivers.title()}")

print("\nRDR2 territories that contain rivers:")
for territory in rdr2_rivers.values():
    print(f"\n{territory.title()}")