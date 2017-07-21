# Extracting all film type data
# Subject format: http://dbtropes.org/resource/Film/[Film Title]

import re

def main():
    film_data = open('film_data.nt', 'w')
    with open('dbtropes.nt') as rawfile:
        for line in rawfile:
            if re.match("<http://dbtropes.org/resource/Film/", line):
                film_data.write(line)
        film_data.close()

if __name__ == "__main__":
    main()
