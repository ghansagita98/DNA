import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("usage: python dna.py <database file> <input file>")
        exit()

    # TODO: Read database file into a variable
    db = []

    with open(sys.argv[1]) as db_file:
        reader = csv.DictReader(db_file)
        for row in reader:
            db += [row]

    # TODO: Read DNA sequence file into a variable
    sequence = ""

    with open(sys.argv[2]) as s_file:
        for line in s_file:
            sequence = line

    # TODO: Find longest match of each STR in DNA sequence
    tmp = {}

    for data in db:
        for key in data:
            if key != "name":
                tmp[key] = str(longest_match(sequence, key))

    # TODO: Check database for matching profiles
    for data in db:
        container = data.copy()
        del container["name"]
        if container == tmp:
            print(data["name"])
            exit()

    print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
