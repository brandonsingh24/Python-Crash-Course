
#Rivers for RDR2

RDR2 = {
    'rdr2_rivers' : {
        'beartooth beck': 'ambarino',
        'kamassa': 'bayou nwa',
        'little creek': 'big valley',
        },

    'characters' : {
        'RDR2_main': 'arthur morgan',
        'RDR2_epilogue': 'john marston',
        },
}
for rivers, character in RDR2.items():
    if 'little creek' in character:
        print(f"\n The {character['little creek']}, from RDR2 is in:")

else:
    print("That's all folks.")


###I can make this code look a lot better later.